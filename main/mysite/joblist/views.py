from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse
from joblist.models import JobListing
from django.template import loader

# Create your views here.

def listing(request, jobId):
    return HttpResponse("You're looking at job # %s." % jobId)

def error(request):
    return HttpResponse("404 page not found")

def index(request):
    latestListing = JobListing.objects.all()[:100]
    paginator = Paginator(latestListing, 9) 
    template = loader.get_template("joblist/index.html")
    
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "latest_job_listings": page_obj,
    }
    return HttpResponse(template.render(context, request))


# mostly followed tutorial on django docs "https://docs.djangoproject.com/en/4.2/intro/tutorial01/"
# reference for django pagination: "https://docs.djangoproject.com/en/4.2/topics/pagination/"