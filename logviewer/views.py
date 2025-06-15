from django.shortcuts import render
from django.db.models import Count
from .models import RequestLog
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import io
import base64
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Django Logger Home Page!")
def log_stats(request):
    data = (
        RequestLog.objects
        .values('status_code')
        .annotate(count=Count('id'))
        .order_by('status_code')
    )
    codes = [d['status_code'] for d in data]
    counts = [d['count'] for d in data]

    plt.figure(figsize=(6,4))
    plt.bar(codes, counts)
    plt.title("Requests by Status Code")
    plt.xlabel("Status Code")
    plt.ylabel("Count")
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    graph = base64.b64encode(buf.getvalue()).decode()
    buf.close()

    return render(request, 'logviewer/log_stats.html', {'graph': graph})
