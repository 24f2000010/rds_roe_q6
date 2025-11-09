import requests

# Test cache functionality
print("Testing cache functionality:")
print("-" * 40)

# First request
r1 = requests.get('http://127.0.0.1:8000/stats?sensor=temperature')
print(f"First request:")
print(f"  X-Cache: {r1.headers.get('X-Cache')}")
print(f"  Stats: {r1.json()['stats']}")

# Second request (same query - should be cached)
r2 = requests.get('http://127.0.0.1:8000/stats?sensor=temperature')
print(f"\nSecond request (same query):")
print(f"  X-Cache: {r2.headers.get('X-Cache')}")
print(f"  Stats: {r2.json()['stats']}")

if r2.headers.get('X-Cache') == 'HIT':
    print("\n[OK] Cache is working!")
else:
    print("\n[ERROR] Cache not working")

