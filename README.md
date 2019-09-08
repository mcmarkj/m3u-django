# Django M3U Manager

*Edit M3U IPTV stream files using a django panel.*

### Features

- M3U File Import
- EPG File Import
- Produces a filter EPG that includes only the active / enabled channels
- Generates M3U Playlist and EPG

# How to build
1. Clone git to machine that Django will run on `git clone https://github.com/markconcept/m3u-django.git`
2. Update the local settings file with your M3U & EPG URL, renaming the file when done
`mv local_settings.py.sample local_settings.py`
3. Start th container
`docker-compose up`
4. Run migrations
`docker exec -it m3u-django_web_1 python manage.py migrate`
5. Create a admin user
`docker exec -it m3u-django_web_1 python manage.py createsuperuser`
Input a username, email and password,
6. Import M3U
`docker exec -it m3u-django_web_1 python manage.py m3u_import`

# Configuring to your requirements

The M3U import script will, by default import any channels from the M3U where the group starts with `UK` or `USA`. This can easily be changed to your requirements.

1. In your local settings change the regex
`vi composeexample/local_settings.py`
2. Change the regex to what you want to filter
`#REGEX FILTERS`
`TVG_ID='.*'`
`TVG_NAME='.*'`
`TVG_LOGO='.*'`
`GROUP_TITLE='UK.*|USA.*'`

Suggestions:
`.*` = all, this should be the default
`UK.*` will match `UK - 123 ABC Channel`

3. Save and close.
`ESC + :wq!`

# Enabling Channels

No programms will be imported by the cron until channels are enabled.
Go into the panel; `http://127.0.0.1:8000` login with your super user details.

1. Go to channels
`http://127.0.0.1:8000/stream/channel/`
2. Select the channels you want to enable, using the drop down select `Enable Channel` then `Go`.
3. EPG for enabled channels will be auto-imported by the cronjob, but you can run the cron manually by running:
`docker exec -it m3u-django_web_1 python manage.py epg_import`

# URLs

**Admin Panel**
http://127.0.0.1:8000

**Admin Panel - Channels**
http://127.0.0.1:8000/stream/channel/

**M3U Output File**
http://127.0.0.1:8000/channels/

**EPG Ouput File**
http://127.0.0.1:8000/epg/


###End
