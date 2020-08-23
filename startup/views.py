from django.shortcuts import render
from django.http import HttpResponse
from . models import Startup
from django.shortcuts import reverse
from django.http import HttpResponseRedirect
from . forms import NewStartupForm
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.views import generic

# Create your views here.
def index(request):
    template_name = 'startup/index.html'
    return render(request, template_name)

def startups(request):
    startups = Startup.objects.order_by('date_added')
    paginator = Paginator(startups, 6)
    page = request.GET.get('page')
    startups = paginator.get_page(page)
    context = {'startups': startups}
    template_name = 'startup/index.html'
    return render(request, template_name, context)

def addstartup(request):
	""" allow users to add new startup """
	if request.method != 'POST':
		# no data submitted, create a new form
		form = NewStartupForm()

	else:
		# data has been submitted, time to process it 
		form = NewStartupForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('startups'))

	context = {"form": form}
	template_name = 'startup/newstartup.html'
	return render(request, template_name, context)

def detail(request, startup_id):
	""" allow investors to view the detail for a startup """
	startup = Startup.objects.get(pk=startup_id)
	template_name = 'startup/startup_detail.html'
	context = {'startup': startup}
	return render(request, template_name, context)

# class DetailView(generic.DetailView):
# 	model = Startup
# 	template_name = 'startup/startup_detail.html'


