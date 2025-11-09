# Server Restart Instructions

## Issue
The server is running old code and needs to be restarted to pick up the fixes for date range queries and CORS.

## To Restart the Server

### Option 1: Stop and Restart
1. Find the running Python process:
   ```powershell
   Get-Process python | Where-Object {$_.Path -like "*python*"}
   ```
2. Stop the process (or use Ctrl+C if running in terminal)
3. Restart:
   ```bash
   python main.py
   ```
   or
   ```bash
   uvicorn main:app --reload
   ```

### Option 2: Use --reload flag (Auto-restart)
If you started with `uvicorn main:app --reload`, it should auto-reload on file changes.

## Fixed Issues

1. ✅ **Date Range Queries**: Fixed timezone handling for date comparisons
2. ✅ **CORS Configuration**: Fixed `allow_credentials` issue that could cause browser fetch errors
3. ✅ **Error Handling**: Added proper exception handling with detailed error messages

## Test After Restart

```bash
# Test date range query
python -c "import requests; r = requests.get('http://127.0.0.1:8000/stats?start_date=2024-01-01&end_date=2024-01-31'); print(r.json())"

# Test combined filters
python -c "import requests; r = requests.get('http://127.0.0.1:8000/stats?location=zone-b&sensor=pressure&start_date=2024-01-01'); print(r.json())"
```

## Browser Access

After restart, the API should work from browsers. The CORS fix should resolve "TypeError: Failed to fetch" errors.

Test URL: `http://127.0.0.1:8000/stats?location=zone-b&sensor=pressure`

