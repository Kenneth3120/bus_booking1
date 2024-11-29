from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_bus, name='upload_bus'),
    path('buses/', views.list_buses, name='list_buses'),
]
