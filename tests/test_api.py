import requests
import json

BASE_URL = "http://127.0.0.1:8000"

def test_stats_endpoint():
    """Test the /stats endpoint with various queries"""
    
    print("Testing FastAPI IoT Sensor Analytics Platform")
    print("=" * 60)
    
    # Test 1: No filters
    print("\n1. Test with no filters:")
    response = requests.get(f"{BASE_URL}/stats")
    print(f"   Status: {response.status_code}")
    print(f"   X-Cache: {response.headers.get('X-Cache', 'N/A')}")
    print(f"   Response: {json.dumps(response.json(), indent=2)}")
    
    # Test 2: With location filter
    print("\n2. Test with location filter (zone-a):")
    response = requests.get(f"{BASE_URL}/stats?location=zone-a")
    print(f"   Status: {response.status_code}")
    print(f"   X-Cache: {response.headers.get('X-Cache', 'N/A')}")
    print(f"   Response: {json.dumps(response.json(), indent=2)}")
    
    # Test 3: With sensor filter
    print("\n3. Test with sensor filter (temperature):")
    response = requests.get(f"{BASE_URL}/stats?sensor=temperature")
    print(f"   Status: {response.status_code}")
    print(f"   X-Cache: {response.headers.get('X-Cache', 'N/A')}")
    print(f"   Response: {json.dumps(response.json(), indent=2)}")
    
    # Test 4: With date range
    print("\n4. Test with date range:")
    response = requests.get(f"{BASE_URL}/stats?start_date=2024-01-01&end_date=2024-01-31")
    print(f"   Status: {response.status_code}")
    print(f"   X-Cache: {response.headers.get('X-Cache', 'N/A')}")
    print(f"   Response: {json.dumps(response.json(), indent=2)}")
    
    # Test 5: Combined filters
    print("\n5. Test with combined filters (location + sensor):")
    response = requests.get(f"{BASE_URL}/stats?location=zone-a&sensor=temperature")
    print(f"   Status: {response.status_code}")
    print(f"   X-Cache: {response.headers.get('X-Cache', 'N/A')}")
    print(f"   Response: {json.dumps(response.json(), indent=2)}")
    
    # Test 6: Cache hit test (same query as test 1)
    print("\n6. Test cache hit (same query as test 1):")
    response = requests.get(f"{BASE_URL}/stats")
    print(f"   Status: {response.status_code}")
    print(f"   X-Cache: {response.headers.get('X-Cache', 'N/A')}")
    print(f"   Response: {json.dumps(response.json(), indent=2)}")
    
    print("\n" + "=" * 60)
    print("All tests completed!")

if __name__ == "__main__":
    try:
        test_stats_endpoint()
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to the server.")
        print("Please make sure the FastAPI server is running:")
        print("  python main.py")
        print("  or")
        print("  uvicorn main:app --reload")

