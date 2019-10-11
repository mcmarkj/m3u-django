#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from stream.models import Channel, Programmes
from urllib.request import urlopen
from django.conf import settings
import re
import xmltodict
import bleach


def insert_show(START, STOP, CHANNEL, TITLE, DESC):
    try:
        print ("[*]Inserting "+TITLE+" in to database, channel: "+CHANNEL+"[*]")
        print
        c = Programmes(Start=START, Stop=STOP, Channel=CHANNEL,
                       Title=TITLE, Description=DESC)
        c.save()

    except Exception as e:
        raise e


class Command(BaseCommand):
    help = 'Imports xml epg files into the DB'
    if not settings.XML_URL:
        print("Update xml URL in config pls")

    def handle(self, *args, **options):
        try:

            Programmes.objects.all().delete()
            filename = settings.XML_URL
            file = urlopen(filename)
            data = file.read()
            file.close()
            data = xmltodict.parse(data)
            # print(data)
            programme_array = data['tv']['programme']
            posint = 0

            # print(programme_array[0])
            for programme in programme_array:
                posint = posint+1
                print(str(posint)+" of "+str(len(programme_array)))
                START = programme['@start']
                STOP = programme['@stop']
                CHANNEL = programme['@channel']
                TITLE = bleach.clean(programme['title']['#text'])
                try:
                    DESC = programme['desc']['#text']
                except:
                    DESC = ""
                    continue
                if DESC is None:
                    DESC = TITLE+" on "+CHANNEL
                    DESC = bleach.clean(DESC)
                else:
                    DESC = bleach.clean(DESC)

                if Channel.objects.filter(tvg_id=CHANNEL, channel_enabled=True).exists():
                    insert_show(START, STOP, CHANNEL, TITLE, DESC)
                else:
                    print("Channel "+CHANNEL +
                          " not active station. Enable to load it's shows.")

        except StopIteration:
            print("END")
