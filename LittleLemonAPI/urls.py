from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from LittleLemonAPI import views

urlpatterns = [
    
    path('message/', views.msg),
        
    path('menu-items/', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('booking/', views.BookingView.as_view()),
    path('booking/<int:pk>', views.SingleBookingView.as_view()),
 
    path('api-token-auth/', obtain_auth_token)
]