
# scripts/importcsv.py

# thank cethegeek from https://stackoverflow.com/questions/1882469/how-do-i-transfer-data-in-csv-file-into-my-sqlite-database-in-django
# for this script from 2009!!

############ All you need to modify is below ############
# Full path and name to your csv file
csv_filepathname="C:\\Users\\Default\\XAMPP\\htdocs\\jobsearch\\crawler\\data\\jobs.csv"
# Full path to the directory immediately above your django project directory
your_djangoproject_home="C:\\Users\\shyth\\Documents\\Code\\jobsearch demo\\main\\mysite"
############ All you need to modify is above ############

# import sys,os
# sys.path.append(your_djangoproject_home)
# os.environ['DJANGO_SETTINGS_MODULE'] ='mysite.settings'

from joblist.models import JobListing

import csv

def run():
    dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')

    for row in dataReader:
        listing=JobListing()
        listing.jobUrl=row[0]
        listing.jobTitle=row[1]
        listing.jobLocation=row[2]
        listing.jobAttributes=row[3]
        listing.jobDescription=row[4]
        listing.save()

    print("success!")