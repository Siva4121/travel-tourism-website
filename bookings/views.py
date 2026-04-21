from decimal import Decimal

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from flights.models import Flight
from hotels.models import Hotel
from packages.models import Package

from .forms import FlightBookingForm, HotelBookingForm, PackageBookingForm
from .models import Booking


@login_required
def booking_list(request):
    bookings = request.user.bookings.select_related('flight', 'hotel', 'package')
    return render(request, 'bookings/booking_list.html', {'bookings': bookings})


@login_required
def booking_detail(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    return render(request, 'bookings/booking_detail.html', {'booking': booking})


@login_required
def book_flight(request, flight_id):
    flight = get_object_or_404(Flight, pk=flight_id)
    if request.method == 'POST':
        form = FlightBookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.booking_type = 'flight'
            booking.flight = flight
            booking.total_price = flight.price * Decimal(booking.travelers)
            booking.save()
            if flight.seats_available >= booking.travelers:
                flight.seats_available -= booking.travelers
                flight.save(update_fields=['seats_available'])
            messages.success(request, f"Flight {flight.flight_number} booked successfully!")
            return redirect('bookings:detail', pk=booking.pk)
    else:
        form = FlightBookingForm()
    return render(
        request,
        'bookings/book_flight.html',
        {'form': form, 'flight': flight},
    )


@login_required
def book_hotel(request, hotel_id):
    hotel = get_object_or_404(Hotel, pk=hotel_id)
    if request.method == 'POST':
        form = HotelBookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.booking_type = 'hotel'
            booking.hotel = hotel
            nights = 1
            if booking.check_in and booking.check_out:
                nights = max(1, (booking.check_out - booking.check_in).days)
            booking.total_price = hotel.price_per_night * Decimal(nights) * Decimal(booking.travelers)
            booking.save()
            if hotel.rooms_available > 0:
                hotel.rooms_available = max(0, hotel.rooms_available - 1)
                hotel.save(update_fields=['rooms_available'])
            messages.success(request, f"{hotel.name} booked for {nights} night(s)!")
            return redirect('bookings:detail', pk=booking.pk)
    else:
        form = HotelBookingForm()
    return render(
        request,
        'bookings/book_hotel.html',
        {'form': form, 'hotel': hotel},
    )


@login_required
def book_package(request, package_id):
    package = get_object_or_404(Package, pk=package_id)
    if request.method == 'POST':
        form = PackageBookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.booking_type = 'package'
            booking.package = package
            booking.total_price = package.price * Decimal(booking.travelers)
            booking.save()
            if package.slots_available >= booking.travelers:
                package.slots_available -= booking.travelers
                package.save(update_fields=['slots_available'])
            messages.success(request, f"Package '{package.name}' booked successfully!")
            return redirect('bookings:detail', pk=booking.pk)
    else:
        form = PackageBookingForm()
    return render(
        request,
        'bookings/book_package.html',
        {'form': form, 'package': package},
    )


@login_required
def cancel_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk, user=request.user)
    if request.method == 'POST' and booking.status == 'confirmed':
        booking.status = 'cancelled'
        booking.save(update_fields=['status'])
        # Release inventory
        if booking.flight:
            booking.flight.seats_available += booking.travelers
            booking.flight.save(update_fields=['seats_available'])
        if booking.hotel:
            booking.hotel.rooms_available += 1
            booking.hotel.save(update_fields=['rooms_available'])
        if booking.package:
            booking.package.slots_available += booking.travelers
            booking.package.save(update_fields=['slots_available'])
        messages.success(request, "Booking cancelled.")
    return redirect('bookings:list')
