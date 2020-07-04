# from django.shortcuts import render_to_response
from django.views.generic.edit import FormView
from gunicorn.http.wsgi import Response

from .forms import LookupForm
from .models import Event
from django.utils import timezone
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from django.template import RequestContext


class LookupView(FormView):
    form_class = LookupForm

    def get(self, request):
        return Response('location/lookup.html', RequestContext(request))

    def form_valid(self, form):
        latitude = form.cleaned_data['latitude']
        longitude = form.cleaned_data['longitude']

        now = timezone.now()

        next_week = now + timezone.timedelta(weeks=1)

        location = Point(longitude, latitude, srid=4326)

        events = Event.objects.filter(datetime__gte=now).filter(datetime__lte=next_week).annotate(
            distance=Distance('venue__location', location)).order_by('distance')[0:5]

        return Response('location/lookupresults.html', {
            'events': events
        })
