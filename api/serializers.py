from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from api.models import Group, Event, UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('image',)

class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()
    class Meta:
        model = User
        fields = ('id', 'username','email','password', 'profile')
        extra_kwargs = {'password': {'write_only': True, 'required': False}}
    
    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create_user(**validated_data)
        UserProfile.objects.create(
            user=user,
            **profile_data
        )
        Token.objects.create(user=user)
        return user

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

