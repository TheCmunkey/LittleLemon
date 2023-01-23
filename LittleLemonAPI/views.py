 
from django.shortcuts import render
  
from rest_framework import generics
from rest_framework import status
from rest_framework import  viewsets 
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from Restaurant.models import *
from Restaurant.serializers import *
 
#######################################################################################################################
 
@api_view()
@permission_classes([IsAuthenticated])
def msg(request):
    return Response({"message":"This view is protected"})

#######################################################################################################################

class MenuItemsView(generics.ListCreateAPIView):
        permission_classes = [IsAuthenticated]
        queryset = MenuItem.objects.all()
        serializer_class = MenuItemSerializer
        
#######################################################################################################################
        
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
        permission_classes = [IsAuthenticated]
        queryset = MenuItem.objects.all()
        serializer_class = MenuItemSerializer
        
#######################################################################################################################

class BookingView(generics.ListCreateAPIView):
        permission_classes = [IsAuthenticated]
        queryset = Booking.objects.all()
        serializer_class = BookingSerializer
        
#######################################################################################################################
        
class SingleBookingView(generics.RetrieveUpdateDestroyAPIView):
        permission_classes = [IsAuthenticated]
        queryset = Booking.objects.all()
        serializer_class = BookingSerializer
        
#######################################################################################################################
        
        