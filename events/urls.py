from django.urls import path
from . import views


urlpatterns = [
    path('', views.FeaturedView.as_view(), name='featured_events'),
    path('events/', views.EventsList.as_view(), name='events_list'),
]
