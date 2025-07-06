from django.db import models

class CarListing(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    trim = models.CharField(max_length=50, blank=True, null=True)
    mileage = models.PositiveIntegerField(blank=True, null=True)
    color = models.CharField(max_length=30, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.year} {self.make} {self.model} {self.trim or ''}".strip()
