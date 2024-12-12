from django.shortcuts import render
from rest_framework import viewsets
from api.models import Group, Event
from api.serializers import GroupSerializer, EventSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer