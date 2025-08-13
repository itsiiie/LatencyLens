from django.http import JsonResponse
from .latency_checker import check_latency
from .models import LatencyResult
from django.shortcuts import render
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


def dashboard(request):
    # Get last 50 latency results, newest first
    latency_results = LatencyResult.objects.order_by('-checked_at')[:50]
    return render(request, 'core/dashboard.html', {'latency_results': latency_results})