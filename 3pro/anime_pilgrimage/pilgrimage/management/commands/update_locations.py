import requests
from django.core.management.base import BaseCommand
from pilgrimage.models import PilgrimageLocation

def get_lat_lng_from_address(address):
    api_key = 'AIzaSyDbVBPDaX1wpt14MoKrWlvxIOoL6K0oRU0'  # ここにAPIキーを入力
    url = f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}'
    response = requests.get(url)
    data = response.json()
    if data['status'] == 'OK':
        location = data['results'][0]['geometry']['location']
        return location['lat'], location['lng']
    else:
        return None, None

class Command(BaseCommand):
    help = 'Update locations with latitude and longitude'

    def handle(self, *args, **kwargs):
        locations = PilgrimageLocation.objects.all()
        for location in locations:
            if location.latitude is None or location.longitude is None:
                lat, lng = get_lat_lng_from_address(location.address)
                if lat is not None and lng is not None:
                    location.latitude = lat
                    location.longitude = lng
                    location.save()
                    self.stdout.write(self.style.SUCCESS(f"Updated {location.name}: {lat}, {lng}"))
                else:
                    self.stdout.write(self.style.WARNING(f"Could not retrieve coordinates for {location.name}"))
