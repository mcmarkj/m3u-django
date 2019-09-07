#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from stream.models import Channel
from urllib.request import urlopen
from django.conf import settings
import re
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

def insert_link(num, id,logo,group,channel_name, link):

	if check_exists(id,link) == None:
		try:
			print ("[*]Inserting "+channel_name+" in to database[*]")
			c = Channel(tvg_id=id, epg_id=num, channel_logo_url=logo, channel_group=group, channel_name=channel_name, channel_url=link, channel_enabled=False)
			c.save()
		except Exception as e:
			raise e

def check_exists(id, link):
	try:
		search_channel = Channel.objects.get(tvg_id=id, channel_url=link)
		print ("[*]Channel "+id+" already in database[*]")
	except Channel.DoesNotExist:
		search_channel = None

	return search_channel

class Command(BaseCommand):
	help = 'Imports m3u files into the DB'
	if not settings.M3U_URL:
		print("Update M3U URL in config pls")
	def handle(self, *args, **options):
		try:
			#Channel.objects.all().delete()
			filename = settings.M3U_URL
			ChannelNum = 0

			with urlopen(filename) as f:
				lines = f.readlines()
				for i in range(0, len(lines)):

					print(str(i)+" of "+str(len(lines)))

					if i+1 == len(lines):
						print("Complete! End of m3u file.")
						break

					line1 = lines[i].decode("utf-8")
					line2 = lines[i+1].decode("utf-8")
					# process line1 and line2 here
					#strip new lines

					header_pattern = re.compile("^(#EXTM3U)+$")
					if not header_pattern.match(line1):
						#print(line1)
						line1r = re.search(r'^#EXTINF:-1 tvg-id="(.*)" tvg-name="(.*)" tvg-logo="(.*)" group-title="(UK.*|USA.*)",(.*)$', line1)
						line2r = re.search(r'^(https?:\/\/.*)$', line2)

						if line1r:
							id = line1r.group(1)
							logo = line1r.group(3)
							group = line1r.group(4)
							channel_name = line1r.group(5)
							link = line2r.group(1)
							ChannelNum = ChannelNum+1

							if ChannelNum == 1:
								num = 1
							else:
								num = 9999

							insert_link(num, id,logo,group, channel_name, link)

		except StopIteration:
			print("END")
