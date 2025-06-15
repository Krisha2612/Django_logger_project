from django.db import models

class RequestLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    method = models.CharField(max_length=10)
    path = models.TextField()
    status_code = models.IntegerField()
    duration = models.FloatField()

    def __str__(self):
        return f"[{self.timestamp}] {self.method} {self.path} = {self.status_code}"
