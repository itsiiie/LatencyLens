from django.http import JsonResponse
from .latency_checker import check_latency
from .models import LatencyResult

SERVERS = [
    "https://www.google.com",
    "https://www.github.com"
]
def home(request):
    return ("welcome")
def healthz(request):
    latencies = check_latency(SERVERS)

    # Save results to database
    for server, latency in latencies.items():
        LatencyResult.objects.create(server=server, latency_ms=latency)

    return JsonResponse({"status": "ok", "latencies": latencies})
