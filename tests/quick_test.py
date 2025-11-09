import requests
import time

# Wait for server to start
time.sleep(3)

try:
    # Test the endpoint
    response = requests.get('http://127.0.0.1:8000/stats?location=zone-a')
    print(f"Status: {response.status_code}")
    print(f"X-Cache: {response.headers.get('X-Cache', 'N/A')}")
    print(f"Response: {response.json()}")
except Exception as e:
    print(f"Error: {e}")
    print("Make sure the server is running: uvicorn main:app --reload")

