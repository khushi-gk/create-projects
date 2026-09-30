from django.shortcuts import render, redirect
from .models import Room, Booking
from .forms import BookingForm, RoomForm


def room_list(request):
    rooms = Room.objects.all()

    check_in = request.GET.get('check_in')
    check_out = request.GET.get('check_out')

    if check_in and check_out:
        bookings = Booking.objects.filter(
            check_in__lt=check_out,
            check_out__gt=check_in
        )

        booked_room_ids = bookings.values_list('room_id', flat=True)

        rooms = rooms.exclude(id__in=booked_room_ids)

    return render(
        request,
        'rooms/room_list.html',
        {
            'rooms': rooms,
            'check_in': check_in,
            'check_out': check_out
        }
    )

def dashboard(request):

    total_rooms = Room.objects.count()

    available_rooms = Room.objects.filter(
        is_available=True
    ).count()

    total_bookings = Booking.objects.count()

    total_guests = Booking.objects.values(
        'guest_name'
    ).distinct().count()

    return render(
        request,
        'rooms/dashboard.html',
        {
            'total_rooms': total_rooms,
            'available_rooms': available_rooms,
            'total_bookings': total_bookings,
            'total_guests': total_guests,
        }
    )
    
def booking_list(request):
    bookings = Booking.objects.all()

    return render(
        request,
        'rooms/booking_list.html',
        {'bookings': bookings}
    )

def guest_list(request):

    search = request.GET.get('search')

    bookings = Booking.objects.all()

    if search:
        bookings = bookings.filter(
            guest_name__icontains=search
        )

    return render(
        request,
        'rooms/guests.html',
        {
            'bookings': bookings,
            'search': search
        }
    )

def add_room(request):

    if request.method == 'POST':

        form = RoomForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('room_list')

    else:
        form = RoomForm()

    return render(
        request,
        'rooms/room_form.html',
        {'form': form}
    )   

def edit_room(request, room_id):

    room = Room.objects.get(id=room_id)

    if request.method == 'POST':

        form = RoomForm(request.POST, instance=room)

        if form.is_valid():
            form.save()
            return redirect('room_list')

    else:
        form = RoomForm(instance=room)

    return render(
        request,
        'rooms/room_form.html',
        {'form': form}
    )     

def delete_room(request, room_id):

    room = Room.objects.get(id=room_id)

    if request.method == 'POST':
        room.delete()
        return redirect('room_list')

    return render(
        request,
        'rooms/delete_room.html',
        {'room': room}
    )

def add_booking(request):

    if request.method == 'POST':

        form = BookingForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('booking_list')

    else:

        room_id = request.GET.get('room')
        check_in = request.GET.get('check_in')
        check_out = request.GET.get('check_out')

        form = BookingForm(
            initial={
                'room': room_id,
                'check_in': check_in,
                'check_out': check_out
            }
        )

    return render(
        request,
        'rooms/booking_form.html',
        {'form': form}
    )

def edit_booking(request, booking_id):

    booking = Booking.objects.get(id=booking_id)

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)

        if form.is_valid():
            form.save()
            return redirect('booking_list')

    else:
        form = BookingForm(instance=booking)

    return render(
        request,
        'rooms/booking_form.html',
        {'form': form}
    ) 

def delete_booking(request, booking_id):

    booking = Booking.objects.get(id=booking_id)

    if request.method == 'POST':
        booking.delete()
        return redirect('booking_list')

    return render(
        request,
        'rooms/delete_booking.html',
        {'booking': booking}
    )       