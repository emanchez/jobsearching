from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:jobId>/", views.listing, name="listing")
]
