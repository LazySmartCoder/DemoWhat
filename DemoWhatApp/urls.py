from django.contrib import admin
from django.urls import path, include
from DemoWhatApp.views import *

urlpatterns = [
    path("", index, name = "HomePage"),
    path("subnum", subnum, name = "subnum"),
    path("viewprof", viewprof, name = "viewprof"),
]
