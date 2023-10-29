from django.db import models


class Agency(models.Model):
    agency_id = models.CharField(max_length=255)
    agency_name = models.CharField(max_length=255)
    agency_url = models.CharField(max_length=255)
    agency_timezone = models.CharField(max_length=255)
    agency_lang = models.CharField(max_length=255)


class Calendar(models.Model):
    service_id = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    exception_type = models.CharField(max_length=255)


class CalendarDates(models.Model):
    service_id = models.CharField(max_length=255)
    monday = models.CharField(max_length=255)
    tuesday = models.CharField(max_length=255)
    wednesday = models.CharField(max_length=255)
    thursday = models.CharField(max_length=255)
    friday = models.CharField(max_length=255)
    saturday = models.CharField(max_length=255)
    sunday = models.CharField(max_length=255)
    start_date = models.CharField(max_length=255)
    end_date = models.CharField(max_length=255)


class Routes(models.Model):
    route_id = models.CharField(max_length=255)
    agency_id = models.CharField(max_length=255)
    route_short_name = models.CharField(max_length=255)
    route_long_name = models.CharField(max_length=255)
    route_type = models.CharField(max_length=255)
    route_color = models.CharField(max_length=255)
    route_text_color = models.CharField(max_length=255)


class Shapes(models.Model):
    shape_id = models.CharField(max_length=255)
    shape_pt_lat = models.CharField(max_length=255)
    shape_pt_lon = models.CharField(max_length=255)
    shape_pt_sequence = models.CharField(max_length=255)
    shape_dist_traveled = models.CharField(max_length=255)


class StopTimes(models.Model):
    trip_id = models.CharField(max_length=255)
    arrival_time = models.CharField(max_length=255)
    departure_time = models.CharField(max_length=255)
    stop_id = models.CharField(max_length=255)
    stop_sequence = models.CharField(max_length=255)
    stop_headsign = models.CharField(max_length=255)
    pickup_type = models.CharField(max_length=255)
    drop_off_type = models.CharField(max_length=255)
    shape_dist_traveled = models.CharField(max_length=255)


class Stops(models.Model):
    stop_id = models.CharField(max_length=255)
    stop_name = models.CharField(max_length=255)
    stop_lat = models.CharField(max_length=255)
    stop_lon = models.CharField(max_length=255)


class Trips(models.Model):
    route_id = models.CharField(max_length=255)
    service_id = models.CharField(max_length=255)
    trip_id = models.CharField(max_length=255)
    shape_id = models.CharField(max_length=255)
    trip_headsign = models.CharField(max_length=255)
    direction_id = models.CharField(max_length=255)

