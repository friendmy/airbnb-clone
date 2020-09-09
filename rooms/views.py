from django.shortcuts import render
from . import models


def all_rooms(request):
    all_rooms = models.Room.objects.all()[:10]
    return render(request, "rooms/home.html", context={"rooms": all_rooms})
