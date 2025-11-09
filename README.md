# IoT Analytics Project

A comprehensive project containing multiple components for IoT sensor analytics, data processing, and CI/CD automation.

## 📁 Project Structure

```
iot-analytics-project/
├── .github/workflows/     # GitHub Actions CI/CD workflows
├── src/                   # Source code (FastAPI application)
├── data/                  # Data files (CSV, JSON)
├── tests/                 # Test scripts
├── scripts/               # Utility scripts
├── docs/                  # Documentation
└── requirements.txt       # Python dependencies
```

## 🚀 Quick Start

### 1. Navigate to Project Directory

```bash
cd iot-analytics-project
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the FastAPI Server

```bash
# From project root
python src/main.py

# Or using uvicorn
uvicorn src.main:app --reload --host 127.0.0.1 --port 8000
```

### 4. Test the API

```bash
# Run tests
python tests/quick_test.py
python tests/test_all_queries.py
```

## 📋 Components

### 1. FastAPI IoT Sensor Analytics (`src/main.py`)

- **Endpoint**: `/stats`
- **Features**: 
  - Query sensor data with filters (location, sensor, date range)
  - Response caching with X-Cache headers
  - CORS enabled
  - Statistics: count, avg, min, max

### 2. LSB Steganography (`scripts/extract_lsb.py`)

Extract hidden messages from images using LSB steganography.

```bash
python scripts/extract_lsb.py
```

### 3. GitHub Actions CI/CD (`.github/workflows/matrix-build.yml`)

Multi-platform matrix build with artifact management.

## 📊 Data Files

- `data/q-fastapi-timeseries-cache.csv` - IoT sensor time-series data
- `data/network_graph.csv` - Network graph data for MST calculation
- `data/sales_data.csv` - Sales transaction data
- `data/stego_image.json` - Image data for steganography

## 🧪 Testing

All test files are in the `tests/` directory:

- `test_api.py` - Comprehensive API tests
- `test_all_queries.py` - Test all query types
- `test_cache.py` - Test caching functionality
- `test_cors.py` - Test CORS headers
- `test_date_query.py` - Test date range queries
- `quick_test.py` - Quick API test

## 📚 Documentation

See `docs/` directory for detailed documentation:

- `README.md` - API documentation
- `GITHUB_ACTIONS_SETUP.md` - CI/CD setup guide
- `SERVER_RESTART_INSTRUCTIONS.md` - Server management
- `FIXES_APPLIED.md` - Bug fixes and improvements

## 🔧 Scripts

- `scripts/extract_lsb.py` - LSB steganography extraction
- `scripts/transform.js` - JavaScript data transformation
- `scripts/service_reliability_query.sql` - SQL queries

## 🌐 API Usage

```bash
# Get all statistics
curl http://127.0.0.1:8000/stats

# Filter by location
curl http://127.0.0.1:8000/stats?location=zone-a

# Filter by sensor
curl http://127.0.0.1:8000/stats?sensor=temperature

# Date range
curl "http://127.0.0.1:8000/stats?start_date=2024-01-01&end_date=2024-01-31"

# Combined filters
curl "http://127.0.0.1:8000/stats?location=zone-b&sensor=pressure&start_date=2024-01-01"
```

## 📝 Next Steps

1. **Initialize Git Repository** (if not already done):
   ```bash
   git init
   git add .
   git commit -m "Initial commit: IoT Analytics Project"
   ```

2. **Create GitHub Repository**:
   - Go to GitHub and create a new repository
   - Push your code:
     ```bash
     git remote add origin <your-repo-url>
     git push -u origin main
     ```

3. **GitHub Actions**:
   - The workflow will automatically run on push
   - Check Actions tab to see matrix builds

4. **Update Email in README**:
   - Edit `docs/README.md` and add your email address

## 📧 Contact

**Contact:** your.email@example.com

## 📄 License

This project is for educational/demonstration purposes.

