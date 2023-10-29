from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from .models import Agency
from .models import Calendar
from .models import CalendarDates
from .models import Routes
from .models import Shapes
from .models import StopTimes
from .models import Stops


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")