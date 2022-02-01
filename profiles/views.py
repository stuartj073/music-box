from django.shortcuts import render, get_object_or_404
from .models import Users

from .models import Users
from .forms import UserForm

# Create your views here.

def profile(request):
    """ Display a user's profile. """
    profile = get_object_or_404(Users, user=request.user)

    form = UserForm(insatnce=profile)

    context = {
        'form': form,
    }

    template = 'profiles/profiles.html'

    return render(request, template)