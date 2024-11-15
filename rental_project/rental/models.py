from django.db import models

class CarRental(models.Model):
    car_model = models.CharField(max_length=100)
    renter_name = models.CharField(max_length=100)
    rental_date = models.DateField()
    return_date = models.DateField()
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.car_model} rented by {self.renter_name}"

