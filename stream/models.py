from django.db import models

STATUS_CHOICES = [
    ('d', 'Draft'),
    ('p', 'Published'),
    ('w', 'Withdrawn'),
]

class Channel(models.Model):
    tvg_id = models.CharField(max_length=200)
    epg_id= models.BigIntegerField(default=9999)
    tvg_name = models.CharField(max_length=200)
    tvg_logo = models.CharField(max_length=800)
    group_title = models.CharField(max_length=200)
    channel_name = models.CharField(max_length=200)
    channel_url = models.CharField(max_length=1200)
    channel_enabled = models.BooleanField()


class EPGChannels(models.Model):
    channel_id = models.CharField(max_length=1200)
    display_name = models.CharField(max_length=1200)
    icon_src = models.CharField(max_length=1200)
    lcn = models.CharField(max_length=1200)

class Programmes(models.Model):
    Start = models.DateTimeField()
    Stop = models.DateTimeField()
    Channel = models.CharField(max_length=200)
    Title = models.CharField(max_length=400)
    Description = models.CharField(max_length=99999)
