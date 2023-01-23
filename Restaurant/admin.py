from django.contrib import admin
from .models import *

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    
    list_display  = ('id', 'name', 'no_of_guests', 'booking_date')
    ordering      = ['name', 'booking_date']
    search_fields = ['name']
   
@admin.register(Menu)   
class MenuAdmin(admin.ModelAdmin):
    
    list_display  = ('id', 'title', 'price', 'inventory')
    ordering      = ['title', 'price']
    search_fields = ['title']
    
@admin.register(MenuItem)   
class MenuItemAdmin(admin.ModelAdmin):
    
      list_display  = ('id', 'title', 'price', 'inventory')
      ordering      = ['title', 'price']
      search_fields = ['title']    

 