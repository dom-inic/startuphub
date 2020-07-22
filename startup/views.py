from django.shortcuts import render
from django.http import HttpResponse
from . models import Startup

# Create your views here.
def index(response):
    template_name = 'startup/index.html'
    return render(response, template_name)

def startup_list(response):
    startup = Startup.objects.order_by('date_added')
    context = {'startup': startup}
    template_name = 'startup/index.html'
    return render(response, template_name, context)