from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Room
from .forms import RoomForm
from django.shortcuts import redirect, render
from django.urls import reverse

@login_required
def index(request):
    """
    Root page view. This is essentially a single-page app, if you ignore the
    login and admin parts.
    """
    # Get a list of rooms, ordered alphabetically
    rooms = Room.objects.order_by("title")

    # Render that in the index template
    return render(request, "index.html", {
        'title': 'Chat Rooms',
        "rooms": rooms,
    })

def room_form(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('chat:index'))

    else:
        form = RoomForm()

    context = {
        'title': 'Add a new room',
        'form': form
    }
    return render(request, 'main/generic_form.html', context)
