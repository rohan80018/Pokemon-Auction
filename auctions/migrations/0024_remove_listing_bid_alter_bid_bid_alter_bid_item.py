# Generated by Django 4.0.5 on 2022-09-21 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0023_bid_item_alter_listing_bid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='bid',
        ),
        migrations.AlterField(
            model_name='bid',
            name='bid',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='bid',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itemBid', to='auctions.listing'),
        ),
    ]
