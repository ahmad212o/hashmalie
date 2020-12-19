from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include
from rest_framework.authtoken import views

from .views import ProjectView,ManageProjectView,CreateProjectView


urlpatterns = [
  path('',ProjectView.as_view(),name='view'),
  path('create/',CreateProjectView.as_view(),name='create'),
  path('<int:pk>/manage/',ManageProjectView.as_view(),name='manage'),
]
