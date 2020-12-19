from django.shortcuts import render
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.generics import RetrieveUpdateDestroyAPIView,ListAPIView,CreateAPIView
from .serializers import ProjectSerializer
from .models import Project,File,Address,Architect,Owner,Contractor

# Create your views here.
class ProjectView(ListAPIView):
    serializer_class=ProjectSerializer
    queryset=Project.objects.all()
    permission_classes=(IsAuthenticated,)
   
    
class CreateProjectView(CreateAPIView):
    serializer_class=ProjectSerializer
    queryset=Project.objects.all()
    #permission_classes=(IsAuthenticated,IsAdminUser)

class ManageProjectView(RetrieveUpdateDestroyAPIView):
    serializer_class=ProjectSerializer
    def get_queryset(self):
        queryset = Project.objects.filter(id=self.kwargs["pk"])
        return queryset
    permission_classes=(IsAuthenticated,IsAdminUser)