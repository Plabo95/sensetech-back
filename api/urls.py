from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path("receivedata/", views.receiveData, name="receiveData"),
    path("devices/", views.devices, name="devices"),
    path("records/", views.records, name="records"),
]