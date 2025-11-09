from fastapi import FastAPI, Query, Response, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
from datetime import datetime
import pandas as pd
from functools import lru_cache
import hashlib
import json
import traceback

app = FastAPI(title="IoT Sensor Analytics Platform")

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,  # Set to False when using allow_origins=["*"]
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

# Simple dictionary-based cache
cache = {}

def get_cache_key(location: Optional[str], sensor: Optional[str], 
                 start_date: Optional[str], end_date: Optional[str]) -> str:
    """Generate a cache key from query parameters"""
    params = {
        "location": location,
        "sensor": sensor,
        "start_date": start_date,
        "end_date": end_date
    }
    # Create a hash of the sorted parameters
    param_str = json.dumps(params, sort_keys=True)
    return hashlib.md5(param_str.encode()).hexdigest()

def load_sensor_data():
    """Load sensor data from CSV file"""
    import os
    # Get the project root directory (parent of src)
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(project_root, 'data', 'q-fastapi-timeseries-cache.csv')
    df = pd.read_csv(csv_path)
    # Convert timestamp to datetime (parse as UTC, then convert to naive)
    df['timestamp'] = pd.to_datetime(df['timestamp'], utc=True)
    # Convert to timezone-naive (remove timezone info for easier comparison)
    df['timestamp'] = df['timestamp'].dt.tz_convert(None)
    return df

@app.get("/stats")
async def get_stats(
    response: Response,
    location: Optional[str] = Query(None, description="Filter by location"),
    sensor: Optional[str] = Query(None, description="Filter by sensor type"),
    start_date: Optional[str] = Query(None, description="Start date (ISO format)"),
    end_date: Optional[str] = Query(None, description="End date (ISO format)")
):
    """
    Get statistics for sensor data with optional filters.
    Returns count, average, min, and max values.
    Implements caching - identical requests return X-Cache: HIT header.
    """
    try:
        # Generate cache key
        cache_key = get_cache_key(location, sensor, start_date, end_date)
        
        # Check cache
        if cache_key in cache:
            response.headers["X-Cache"] = "HIT"
            return cache[cache_key]
        
        # Load data
        df = load_sensor_data().copy()
        
        # Apply filters
        if location:
            df = df[df['location'] == location]
        
        if sensor:
            df = df[df['sensor'] == sensor]
        
        if start_date:
            start_dt = pd.to_datetime(start_date)
            # Convert to timezone-naive if timezone-aware
            if isinstance(start_dt, pd.Timestamp) and start_dt.tz is not None:
                start_dt = start_dt.tz_convert(None)
            df = df[df['timestamp'] >= start_dt]
        
        if end_date:
            end_dt = pd.to_datetime(end_date)
            # Convert to timezone-naive if timezone-aware
            if isinstance(end_dt, pd.Timestamp) and end_dt.tz is not None:
                end_dt = end_dt.tz_convert(None)
            df = df[df['timestamp'] <= end_dt]
        
        # Calculate statistics
        if len(df) == 0:
            stats = {
                "count": 0,
                "avg": 0.0,
                "min": 0.0,
                "max": 0.0
            }
        else:
            stats = {
                "count": len(df),
                "avg": round(df['value'].mean(), 2),
                "min": round(df['value'].min(), 2),
                "max": round(df['value'].max(), 2)
            }
        
        # Prepare response
        result = {"stats": stats}
        
        # Store in cache
        cache[cache_key] = result
        response.headers["X-Cache"] = "MISS"
        
        return result
    except Exception as e:
        # Return error details for debugging
        import traceback
        error_detail = f"Error: {str(e)}\nTraceback: {traceback.format_exc()}"
        raise HTTPException(status_code=500, detail=error_detail)

@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
        "message": "IoT Sensor Analytics Platform",
        "endpoints": {
            "/stats": "Get sensor statistics with optional filters (location, sensor, start_date, end_date)"
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

