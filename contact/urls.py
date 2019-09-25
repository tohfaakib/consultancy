from django.urls import path
from .views import contact, email_sending

urlpatterns = [
    path('contact/', contact, name='contact'),
    path('send_mail', email_sending, name='send_mail')
]