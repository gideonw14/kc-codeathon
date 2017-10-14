from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Room

@login_required
def index(request):
    rooms = Room.objects.order_by("title")
    context = {
        'title': 'Chat Rooms',
        'rooms': rooms,
    }
    return render(request, "index.html", context)
