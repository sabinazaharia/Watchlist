# Generated by Django 4.0.4 on 2022-05-14 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicatie2', '0003_alter_movies_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='added',
            field=models.BooleanField(default=0),
        ),
    ]
