# Generated by Django 4.2.6 on 2023-10-29 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agency_id', models.CharField(max_length=255)),
                ('agency_name', models.CharField(max_length=255)),
                ('agency_url', models.CharField(max_length=255)),
                ('agency_timezone', models.CharField(max_length=255)),
                ('agency_lang', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_id', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=255)),
                ('exception_type', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CalendarDates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_id', models.CharField(max_length=255)),
                ('monday', models.CharField(max_length=255)),
                ('tuesday', models.CharField(max_length=255)),
                ('wednesday', models.CharField(max_length=255)),
                ('thursday', models.CharField(max_length=255)),
                ('friday', models.CharField(max_length=255)),
                ('saturday', models.CharField(max_length=255)),
                ('sunday', models.CharField(max_length=255)),
                ('start_date', models.CharField(max_length=255)),
                ('end_date', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Routes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route_id', models.CharField(max_length=255)),
                ('agency_id', models.CharField(max_length=255)),
                ('route_short_name', models.CharField(max_length=255)),
                ('route_long_name', models.CharField(max_length=255)),
                ('route_type', models.CharField(max_length=255)),
                ('route_color', models.CharField(max_length=255)),
                ('route_text_color', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Shapes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shape_id', models.CharField(max_length=255)),
                ('shape_pt_lat', models.CharField(max_length=255)),
                ('shape_pt_lon', models.CharField(max_length=255)),
                ('shape_pt_sequence', models.CharField(max_length=255)),
                ('shape_dist_traveled', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Stops',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stop_id', models.CharField(max_length=255)),
                ('stop_name', models.CharField(max_length=255)),
                ('stop_lat', models.CharField(max_length=255)),
                ('stop_lon', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='StopTimes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trip_id', models.CharField(max_length=255)),
                ('arrival_time', models.CharField(max_length=255)),
                ('departure_time', models.CharField(max_length=255)),
                ('stop_id', models.CharField(max_length=255)),
                ('stop_sequence', models.CharField(max_length=255)),
                ('stop_headsign', models.CharField(max_length=255)),
                ('pickup_type', models.CharField(max_length=255)),
                ('drop_off_type', models.CharField(max_length=255)),
                ('shape_dist_traveled', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Trips',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route_id', models.CharField(max_length=255)),
                ('service_id', models.CharField(max_length=255)),
                ('trip_id', models.CharField(max_length=255)),
                ('shape_id', models.CharField(max_length=255)),
                ('trip_headsign', models.CharField(max_length=255)),
                ('direction_id', models.CharField(max_length=255)),
            ],
        ),
    ]
