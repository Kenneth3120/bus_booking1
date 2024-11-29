from django.db import models

class Bus(models.Model):
    name = models.CharField(max_length=100)
    bus_number = models.CharField(max_length=50)
    from_location = models.CharField(max_length=100)
    to_location = models.CharField(max_length=100)
    journey_time = models.CharField(max_length=50)
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2)
    no_of_seats = models.IntegerField()

    def __str__(self):
        return self.name
