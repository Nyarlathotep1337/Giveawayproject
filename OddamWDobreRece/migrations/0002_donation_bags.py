# Generated by Django 4.1.3 on 2022-12-07 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OddamWDobreRece', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='bags',
            field=models.IntegerField(default=0),
        ),
    ]
