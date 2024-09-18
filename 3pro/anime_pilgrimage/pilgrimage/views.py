from django.shortcuts import render, get_object_or_404
from .models import Title, PilgrimageLocation

def display_pilgrimage_info(request, title_id):
    title = get_object_or_404(Title, id=title_id)
    locations = PilgrimageLocation.objects.filter(title=title)
    return render(request, 'pilgrimage/detail.html', {'title': title, 'locations': locations})

from django.shortcuts import render
from .models import PilgrimageLocation
import json

def map_view(request):
    # データベースから聖地のデータを取得
    locations = PilgrimageLocation.objects.all()
    # JSON形式に変換
    locations_data = list(locations.values('name', 'latitude', 'longitude'))
    # テンプレートにデータを渡す
    context = {
        'locations_json': json.dumps(locations_data)
    }
    return render(request, 'pilgrimage/map.html', context)

# views.py
from django.http import JsonResponse
from .models import PilgrimageLocation

from rest_framework import generics
from .models import PilgrimageLocation

# views.py 内の関数やクラスの中でインポートする
class PilgrimageLocationList(generics.ListCreateAPIView):
    def get_serializer_class(self):
        from .serializers import PilgrimageLocationSerializer  # 関数内でインポート
        return PilgrimageLocationSerializer
    
    queryset = PilgrimageLocation.objects.all()

from django.http import JsonResponse
from .models import PilgrimageLocation

def pilgrimage_locations(request):
    locations = list(PilgrimageLocation.objects.values('id', 'name', 'latitude', 'longitude'))
    return JsonResponse(locations, safe=False)



# views.py
from django.http import JsonResponse
import requests

def get_lat_lng_view(request):
    address = request.GET.get('address', '')
    api_key = 'AIzaSyDbVBPDaX1wpt14MoKrWlvxIOoL6K0oRU0'
    url = f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}'
    response = requests.get(url)
    data = response.json()
    if data['status'] == 'OK':
        location = data['results'][0]['geometry']['location']
        lat, lng = location['lat'], location['lng']
        return JsonResponse({'latitude': lat, 'longitude': lng})
    else:
        return JsonResponse({'error': 'Error fetching location data'})

import requests
from pilgrimage.models import PilgrimageLocation



def get_lat_lng_from_address(address):
    api_key = 'AIzaSyDbVBPDaX1wpt14MoKrWlvxIOoL6K0oRU0'
    url = f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}'
    response = requests.get(url)
    print(f"Request URL: {url}")
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Content: {response.text}")
    
    data = response.json()
    if data['status'] == 'OK':
        location = data['results'][0]['geometry']['location']
        return location['lat'], location['lng']
    else:
        print(f"Error: {data['error_message']}")
        return None, None

def update_locations():
    print("update_locations function started")
    locations = PilgrimageLocation.objects.all()
    for location in locations:
        print(f"Processing location: {location.name}")
        if location.latitude is None or location.longitude is None:
            lat, lng = get_lat_lng_from_address(location.address)
            if lat and lng:
                location.latitude = lat
                location.longitude = lng
                location.save()
                print(f"Updated {location.name}: {lat}, {lng}")
            else:
                print(f"Failed to update {location.name}")

update_locations()






def update_locations():
    print("update_locations function started")
    locations = PilgrimageLocation.objects.all()
    for location in locations:
        try:
            print(f"Processing location: {location.name}")
            if location.latitude is None or location.longitude is None:
                lat, lng = get_lat_lng_from_address(location.address)
                if lat and lng:
                    location.latitude = lat
                    location.longitude = lng
                    location.save()
                    print(f"Updated {location.name}: {lat}, {lng}")
                else:
                    print(f"Failed to update {location.name}: {location.address}")
        except Exception as e:
            print(f"An error occurred: {e}")

update_locations()


from django.http import JsonResponse
from .models import PilgrimageLocation, Title

def get_location_details(request, location_id):
    try:
        location = PilgrimageLocation.objects.get(id=location_id)
        title = location.title
        data = {
            'name': location.name,
            'address': location.address,
            'latitude': location.latitude,
            'longitude': location.longitude,
            'title_name': title.name,
            'title_description': title.description,
            'title_image': title.image.url if title.image else None,
            'location_image': location.image.url if location.image else None,
        }
        return JsonResponse(data)
    except PilgrimageLocation.DoesNotExist:
        return JsonResponse({'error': 'Location not found'}, status=404)

from django.http import JsonResponse
from .models import PilgrimageLocation

def location_details(request, id):
    try:
        location = PilgrimageLocation.objects.get(id=id)
        data = {
            'name': location.name,
            'title_name': location.title.name,
            'title_description': location.title.description,
            'title_image': location.title.image.url,
            'location_image': location.image.url
        }
        return JsonResponse(data)
    except PilgrimageLocation.DoesNotExist:
        return JsonResponse({'error': 'Location not found'}, status=404)

#指定の距離から◯◯KMの聖地検出システム
from django.shortcuts import render
from django.http import JsonResponse
from .models import PilgrimageLocation
import math

def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # 地球の半径 (km)
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return distance

from django.shortcuts import render
from django.http import HttpResponseBadRequest
from .models import PilgrimageLocation
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D

# views.py
from django.http import JsonResponse
from .models import PilgrimageLocation
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D

# views.py
from django.http import JsonResponse
from .models import PilgrimageLocation
from django.contrib.gis.measure import D
from geopy.distance import geodesic

from django.http import JsonResponse
from django.shortcuts import render
from geopy.distance import geodesic
from .models import PilgrimageLocation

def find_nearby_locations(request):
    # 始点を東京駅に設定
    tokyo_station_coords = (35.6812, 139.7671)
    
    try:
        latitude = float(request.GET.get('latitude', tokyo_station_coords[0]))
        longitude = float(request.GET.get('longitude', tokyo_station_coords[1]))
        radius = float(request.GET.get('radius', 10))  # 半径（キロメートル）

        # 半径内の聖地を取得
        nearby_locations = []
        locations = PilgrimageLocation.objects.all()
        for location in locations:
            location_coords = (location.latitude, location.longitude)
            distance = geodesic(tokyo_station_coords, location_coords).kilometers
            if distance <= radius:
                nearby_locations.append({
                    'name': location.name,
                    'address': location.address,
                    'latitude': location.latitude,
                    'longitude': location.longitude,
                    'distance': distance
                })
        
        return JsonResponse({'locations': nearby_locations})

    except ValueError:
        return JsonResponse({'error': 'Invalid input'}, status=400)


def find_nearby_locations_form(request):
    return render(request, 'myapp/find_nearby_locations.html')



def map_view(request):
    locations = PilgrimageLocation.objects.all()
    return render(request, 'pilgrimage/map_view.html', {'locations': locations})
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import PilgrimageLocation
import json
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import PilgrimageLocation
from django.core.exceptions import ValidationError

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
from .models import PilgrimageLocation
def filter_locations(request):
    if request.method == 'POST':
        import json
        try:
            data = json.loads(request.body)
            center_address = data.get('centerAddress')
            radius = float(data.get('radius'))

            geolocator = Nominatim(user_agent="geoapiExercises")
            location = geolocator.geocode(center_address)

            if not location:
                return JsonResponse({"error": "住所が見つかりません"}, status=400)

            center_coordinates = (location.latitude, location.longitude)

            # データベースから聖地情報を取得し、半径内の聖地をフィルタリング
            filtered_locations = []
            for loc in PilgrimageLocation.objects.all():
                loc_coordinates = (loc.latitude, loc.longitude)
                distance = geodesic(center_coordinates, loc_coordinates).km
                if distance <= radius:
                    filtered_locations.append({
                        "name": loc.name,
                        "address": loc.address,
                        "latitude": loc.latitude,
                        "longitude": loc.longitude
                    })

            return JsonResponse({
                "center": {"lat": location.latitude, "lng": location.longitude},
                "locations": filtered_locations
            })
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "POSTメソッドでリクエストしてください"}, status=400)

