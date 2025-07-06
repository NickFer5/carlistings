from django.shortcuts import render, redirect
from .models import CarListing
from .forms import CarListingForm

def car_list_and_add(request):
    if request.method == 'POST':
        form = CarListingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('car_list_add')  # avoid double submission
    else:
        form = CarListingForm()

    cars = CarListing.objects.all().order_by('-created_at')
    return render(request, 'cars/car_list_add.html', {'cars': cars, 'form': form})

