from django.shortcuts import render
from .models import Meetups

# Create your views here.


def index(request):
    meetups = Meetups.objects.all()
    return render(request, 'meetups/index.html', {
        'meetups': meetups
    })


def meetup_details(request, meetup_slug):
    # print(meetup_slug)
    selected_meetup = {
        'title': 'A First Meetup',
        'description': 'This is the first meetup!'
    }

    return render(
        request, 'meetups/meetup-details.html', {
            'meetup_title': selected_meetup['title'],
            'meetup_description': selected_meetup['description']
        })
