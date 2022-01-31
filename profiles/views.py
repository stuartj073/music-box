from django.shortcuts import render, get_object_or_404
from .models import Users

# Create your views here.

def profile(request):
    """ Display a user's profile. """
    template = 'profiles/profiles.html'

    return render(request, template)