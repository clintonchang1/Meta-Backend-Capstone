from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = menu
        fields = ['id', 'title', 'price', 'inventory']


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = booking
        fields = '__all__'
    
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
        


        