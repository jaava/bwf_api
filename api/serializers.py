from rest_framework import serializers
from api.models import Group, Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'team1', 'team2', 'time', 'score1', 'score2', 'group')

class GroupSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Group
        fields = ('id', 'name', 'location', 'description')

class GroupFullSerializer(serializers.ModelSerializer):

    events = EventSerializer(many=True, read_only=True)
    class Meta:
        model = Group
        fields = ('id', 'name', 'location', 'description', 'events')

