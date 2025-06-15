from django.contrib import admin
from django.urls import path, include
from logviewer import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('log-stats/', include('logviewer.urls')),
    path('', views.home),  # ✅ handle root URL
]
