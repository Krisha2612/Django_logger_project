from django.urls import path
from . import views

urlpatterns = [
    path('', views.log_stats, name='log_stats'),  # ✅ this matches /log-stats/
]
