from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action,api_view
from rest_framework.response import Response
from .models import Track

from .serializers import  ArtistListSerializer, TrackListSerializer


class TrackViewSet(ModelViewSet):
    serializer_class=TrackListSerializer
    queryset = Track.objects.all()
    filter_fields = ['title']
    


    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    
class ArtistViewSet(ModelViewSet):
    serializer_class=ArtistListSerializer
    queryset = Track.objects.all()
    filter_fields = ['artist']

    
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)




        
        


    


