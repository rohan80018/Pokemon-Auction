# Generated by Django 4.0.5 on 2022-09-20 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0016_alter_listing_watchlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name='Bid',
        ),
    ]