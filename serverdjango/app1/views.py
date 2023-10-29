from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Agency
from .models import Calendar
from .models import CalendarDates
from .models import Routes
from .models import Shapes
from .models import StopTimes
from .models import Stops


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def agency(request, agency_id):
    agency = get_object_or_404(Agency, agency_id=agency_id)
    context = {
        "agency": agency
    }
    return render(request, "app1/agency.html", context)