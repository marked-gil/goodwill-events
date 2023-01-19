from django.urls import path
from . import views

urlpatterns = [
     path('seat-reservation/',
          views.EventSeatsView.as_view(), name='seatmap'),
     path('reserve-seats/', views.ReserveSeats.as_view(),
          name='reserve_seats'),
     path('update-reservation/', views.UpdateSeatsReservation.as_view(),
          name='update_reservation'),
     path('delete-reservation/', views.DeleteSeatsReservation.as_view(),
          name='delete_reservation'),
]
