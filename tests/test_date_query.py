import requests
import json

# Test date query
r = requests.get('http://127.0.0.1:8000/stats?start_date=2024-01-01&end_date=2024-01-31')
print(f'Status: {r.status_code}')
print(f'Headers: {dict(r.headers)}')
try:
    print(f'Response: {json.dumps(r.json(), indent=2)}')
except:
    print(f'Error text: {r.text}')

