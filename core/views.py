from django.shortcuts import render
from django.http import JsonResponse
import time

def home(request):
    return JsonResponse({"message": "Welcome to LatencyLens!"})

def healthz(request):
    start = time.time()
    # Simulate a tiny operation
    time.sleep(0.05)
    latency = (time.time() - start) * 1000  # ms
    return JsonResponse({"status": "ok", "latency_ms": round(latency, 2)})


