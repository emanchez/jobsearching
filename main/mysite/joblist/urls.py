from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("listing/<int:jobId>/", views.listing, name="listing"),
    path("error", views.error, name="error")
]
