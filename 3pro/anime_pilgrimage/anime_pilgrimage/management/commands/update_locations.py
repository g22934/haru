import requests
from django.core.management.base import BaseCommand
from pilgrimage.models import PilgrimageLocation

class Command(BaseCommand):
    help = 'Updates pilgrimage locations with latitude and longitude'

    def get_lat_lng_from_address(self, address):
        api_key = 'AIzaSyDbVBPDaX1wpt14MoKrWlvxIOoL6K0oRU0'
        url = f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}'
        response = requests.get(url)
        data = response.json()
        if data['status'] == 'OK':
            location = data['results'][0]['geometry']['location']
            return location['lat'], location['lng']
        else:
            return None, None

    def handle(self, *args, **kwargs):
        locations = PilgrimageLocation.objects.all()
        for location in locations:
            if location.latitude is None or location.longitude is None:
                lat, lng = self.get_lat_lng_from_address(location.address)
                if lat and lng:
                    location.latitude = lat
                    location.longitude = lng
                    location.save()
                    self.stdout.write(self.style.SUCCESS(f"Updated {location.name}: {lat}, {lng}"))
