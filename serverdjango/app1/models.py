from django.db import models


class Agency(models.Model):
    agency_id = models.CharField(max_length=255)
    agency_name = models.CharField(max_length=255)
    agency_url = models.CharField(max_length=255)
    agency_timezone = models.CharField(max_length=255)
    agency_lang = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.agency_id} | {self.agency_name} | {self.agency_url} | {self.agency_timezone} | {self.agency_lang}"


class Calendar(models.Model):
    service_id = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    exception_type = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.service_id} | {self.date} | {self.exception_type}"


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

    def __str__(self):
        return f"{self.service_id} | {self.monday} | {self.tuesday} | {self.wednesday} | {self.thursday} | {self.friday} | {self.saturday} | {self.sunday} | {self.start_date} | {self.end_date}"


class Routes(models.Model):
    route_id = models.CharField(max_length=255)
    agency_id = models.CharField(max_length=255)
    route_short_name = models.CharField(max_length=255)
    route_long_name = models.CharField(max_length=255)
    route_type = models.CharField(max_length=255)
    route_color = models.CharField(max_length=255)
    route_text_color = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.route_id} | {self.agency_id} | {self.route_short_name} | {self.route_long_name} | {self.route_type} | {self.route_color} | {self.route_text_color}"


class Shapes(models.Model):
    shape_id = models.CharField(max_length=255)
    shape_pt_lat = models.CharField(max_length=255)
    shape_pt_lon = models.CharField(max_length=255)
    shape_pt_sequence = models.CharField(max_length=255)
    shape_dist_traveled = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.shape_id} | {self.shape_pt_lat} | {self.shape_pt_lon} | {self.shape_pt_sequence} | {self.shape_dist_traveled}"


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

    def __str__(self):
        return f"{self.trip_id} | {self.arrival_time} | {self.departure_time} | {self.stop_id} | {self.stop_sequence} | {self.stop_headsign} | {self.pickup_type} | {self.drop_off_type} | {self.shape_dist_traveled}"


class Stops(models.Model):
    stop_id = models.CharField(max_length=255)
    stop_name = models.CharField(max_length=255)
    stop_lat = models.CharField(max_length=255)
    stop_lon = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.stop_id} | {self.stop_name} | {self.stop_lat} | {self.stop_lon}"


class Trips(models.Model):
    route_id = models.CharField(max_length=255)
    service_id = models.CharField(max_length=255)
    trip_id = models.CharField(max_length=255)
    shape_id = models.CharField(max_length=255)
    trip_headsign = models.CharField(max_length=255)
    direction_id = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.route_id} | {self.service_id} | {self.trip_id} | {self.shape_id} | {self.trip_headsign} | {self.direction_id}"

