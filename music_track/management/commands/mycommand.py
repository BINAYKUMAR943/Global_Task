import json
from django.core.management.base import BaseCommand
from music_track.models import Track

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('json_data', type=str)

    def handle(self, *args, **options):
        with open(options['json_data']) as f:
            data_list = json.load(f)

        for data in data_list:
            data['id'] = data.pop('id')
            Track.objects.get_or_create(pk=data['id'], defaults=data)