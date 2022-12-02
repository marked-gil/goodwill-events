from django.urls import path
from . import views


urlpatterns = [
    path('account/<str:slug>', views.MemberAccount.as_view(),
         name='member_account')
]
