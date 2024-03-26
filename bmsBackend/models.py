from django.db import models

class Station(models.Model):
    station_name = models.CharField(max_length=100)
    onboard_frequency = models.IntegerField()
    offboard_frequency = models.IntegerField()


class Passengers(models.Model):
    station_name = models.CharField(max_length=100)
    onboard_frequency = models.IntegerField()
    offboard_frequency = models.IntegerField()


class Journey(models.Model):
    start_station = models.CharField(max_length=100)
    end_station = models.CharField(max_length=100)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True)
    available_seats = models.IntegerField()
    total_passengers = models.IntegerField()    
    total_duration = models.CharField(max_length=100,default="Journey Ongoing!")


class Meta:
        app_label = 'bmsBackend'

# test