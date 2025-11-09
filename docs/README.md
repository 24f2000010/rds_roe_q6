# IoT Sensor Analytics Platform

FastAPI service for analyzing IoT sensor data with intelligent caching.

**Contact:** your.email@example.com

## Features

- ✅ `/stats` endpoint with optional query parameters
- ✅ Response caching with `X-Cache` header (HIT/MISS)
- ✅ CORS enabled for all origins
- ✅ Filters: location, sensor, start_date, end_date
- ✅ Returns: count, avg, min, max statistics

## Installation

```bash
pip install -r requirements.txt
```

## Running the Server

```bash
# Option 1: Using Python
python main.py

# Option 2: Using uvicorn directly
uvicorn main:app --reload
```

The server will start at: `http://127.0.0.1:8000`

## API Endpoints

### GET /stats

Get statistics for sensor data with optional filters.

**Query Parameters:**
- `location` (optional): Filter by location (e.g., "zone-a", "zone-b")
- `sensor` (optional): Filter by sensor type (e.g., "temperature", "humidity", "pressure", "light")
- `start_date` (optional): Start date in ISO format (e.g., "2024-01-01")
- `end_date` (optional): End date in ISO format (e.g., "2024-01-31")

**Response Headers:**
- `X-Cache`: "HIT" for cached responses, "MISS" for fresh calculations

**Example Request:**
```
GET http://127.0.0.1:8000/stats?location=zone-a&sensor=temperature
```

**Example Response:**
```json
{
  "stats": {
    "count": 45,
    "avg": 22.5,
    "min": 15.2,
    "max": 34.8
  }
}
```

## Example Usage

```bash
# Get all statistics
curl http://127.0.0.1:8000/stats

# Filter by location
curl http://127.0.0.1:8000/stats?location=zone-a

# Filter by sensor
curl http://127.0.0.1:8000/stats?sensor=temperature

# Filter by date range
curl "http://127.0.0.1:8000/stats?start_date=2024-01-01&end_date=2024-01-31"

# Combined filters
curl "http://127.0.0.1:8000/stats?location=zone-a&sensor=temperature&start_date=2024-01-01"
```

## Caching

The service implements intelligent caching:
- Identical requests (same query parameters) return cached results
- Cache hit: `X-Cache: HIT` header
- Cache miss: `X-Cache: MISS` header
- Cache key is generated from all query parameters

## Data Format

The CSV file should have the following columns:
- `timestamp`: ISO format timestamp
- `location`: Location identifier
- `sensor`: Sensor type
- `value`: Numeric sensor value

