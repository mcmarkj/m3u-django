# Generated by Django 2.2.5 on 2019-09-21 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0005_auto_20190921_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='tvg_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stream.EPGChannels'),
        ),
    ]
