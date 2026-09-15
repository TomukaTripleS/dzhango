import random
from datetime import date

from django.shortcuts import redirect, render
from django.http import Http404

from .forms import PlaceForm


def home(request):
    places = request.session.get("places", [])
    place = None

    if request.method == "POST" and places:
        ratings = [item["rating"] for item in places]
        place = random.choices(places, weights=ratings)[0]

    return render(request, "places/home.html", {
        "place": place,
        "places": places,
    })


def place_list(request):
    places = request.session.get("places", [])
    return render(request, "places/place_list.html", {"places": places})


def add_place(request):
    if request.method == "POST":
        form = PlaceForm(request.POST)
        if form.is_valid():
            places = request.session.get("places", [])
            place = form.cleaned_data.copy()
            place["id"] = len(places) + 1
            place["created_at"] = date.today().strftime("%d.%m.%Y")
            places.append(place)
            request.session["places"] = places
            return redirect("/places/")
    else:
        form = PlaceForm()
    return render(request, "places/add_place.html", {"form": form})


def place_detail(request, id):
    places = request.session.get("places", [])
    for place in places:
        if place["id"] == id:
            return render(
                request, "places/place_detail.html", {"place": place}
            )
    raise Http404("Місце не знайдено")
