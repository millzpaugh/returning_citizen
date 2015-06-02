from django.core.management.base import BaseCommand
from app.management.scraping.get_data import reader_all
from app.models import Provider, Resource, Location

class Command(BaseCommand):

    def handle(self, *args, **options):
        # Location.objects.destroy_all()
        # Provider.objects.destroy_all()
        # Resource.objects.destroy_all()

        all_orgs = reader_all()
        for org in all_orgs:
            for key,value in org.iteritems():
                categories = value['Category']

                resources = []
                for resource in categories:
                    resource = Resource.objects.get_or_create(name=resource)
                    resources.append(resource[0])

                name=key
                description = value.get('Description','No Description Provided.')
                programs = value.get('Program','No Programs Provided.')
                url = value.get('Website', 'No Website Provided.')
                population_served = value.get('Population', 'No Information Provided About Population Served.')
                eligibility = value.get('Eligibility','No Information Provided About Eligiblity.')
                language = value.get('Language','No Information Provided About Language Services.')
                services=value.get('Services', 'No Information about Services Provided'),

                provider = Provider.objects.get_or_create(
                    name=name,
                    description=description,
                    url=url,
                    population_served=population_served,
                    eligibility=eligibility,
                    programs=programs,
                    language_services=language,
                    services=services)

                if provider[1] == True:
                    address=value['Address']
                    phone=value.get('Phone', 'No Phone Number Provided.'),
                    hours=value.get('Hours', 'Hours of Operation Not Provided.'),
                    population=value.get('Population', 'No Information Provided About Language Services.')

                    location = Location(
                        provider=provider[0],
                        address=address,
                        phone=phone,
                        is_headquarters=False,
                        hours_open=hours,
                        population=population
                    )
                    location.save()
                    location.clean_location_data()

                    try:
                        for resource in resources:
                            location.resources_available.add(resource)
                            location.save()
                    except:
                        for resource in resources:
                            location.resources_available.add(resource)

def clean_location_data(location):
    location.phone = location.phone.replace('(u\'', '').replace('\',)','')
    location.hours_open = location.hours_open.replace('(u\'', '').replace('\',)','')
    location.population = location.population.replace('[u\'', '').replace('\']','').replace('\'u','').replace('u\'','').replace('\'','')
    location.save()

def clean_provider_data(provider):
    provider.population_served = provider.population_served.replace('[u\'', '').replace('\']','').replace('\'u','').replace('u\'','').replace('\'','')
    provider.programs = provider.programs.replace('[u\'', '').replace('\']','').replace('\'u','').replace('u\'','').replace('\'','')
    provider.language_services = provider.language_services.replace('[u\'', '').replace('\']','').replace('\'u','').replace('u\'','').replace('\'','')
    provider.services = p.services.replace('([u\'', '').replace('\'],)','').replace('\'u','').replace('u\'','').replace('\'','')
    provider.save()





