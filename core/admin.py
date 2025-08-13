from django.contrib import admin
from .models import LatencyResult

@admin.register(LatencyResult)
class LatencyResultAdmin(admin.ModelAdmin):
    list_display = ("server", "latency_ms", "checked_at")
    list_filter = ("server", "checked_at")
    ordering = ("-checked_at",)
