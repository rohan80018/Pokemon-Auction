# Generated by Django 4.0.5 on 2022-09-18 12:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_alter_listing_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='watchlist',
            field=models.ManyToManyField(blank=True, null=True, related_name='watch_list', to=settings.AUTH_USER_MODEL),
        ),
    ]