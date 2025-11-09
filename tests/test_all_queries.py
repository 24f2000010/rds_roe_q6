import requests
import json

BASE_URL = "http://127.0.0.1:8000"

print("Testing All Query Types")
print("=" * 60)

# Test 1: location=zone-b, sensor=pressure
print("\n1. location=zone-b, sensor=pressure")
r = requests.get(f"{BASE_URL}/stats?location=zone-b&sensor=pressure")
print(f"   Status: {r.status_code}")
print(f"   X-Cache: {r.headers.get('X-Cache', 'N/A')}")
print(f"   Response: {json.dumps(r.json(), indent=2)}")

# Test 2: Date range query
print("\n2. Date range: 2024-01-01 to 2024-01-31")
r = requests.get(f"{BASE_URL}/stats?start_date=2024-01-01&end_date=2024-01-31")
print(f"   Status: {r.status_code}")
print(f"   X-Cache: {r.headers.get('X-Cache', 'N/A')}")
if r.status_code == 200:
    print(f"   Response: {json.dumps(r.json(), indent=2)}")
else:
    print(f"   Error: {r.text[:200]}")

# Test 3: Combined filters
print("\n3. Combined: location=zone-b, sensor=pressure, date range")
r = requests.get(f"{BASE_URL}/stats?location=zone-b&sensor=pressure&start_date=2024-01-01&end_date=2024-01-31")
print(f"   Status: {r.status_code}")
print(f"   X-Cache: {r.headers.get('X-Cache', 'N/A')}")
print(f"   Response: {json.dumps(r.json(), indent=2)}")

# Test 4: Check CORS headers
print("\n4. Checking CORS headers")
r = requests.options(f"{BASE_URL}/stats")
print(f"   Access-Control-Allow-Origin: {r.headers.get('Access-Control-Allow-Origin', 'N/A')}")
print(f"   Access-Control-Allow-Methods: {r.headers.get('Access-Control-Allow-Methods', 'N/A')}")

print("\n" + "=" * 60)
print("All tests completed!")

