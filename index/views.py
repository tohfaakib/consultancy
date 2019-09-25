from django.shortcuts import render
from .models import Slider, SliderText
from about.models import FAQ
from projects.models import Projects

# Create your views here.


def index(request):
    slider = Slider.objects.all().order_by('-created_at')
    sliderText = SliderText.objects.all().order_by('-created_at')
    faqs = FAQ.objects.all().order_by('-pk')
    projects_obj = Projects.objects.all().order_by('-pk')

    if len(projects_obj) > 4:
        projects_obj = projects_obj[:4]

    context = {
        'slider': slider,
        'sliderText': sliderText,
        'faqs': faqs,
        'projects': projects_obj,
    }

    return render(request, 'index/index.html', context)
