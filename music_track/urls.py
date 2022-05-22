from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import ArtistViewSet, TrackViewSet
urlpatterns = [
    path("tracks/", TrackViewSet.as_view({
        'get':'list',
        'post':'create'
    }),name='track_create_list_view'),
    path("tracks/<int:pk>/", TrackViewSet.as_view({
        'get':'retrieve',
        'patch':'partial_update'
    }),name='track_retrieve_update_view'),
     path("artists/", ArtistViewSet.as_view({
        'get':'list',
    }),name='artist_list_view'),
    
    
]