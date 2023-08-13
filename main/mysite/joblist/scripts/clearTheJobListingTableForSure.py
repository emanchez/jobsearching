
from joblist.models import JobListing


def run():
    JobListing.objects.all().delete()


    print("success!")