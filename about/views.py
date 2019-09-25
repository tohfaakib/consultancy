from django.shortcuts import render
from .models import About, FAQ

# Create your views here.

def about(request):
    about = About.objects.all().order_by('-pk')
    faqs = FAQ.objects.all().order_by('-pk')
    context = {
        'about': about,
        'faqs': faqs
    }
    return render(request, 'about/about.html', context)
