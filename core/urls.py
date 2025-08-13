from django.urls import path
from . import views

urlpatterns = [
    path('healthz/', views.healthz, name='healthz'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
