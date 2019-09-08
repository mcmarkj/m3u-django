from django.contrib import admin

from .models import Channel, Programmes

def enable_channel(modeladmin, request, queryset):
    for channel in queryset:
        ID_EPG = Channel.objects.exclude(epg_id=9999).order_by("-epg_id")[0]
        ID_EPG = ID_EPG.epg_id+1
        Update_ID = channel.id
        Updating_Channel = Channel.objects.all().filter(id=Update_ID)
        Updating_Channel.update(channel_enabled=True, epg_id=ID_EPG)
enable_channel.short_description = "Enable Channel"

def disable_channel(modeladmin, request, queryset):
    queryset.update(channel_enabled=False, epg_id=9999)
disable_channel.short_description = "Disable Channel"

def change_cat_ENTERTAINMENT(modeladmin, request, queryset):
    queryset.update(channel_group='ENTERTAINMENT')
change_cat_ENTERTAINMENT.short_description = "Change Category to Entertainment"

def change_cat_COMEDY(modeladmin, request, queryset):
    queryset.update(channel_group='COMEDY')
change_cat_COMEDY.short_description = "Change Category to Comedy"

def change_cat_DRAMA(modeladmin, request, queryset):
    queryset.update(channel_group='DRAMA')
change_cat_DRAMA.short_description = "Change Category to Drama"

def change_cat_MOVIES(modeladmin, request, queryset):
    queryset.update(channel_group='MOVIES')
change_cat_MOVIES.short_description = "Change Category to Movies"

def change_cat_MUSIC(modeladmin, request, queryset):
    queryset.update(channel_group='MUSIC')
change_cat_MUSIC.short_description = "Change Category to Music"

def change_cat_NEWS(modeladmin, request, queryset):
    queryset.update(channel_group='NEWS')
change_cat_NEWS.short_description = "Change Category to News"

def change_cat_SPORTS(modeladmin, request, queryset):
    queryset.update(channel_group='SPORTS')
change_cat_SPORTS.short_description = "Change Category to Sports"

def change_cat_TRAVEL(modeladmin, request, queryset):
    queryset.update(channel_group='TRAVEL')
change_cat_TRAVEL.short_description = "Change Category to Travel"

class ChannelAdmin(admin.ModelAdmin):
    list_display = ('epg_id', 'channel_name','channel_group','channel_enabled')
    ordering = ('epg_id', 'id')
    actions = [enable_channel, disable_channel,change_cat_ENTERTAINMENT,change_cat_COMEDY,change_cat_DRAMA,change_cat_MOVIES,change_cat_MUSIC,change_cat_NEWS,change_cat_SPORTS,change_cat_TRAVEL]

class ProgrammeAdmin(admin.ModelAdmin):
    list_display = ('Channel', 'Title', 'Start')
    ordering = ('Start',)

admin.site.register(Channel, ChannelAdmin)
admin.site.register(Programmes, ProgrammeAdmin)
