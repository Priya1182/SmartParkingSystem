from django.urls import path
from parking import views

urlpatterns =[
path('',views.home,name='home'),
path('login',views.login,name='login'),
path('register',views.register,name='register'),
path("logout",views.logout,name="logout"),
path("profile",views.profile,name="profile"),
path("creatparkingslot",views.creatparkingslot,name="creatparkingslot"),
path("evcharging",views.evcharging,name="evcharging"),
path("parking",views.parking,name="parking"),
path("checkout",views.checkout,name="checkout"),
path("booking-success",views.bookingSuccess,name="bookingSuccess"),
path("deleterecord",views.deleterecord,name="deleterecord")
]