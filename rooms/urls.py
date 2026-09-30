from django.urls import path

from . import views

urlpatterns = [

    path('', views.dashboard, name='dashboard'),

    path('rooms/', views.room_list, name='room_list'),

    path('bookings/', views.booking_list, name='booking_list'),

    path('guests/', views.guest_list, name='guest_list'),

    path('add-booking/', views.add_booking, name='add_booking'),

    path('add-room/', views.add_room, name='add_room'),

    path('edit-room/<int:room_id>/', views.edit_room, name='edit_room'),

    path('delete-room/<int:room_id>/', views.delete_room, name='delete_room'),

    path('edit-booking/<int:booking_id>/', views.edit_booking, name='edit_booking'),

    path('delete-booking/<int:booking_id>/', views.delete_booking, name='delete_booking'),

]