from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from app.models import ZipcodeCoordinates, Resource, Location, Search
from geopy.distance import vincenty
from geopy.geocoders import GoogleV3
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest

# Create your views here.

RADIUS_DISTANCE = 35 # miles

def index(request):
    return render_to_response('index.html', {
    }, RequestContext(request))

def about(request):
    return render_to_response('about.html', {
    }, RequestContext(request))

def find_search_coordinates(searched_location):
    #helper function, not meant to be connected in urls.py
    #putting the geocoding of search addresses into a separate method to stay DRY
    #takes the address searched for, returns coordinates

    coords = False

    try:
        searched_location = int(searched_location[:5])

        # Zero-pad New England zipcodes
        if len(str(searched_location)) == 4:
            searched_location = '0{0}'.format(searched_location)
    except:
        try:
            geolocator = GoogleV3()
            address, (latitude, longitude) = geolocator.geocode(searched_location)
        except:
            pass
        else:
            coords = {
                'latitude': latitude,
                'longitude': longitude,
            }
    else:
        try:
            zipcode_coords = ZipcodeCoordinates.objects.get(zipcode=searched_location)
        except:
            # If this zipcode has not yet been searched, create a new one
            zipcode_coords = ZipcodeCoordinates(zipcode=searched_location)
            zipcode_coords.save()
        finally:
            coords = {
                'latitude': zipcode_coords.latitude,
                'longitude': zipcode_coords.longitude
            }

    return coords

def resources(request, **kwargs):
    searched_location = request.POST.get('location')
    resource = request.POST.getlist('resource')
    type_ = request.POST.get('type')
    radius = request.POST.get('radius')
    if not type_:
        type_ = request.GET.get('type')

    if not type_:
        type_ = kwargs.get('type')

    try:
        radius = int(radius)
        assert 10 < radius < 150
    except:
        radius = RADIUS_DISTANCE

    if not searched_location and not resource: # neither
        return render(request, 'resources.html', { 'type': type_ })
    elif searched_location and resource: # both
        # Save the search
        search = Search(**{
                'location': searched_location,
                'resource': resource
            })
        search.save()

        coords = find_search_coordinates(searched_location)
    elif not searched_location:
        coords = False

    if not coords:
        cdnt_find_loc_error_msg = _("Sorry, I couldn't find that location. Please try again. You can also search by city or by zipcode.")
        messages.error(request, cdnt_find_loc_error_msg)
        if type_:
            return HttpResponseRedirect(reverse('resources', kwargs={'type': type_}))
        else:
            return HttpResponseRedirect(reverse('resources'))

    try:
        if len(resource) == 1:
            resource = [Resource.objects.get(name=resource[0])]
        elif len(resource) > 1:
            resource = Resource.objects.filter(name__in=[res for res in resource])
        else:
            raise ValueError
    except:
        cdnt_find_res_error_msg = _("Please choose a resource and try again.")
        messages.error(request, cdnt_find_res_error_msg)
        if type_:
            return HttpResponseRedirect(reverse('resources', kwargs={'type': type_}))
        else:
            return HttpResponseRedirect(reverse('resources'))
    else:
        locations = Location.objects.select_related('provider')

        if len(resource) == 1: # Just one resource chosen
            locations = locations.filter(resources_available=resource[0])
        elif len(resource) > 1:
            locations = locations.filter(resources_available__in=resource)

        preferred_orgs = False
        within_radius = []
        for location in locations:
            dist = vincenty(
                (location.latitude, location.longitude),
                (coords['latitude'], coords['longitude'])
            ).miles
            if dist <= radius:
                within_radius.append((location,round(dist,1)))

        #passing a sorted list of tuples with (orgname, distance)


    context = {
        'within_radius': within_radius,
        'radius':radius,
        'location': searched_location,
        'resource': resource,
        'search_from': coords,
        'type': type_
    }

    return render(request, 'resources.html', dictionary=context)