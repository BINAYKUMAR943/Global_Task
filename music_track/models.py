from django.db import models
from datetime import datetime    


class Track(models.Model):
    title=models.CharField(max_length=2048)
    artist=models.CharField(max_length=2048)
    duration=models.DecimalField(decimal_places=2,max_digits=5)
    last_play=models.DateTimeField(default=datetime.now)