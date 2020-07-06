from django.shortcuts import render
from django.http import HttpResponse
from . models import Startup

# Create your views here.
def index(response):
    template_name = 'startup/index.html'
    return render(response, template_name)

def startup_list(response):
    headlines = Startup.objects.all() [::-1]
    context = {'object_list': headlines}
    template_name = 'startup/index.html'
    return render(response, template_name, context)