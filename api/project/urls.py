from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include
from rest_framework.authtoken import views

from .views import ProjectView


urlpatterns = [
  path('',ProjectView.as_view(),name=''),
]
