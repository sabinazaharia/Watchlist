# Generated by Django 4.0.4 on 2022-05-14 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicatie1', '0004_remove_watchlist_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='rating',
            field=models.FloatField(null=True),
        ),
    ]
