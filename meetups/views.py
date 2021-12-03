from django.shortcuts import render
#from django.shortcuts import render

from meetups.forms import RegisterationForm
from .models import Meetups

# Create your views here.


def index(request):
    meetups = Meetups.objects.all()
    return render(request, 'meetups/index.html', {
        'meetups': meetups
    })


def meetup_details(request, meetup_slug):
    try:
        selected_meetup = Meetups.objects.get(slug=meetup_slug)
        registeration_form = RegisterationForm()

        return render(
            request, 'meetups/meetup-details.html', {
            'meetup_found': True,
            'meetup': selected_meetup,
            'form': registeration_form
        })
    except Exception as exc:
        return render(request, 'meetups/meetup-details.html', {
            'meetup_found': False
        })