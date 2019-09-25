from django.shortcuts import render
from .models import Projects

# Create your views here.


def projects(request):
    projects_obj = Projects.objects.all().order_by('-pk')
    context = {
        'projects': projects_obj
    }
    return render(request, 'projects/project.html', context)



def projects_detail(request, pk):
    project = Projects.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'projects/project_detail.html', context)