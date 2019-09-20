from django.db import models
from django.core.files import File
from urllib.request import urlopen
from tempfile import NamedTemporaryFile


class Channel(models.Model):
    id = models.AutoField(primary_key = True)
    tvg_id = models.CharField(max_length=200, editable=True, default='')
    epg_id= models.BigIntegerField(default=9999)
    channel_group = models.CharField(max_length=200)
    channel_name = models.CharField(max_length=200)
    channel_url = models.CharField(max_length=1200)
    channel_logo = models.ImageField(upload_to='channel_logos/', null=True, blank=True)
    channel_logo_url = models.URLField(null=True)
    channel_enabled = models.BooleanField()

class Programmes(models.Model):
    Start = models.CharField(max_length=400)
    Stop = models.CharField(max_length=400)
    Channel = models.CharField(max_length=400)
    Title = models.CharField(max_length=400)
    Description = models.CharField(max_length=99999, null=True)
