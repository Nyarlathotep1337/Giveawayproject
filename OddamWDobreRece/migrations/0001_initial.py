# Generated by Django 4.1.3 on 2022-12-01 17:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('type', models.CharField(blank=True, choices=[('fundacja', 'fundacja'), ('organizacja pozarzádowa', 'organizacja pozarzádowa'), ('zbiórka lokalna', 'zbiórka lokalna')], default='fundacja', help_text='What type of organization?', max_length=40, null=True)),
                ('categories', models.ManyToManyField(to='OddamWDobreRece.category')),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('address', models.CharField(max_length=40)),
                ('phone_number', models.IntegerField()),
                ('city', models.CharField(max_length=40)),
                ('zip_code', models.CharField(max_length=6)),
                ('pick_up_date', models.TimeField()),
                ('pick_up_time', models.DateTimeField()),
                ('pick_up_comment', models.TextField()),
                ('categories', models.ManyToManyField(to='OddamWDobreRece.category')),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='OddamWDobreRece.institution')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
