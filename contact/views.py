from django.shortcuts import render, redirect

from .models import Contact

from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def contact(request):
    return render(request, 'contact/contact.html')


def email_sending(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        country = request.POST.get("country")
        subject = request.POST.get("subject")
        messages = request.POST.get("message")

        subject = email + ': '+subject
        message = messages
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['tnishan7@gmail.com', 'petergsalmon12@gmail.com', ]
        send_mail(subject, message, email_from, recipient_list)

        contacts = Contact()

        contacts.name = name
        contacts.email = email
        contacts.country = country
        contacts.subject = subject
        contacts.messages = messages

        contacts.save()

        return redirect('/contact')
    return render(request, 'contact/contact.html')



