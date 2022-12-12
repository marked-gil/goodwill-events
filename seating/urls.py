from django.urls import path
from . import views

urlpatterns = [
     path('reserve-seat/',
          views.EventSeatsView.as_view(), name='seatmap'),
     path('update-reservation/', views.UpdateSeatsReservation.as_view(),
          name='update_reservation'),
     path('delete-reservation/', views.DeleteSeatsReservation.as_view(),
          name='delete_reservation'),
]
