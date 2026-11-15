
import time
import requests
import statistics

BASE_URL = "http://127.0.0.1:8000"


def test_api_response_time():
    response_times = []

    for _ in range(10):
        start = time.perf_counter()

        response = requests.get(
            f"{BASE_URL}/health",
            timeout=5
        )

        end = time.perf_counter()

        assert response.status_code == 200

        response_times.append((end - start) * 1000)

    average_time = statistics.mean(response_times)
    maximum_time = max(response_times)

    print(f"\nAverage Response Time: {average_time:.2f} ms")
    print(f"Maximum Response Time: {maximum_time:.2f} ms")

    assert average_time < 1000, "API response is too slow"
