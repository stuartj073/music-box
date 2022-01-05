from django.shortcuts import render, get_object_or_404
from .models import Users

# Create your views here.

def profiles(request):
    """ Display a user's profile. """
    users = get_object_or_404(Users, pk=user_id)

    context = {
        'users': users
    }

    return render(request, 'profiles.html', context)