from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include
from rest_framework.authtoken import views

from .views import ProjectView,ManageProjectView,CreateProjectView,FileView,OwnerView,ArchitectView,AddressView,ContractorView


urlpatterns = [
  path('',ProjectView.as_view(),name='view'),
  path('owner/<int:pk>/',OwnerView.as_view(),name='owner'),
  path('architect/<int:pk>/',ArchitectView.as_view(),name='architect'),
  path('contractor/<int:pk>/',ContractorView.as_view(),name='contractor'),
  path('address/<int:pk>/',AddressView.as_view(),name='address'),
  path('file/<int:pk>/',FileView.as_view(),name='file'),
  path('create/',CreateProjectView.as_view(),name='create'),
  path('<int:pk>/manage/',ManageProjectView.as_view(),name='project'),
]
