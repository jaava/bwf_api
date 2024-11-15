from django.shortcuts import render
from rest_framework import viewsets
from api.models import Group
from api.serializers import GroupSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer