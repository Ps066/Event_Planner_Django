from django.contrib import admin
from django.urls import path, include
from userDashboard.views import *

app_name = "userDashboard"

urlpatterns = [
    path('events/', dashboard_view, name="dash"),
    path('products/', product_view, name="product"),
    path('profiel/', profile_view, name="profile"),
    # path('add/', add_view, name="add")
    # path('booking/', slotBooking_view, name="booking"),
    # path('profile/', userProfile_view, name="userProfile"),
    # path("delete/<str:id>/", delete_view, name="delete"),
    # path("shop/", shopDetail_view, name="shopDetails"),
    
]