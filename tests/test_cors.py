import requests

# Test without Origin header
r1 = requests.get('http://127.0.0.1:8000/stats')
print('Without Origin header:')
print(f'  Access-Control-Allow-Origin: {r1.headers.get("Access-Control-Allow-Origin", "N/A")}')

# Test with Origin header (simulates browser request)
r2 = requests.get('http://127.0.0.1:8000/stats', headers={'Origin': 'http://localhost:3000'})
print('\nWith Origin header (browser simulation):')
print(f'  Access-Control-Allow-Origin: {r2.headers.get("Access-Control-Allow-Origin", "N/A")}')
print(f'  Status: {r2.status_code}')

