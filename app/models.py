from django.db import models
from geopy.geocoders import GoogleV3
import datetime

# Create your models here.

#category, services, programs, population

class Resource(models.Model):
    name = models.CharField(max_length = 300)

class Provider(models.Model):
    name = models.CharField(max_length = 200, blank=False)
    description = models.CharField(max_length = 20000, null=True)
    url = models.CharField(max_length = 2000, null=True)
    population_served = models.CharField(max_length = 2000, null=True)
    eligibility = models.CharField(max_length = 2000, null=True)
    programs = models.CharField(max_length = 2000, null=True)
    language_services = models.CharField(max_length = 2000, null=True)
    services = models.CharField(max_length = 2000, null=True)

class Location(models.Model):
    provider = models.ForeignKey(Provider)
    address = models.CharField(max_length=140)
    latitude = models.FloatField(default=0, null=True, blank=True)
    longitude = models.FloatField(default=0, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True)
    is_headquarters = models.BooleanField(default=False)
    hours_open = models.CharField(max_length=200, null=True)
    population = models.CharField(max_length=2000, null=True)
    resources_available = models.ManyToManyField(Resource)

    # Auto-generated timestamps
    created_at = models.DateTimeField(auto_now_add=True, default=datetime.datetime.now())
    updated_at = models.DateTimeField(auto_now=True, default=datetime.datetime.now())

    def __unicode__(self):
        return self.address

    def save(self):
        if self.latitude is None or self.longitude is None or int(self.latitude) == 0 or int(self.longitude) == 0:
            try:
                geolocator = GoogleV3()
                self.address, (self.latitude, self.longitude) = geolocator.geocode(self.address)
            except:
                self.latitude = 0
                self.longitude = 0
        super(Location, self).save()


class ZipcodeCoordinates(models.Model):
    " Storing this so multiple searches to a single zip code only retrieve coordinates once. "

    zipcode = models.CharField(max_length=10)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)

    def save(self):
        if self.latitude == 0 or self.longitude == 0:
            try:
                geolocator = GoogleV3()
                address, (self.latitude, self.longitude) = geolocator.geocode(self.zipcode)
            except:
                pass
        super(ZipcodeCoordinates, self).save()

    def __unicode__(self):
        return '{0} ({1}, {2})'.format(self.zipcode, self.latitude, self.longitude)

class Search(models.Model):

    "One search for resources near a location."

    location = models.CharField(max_length=255)
    resource = models.CharField(max_length=255)

    # Auto-generated timestamps
    created_at = models.DateTimeField(auto_now_add=True, default=datetime.datetime.now())
    updated_at = models.DateTimeField(auto_now=True, default=datetime.datetime.now())

    def __unicode__(self):
        return '{0}: {1} ({2})'.format(self.location, self.resource, self.created_at)

