# Generated by Django 3.2.4 on 2022-05-03 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Park',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parkid', models.CharField(default=None, max_length=10)),
                ('park_name', models.CharField(default=None, max_length=20)),
                ('park_location', models.CharField(default=None, max_length=20)),
                ('slot_type', models.CharField(default=None, max_length=20)),
                ('date', models.DateField()),
                ('slotsNo', models.IntegerField()),
            ],
        ),
    ]
