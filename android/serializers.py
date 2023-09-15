# Serializers for Django REST framework:
# - `UserSerializer` serializes User model fields like 'id', 'username', 'password', and 'email'.
# - `ContentSerializer` serializes all fields of the Content model.
# Convert instances of the User and Content models into JSON when you send responses from your API
from rest_framework import serializers
from django.contrib.auth.models import User
from main.models import Content

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ['id', 'username', 'password', 'email']

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__' 
