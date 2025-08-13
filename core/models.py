from django.db import models

class LatencyResult(models.Model):
    server = models.URLField()            # The server URL that was pinged
    latency_ms = models.FloatField(null=True)  # Latency in milliseconds, can be None if failed
    checked_at = models.DateTimeField(auto_now_add=True)  # Timestamp of the check

    def __str__(self):
        return f"{self.server} - {self.latency_ms} ms at {self.checked_at}"



