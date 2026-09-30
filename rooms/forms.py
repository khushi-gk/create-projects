from django import forms
from .models import Room, Booking


class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ['guest_name', 'room', 'check_in', 'check_out']

        widgets = {
            'check_in': forms.DateInput(attrs={'type': 'date'}),
            'check_out': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned_data = super().clean()

        room = cleaned_data.get('room')
        check_in = cleaned_data.get('check_in')
        check_out = cleaned_data.get('check_out')

        if room and check_in and check_out:

            if check_out <= check_in:
                raise forms.ValidationError(
                    "Check-out date must be after check-in date."
                )

            overlapping_bookings = Booking.objects.filter(
                room=room,
                check_in__lt=check_out,
                check_out__gt=check_in
            )

            if overlapping_bookings.exists():
                raise forms.ValidationError(
                    f"Room {room.room_number} is already booked for these dates."
                )

        return cleaned_data


class RoomForm(forms.ModelForm):

    class Meta:
        model = Room
        fields = ['room_number', 'room_type', 'price', 'is_available']