from django.shortcuts import render
from .models import Flight ,Passenger
from django.http import HttpResponseRedirect
# lets me use the name of a path, and it finds the actual path
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
        })

def flight(request, flight_id):
    flight = Flight.objects.get(pk=flight_id)
    return render(request, "flights/flight.html",{
        # which flight is rendered
        "flight":flight,
        # who are the passengers
        "passengers":flight.passengers.all(),
        # who is not on the flight
        "non_passengers": Passenger.objects.exclude(flights=flight).all()
    })

def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        # determines the name for the input field
        passenger = Passenger.objects.get(pk = int(request.POST["passenger"]))
        # adds new row to the table, implementation details hidden
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flight", args=(flight.id,)))