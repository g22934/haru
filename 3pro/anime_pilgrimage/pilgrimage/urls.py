from django.urls import path
from . import views

urlpatterns = [
    #path('title/<int:title_id>/', views.display_pilgrimage_info, name='display_pilgrimage_info'),
    path('<int:title_id>/', views.display_pilgrimage_info, name='display_pilgrimage_info'),
    path('map/', views.map_view, name='map'),
    #path('api/pilgrimage_locations/', views.PilgrimageLocationList.as_view(), name='pilgrimage-location-list'),
    #path('api/pilgrimage_locations/', views.pilgrimage_locations, name='pilgrimage-location-list'),
    path('api/pilgrimage_locations/', views.pilgrimage_locations, name='pilgrimage_locations'),
    path('api/location/<int:location_id>/', views.get_location_details, name='get_location_details'),
    path('find_nearby_locations/', views.find_nearby_locations, name='find_nearby_locations'),
    path('map/', views.map_view, name='map_view'),
    path('filter_locations/', views.filter_locations, name='filter_locations'),
    
    

]

