import time
import requests

def check_latency(servers):
    """
    Check latency to a list of servers.

    Args:
        servers (list): List of URLs to ping.

    Returns:
        dict: Server URL as key, latency in ms as value.
    """
    results = {}
    for server in servers:
        try:
            start = time.time()
            requests.get(server, timeout=2)
            latency = (time.time() - start) * 1000  # convert to milliseconds
            results[server] = round(latency, 2)
        except requests.RequestException:
            results[server] = None
    return results
