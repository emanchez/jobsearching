from django.shortcuts import render
from django.http import HttpResponse
from joblist.models import JobListing
from django.template import loader

# Create your views here.

def listing(request, jobId):
    return HttpResponse("You're looking at job # %s." % jobId)

def error(request):
    return HttpResponse("404 page not found")

def index(request):
    latestListing = JobListing.objects.all()[:10]
    template = loader.get_template("joblist/index.html")
    context = {
        "latest_job_listings": latestListing,
    }
    return HttpResponse(template.render(context, request))
