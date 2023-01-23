from rest_framework import serializers
from .models import *

class  MenuSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Menu 
        fields = ['id', 'title', 'price', 'inventory']
        
        
class  MenuItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'inventory']
        
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'name', 'no_of_guests', 'booking_date']
     