from django.urls import path, include
from rest_framework.authtoken import views

from .views import InfoListView,InfoUpdateView


urlpatterns = [
  path('<int:pk>/',InfoListView.as_view()),
  path('<int:pk>/update/',InfoUpdateView.as_view()),
  
]
