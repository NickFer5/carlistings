from django import forms
from .models import CarListing

class CarListingForm(forms.ModelForm):
    class Meta:
        model  = CarListing
        fields = ['year', 'make', 'model', 'trim', 'price', 'description']