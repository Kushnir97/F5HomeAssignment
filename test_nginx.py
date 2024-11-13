import requests

# URLs to test
urls = ["http://nginx-container:8080", "http://nginx-container:8081"]

for url in urls:
    try:
        response = requests.get(url)
        print(f"Testing {url}: Status Code {response.status_code}")
        if url.endswith('8080') and response.status_code != 200:
            raise Exception(f"Expected 200 OK, got {response.status_code}")
        if url.endswith('8081') and response.status_code != 503:
            raise Exception(f"Expected 503 Service Unavailable, got {response.status_code}")
    except Exception as e:
        print(f"Test failed: {e}")
        with open("/results/fail", "w") as f:
            f.write("Test failed")
        exit(1)

# If all tests pass
with open("/results/succeeded", "w") as f:
    f.write("Test succeeded")

print("All tests passed")
