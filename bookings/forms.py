from django import forms

from .models import Booking


class FlightBookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('travelers', 'travel_date', 'notes')
        widgets = {
            'travel_date': forms.DateInput(attrs={'type': 'date'}),
        }


class HotelBookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('travelers', 'check_in', 'check_out', 'notes')
        widgets = {
            'check_in': forms.DateInput(attrs={'type': 'date'}),
            'check_out': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean(self):
        cleaned = super().clean()
        ci = cleaned.get('check_in')
        co = cleaned.get('check_out')
        if ci and co and co <= ci:
            raise forms.ValidationError("Check-out must be after check-in.")
        return cleaned


class PackageBookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('travelers', 'travel_date', 'notes')
        widgets = {
            'travel_date': forms.DateInput(attrs={'type': 'date'}),
        }
