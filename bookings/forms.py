from django import forms
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Booking

class BookingForm(forms.ModelForm):
    """A form to create a booking"""

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
          self.fields['email'].initial = user.email
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['date'].required = True

        self.fields['first_name'].label = "First Name"
        self.fields['last_name'].label = "Last Name"
        self.fields['date'].widget = forms.DateInput(attrs={'type': 'date'})

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')
        time = cleaned_data.get('time')

        # Check if a booking with the same date and time already exists
        if (date and time and
                Booking.objects.filter(date=date, time=time).exists()):
            self.add_error('time', 'This date and time is already booked.')

        instance = getattr(self, 'instance', None)
        if instance:
            # Exclude date and time from cleaning if they haven't been changed
            if cleaned_data.get('date') == instance.date:
                cleaned_data.pop('date', None)
            if cleaned_data.get('time') == instance.time:
                cleaned_data.pop('time', None)
        return cleaned_data

    class Meta:
        model = Booking
        fields = [
            'first_name', 'last_name', 'email', 'date', 'time'
        ]