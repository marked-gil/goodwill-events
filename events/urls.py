from django.urls import path
from . import views


urlpatterns = [
    path('', views.FeaturedView.as_view(), name='featured_events')
]
