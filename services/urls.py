from django.urls import path
from .views import services, services_details


urlpatterns = [
    path('services/', services, name='services'),
    path('services/<int:pk>/', services_details, name='services_details')
]
