import time
import logging
from .models import RequestLog

logger = logging.getLogger(__name__)

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = time.time()
        response = self.get_response(request)
        duration = time.time() - start

        RequestLog.objects.create(
            method=request.method,
            path=request.path,
            status_code=response.status_code,
            duration=duration
        )
        logger.info(f"{request.method} {request.path} -> {response.status_code} ({duration:.3f}s)")
        return response
