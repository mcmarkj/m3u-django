from django.shortcuts import render
from django.http import HttpResponse
from .models import Channel

##EXTM3U
#EXTINF:-1 tvg-id="BBC1London.uk" tvg-name="UK: BBC ONE HD" tvg-logo="http://cyber-files.co.uk/andy-apps/picon/bbconehd.png" group-title="UK | Entertainment",UK: BBC ONE HD
#http://gateways.ml:80/itshotilikeit@gmail.com/YPtr57GiPe/52

HEADER = "#EXTM3U"
LINE_START = "#EXTINF:-1"
LINE_BREAK = "\n"


def index(request):
    channel_list = Channel.objects.all().filter(channel_enabled=True).order_by("epg_id")

    if channel_list:
        # Set the header for the m3u
        output = [HEADER]

        #Loop through the returned channels and output them
        for channel in channel_list:
            #Formatting for each line
            line = ' tvg-id="{tvg_id}" epg-id="{epg_id}" tvg-name="{tvg_name}" tvg-logo="{tvg_logo}" group-title="{group_title}",{channel_name}'.format(tvg_id=channel.tvg_id, tvg_name=channel.tvg_name, tvg_logo=channel.tvg_logo, epg_id=channel.epg_id, group_title=channel.group_title, channel_name=channel.channel_name)
            url = channel.channel_url
            #Construct the string
            output.append(LINE_START+line+LINE_BREAK+url)


    else:
        #Default output if the array is returned null.
        output = "Error: No Enabled Channels Found."


    return_output = LINE_BREAK.join(output)

    return HttpResponse(return_output)
