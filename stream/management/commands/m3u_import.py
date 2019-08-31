#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from stream.models import Channel
from urllib.request import urlopen
import re

def insert_link(id,name,logo,group,channel_name, link):
	try:
		print ("[*]Inserting "+channel_name+" in to database[*]")
		c = Channel(tvg_id=id, tvg_name=name, tvg_logo=logo, group_title=group, channel_name=channel_name, channel_url=link, channel_enabled=False)
		c.save()

	except Exception as e:
		raise e

class Command(BaseCommand):
	help = 'Imports m3u files into the DB'
	def handle(self, *args, **options):
		try:
			Channel.objects.all().delete()
			filename = "{URL HERE}"

			with urlopen(filename) as f:
				lines = f.readlines()
				for i in range(0, len(lines)):
					line1 = lines[i].decode("utf-8")
					line2 = lines[i+1].decode("utf-8")
					# process line1 and line2 here
					#strip new lines

					header_pattern = re.compile("^(#EXTM3U)+$")
					if not header_pattern.match(line1):
						print(line1)
						line1r = re.search(r'^#EXTINF:-1 tvg-id="(.*)" tvg-name="(.*)" tvg-logo="(.*)" group-title="(.*)",(.*)$', line1)
						line2r = re.search(r'^(http:\/\/.*)$', line2)

						if line1r:
							id = line1r.group(1)
							name = line1r.group(2)
							logo = line1r.group(3)
							group = line1r.group(4)
							channel_name = line1r.group(5)
							link = line2r.group(1)

							insert_link(id,name,logo,group, channel_name, link)

		except StopIteration:
			print("END")
