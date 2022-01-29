from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from events.filters import EventFilter

from .models import Event
from .serializers import EventSerializer


class EventsList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = EventFilter
