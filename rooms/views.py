from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django_countries import countries
from . import models


class HomeView(ListView):

    """ HomeView Definitino """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"


class RoomDetail(DetailView):

    model = models.Room


def search(request):
    city = request.GET.get("city", "Anywhere")
    city = str.capitalize(city)
    return render(request, "rooms/search.html", {"city": city, "countries": countries})
