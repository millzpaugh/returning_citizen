from django.core.management.base import BaseCommand
from app.management.scraping.get_data import reader_all
from app.models import Provider, Resource, Location

def clean_location_data(location):
    location.phone = location.phone.replace('(u\'', '').replace('\',)','')
    location.hours_open = location.hours_open.replace('(u\'', '').replace('\',)','')
    location.population = location.population.replace('[u\'', '').replace('\']','').replace('\'u','').replace('u\'','').replace('\'','')
    location.save()

def clean_provider_data(provider):
    provider.population_served = provider.population_served.replace('[u\'', '').replace('\']','').replace('\'u','').replace('u\'','').replace('\'','')
    provider.programs = provider.programs.replace('[u\'', '').replace('\']','').replace('\'u','').replace('u\'','').replace('\'','')
    provider.language_services = provider.language_services.replace('[u\'', '').replace('\']','').replace('\'u','').replace('u\'','').replace('\'','')
    provider.services = provider.services.replace('([u\'', '').replace('\'],)','').replace('\'u','').replace('u\'','').replace('\'','')
    provider.save()

class Command(BaseCommand):

    def handle(self, *args, **options):

        providers = Provider.objects.all()
        for p in providers:
            clean_provider_data(p)

            if Location.objects.filter(provider=p).exists():
                location = Location.objects.filter(provider=p)[0]
                clean_location_data(location)




