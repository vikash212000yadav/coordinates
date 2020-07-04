from django.contrib.gis.db import models


class Venue(models.Model):
    name = models.CharField(max_length=256)
    location = models.PointField()

    def __str__(self):
        return self.name


class Event(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    datetime = models.DateTimeField()

    def __str__(self):
        return "%s - %s" % (self.name, self.venue.name)
