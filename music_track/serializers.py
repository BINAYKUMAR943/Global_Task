from rest_framework import serializers

from .models import Track

class TrackListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Track
        fields="__all__"


class ArtistListSerializer(serializers.ModelSerializer):
    total_number_of_tracks = serializers.SerializerMethodField()
    most_recently_played_track=serializers.SerializerMethodField()

    def get_total_number_of_tracks(self,instance):
        return self.Meta.model.objects.filter(artist=instance.artist).count()
       
    
    def get_most_recently_played_track(self,instance):
        first_track= self.Meta.model.objects.filter(artist=instance.artist).order_by('-last_play').first()
        if first_track:
            return TrackListSerializer(instance=first_track).data
        return {}
    class Meta:
        model=Track
        fields=['id','artist','total_number_of_tracks','most_recently_played_track']

    