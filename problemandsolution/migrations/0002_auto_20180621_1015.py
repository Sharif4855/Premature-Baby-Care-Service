# Generated by Django 2.0.5 on 2018-06-21 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problemandsolution', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problemandsolution',
            name='youtubeurl',
            field=models.URLField(blank=True),
        ),
    ]
