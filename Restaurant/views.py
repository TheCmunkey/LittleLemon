from django.shortcuts import render
from rest_framework import generics
from rest_framework import  viewsets 
from .models import *
from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

#######################################################################################################################

def index(request):
    
    return render(request, 'index.html', {}) 

  
#######################################################################################################################

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
  
#######################################################################################################################
  