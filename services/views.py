from django.shortcuts import render
from .models import Services

# Create your views here.


def services(request):
    services = Services.objects.all().order_by('-pk')
    context = {
        'services': services
    }
    return render(request, 'services/services.html', context)


def services_details(request, pk):
    service = Services.objects.get(pk=pk)
    context = {
        'service': service
    }
    return render(request, 'services/services_details.html', context)
