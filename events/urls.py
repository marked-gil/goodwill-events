from django.urls import path
from . import views


urlpatterns = [
     path('', views.FeaturedView.as_view(), name='featured_events'),
     path('seatmap/', views.SeatMapView.as_view(), name='view_seatmap'),
     path('events/', views.EventsList.as_view(), name='events_list'),
     path('<slug:slug>/', views.EventDetails.as_view(), name='event_details'),
     path('like/<slug:slug>', views.EventLike.as_view(), name='event_like'),
     path('comment/<slug:slug>/', views.CommentView.as_view(),
          name='event_comment'),
     path('delete-comment/<pk>/', views.DeleteComment.as_view(),
          name='delete_comment'),
]
