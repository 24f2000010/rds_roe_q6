# Project Structure

```
iot-analytics-project/
├── .github/
│   └── workflows/
│       └── matrix-build.yml          # GitHub Actions CI/CD
├── src/
│   └── main.py                       # FastAPI application
├── data/
│   ├── q-fastapi-timeseries-cache.csv
│   ├── network_graph.csv
│   ├── sales_data.csv
│   └── stego_image.json
├── tests/
│   ├── test_api.py
│   ├── test_all_queries.py
│   ├── test_cache.py
│   ├── test_cors.py
│   ├── test_date_query.py
│   └── quick_test.py
├── scripts/
│   ├── extract_lsb.py                # LSB steganography extraction
│   ├── transform.js                   # JavaScript transformation
│   └── service_reliability_query.sql # SQL query
├── docs/
│   ├── README.md
│   ├── GITHUB_ACTIONS_SETUP.md
│   ├── SERVER_RESTART_INSTRUCTIONS.md
│   └── FIXES_APPLIED.md
├── requirements.txt
└── PROJECT_STRUCTURE.md              # This file
```

