# Generated by Django 4.0.5 on 2022-09-12 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auction_imageurl_auction_owner_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Auction',
            new_name='Listing',
        ),
    ]