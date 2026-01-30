from django.shortcuts import render
from django.views.generic import DetailView
from .models import *

# Create your views here.

class ProfileDetailView(DetailView):
    model = Profile
    template_name = "home.html"
    context_object_name = "profile"
    