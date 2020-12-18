from django.shortcuts import render
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .serializers import ProjectSerializer
from .models import Project,File,Address,Architect,Owner,Contractor

# Create your views here.
class ProjectView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    serializer_class=ProjectSerializer
    queryset=Project.objects.all()
    permission_classes=(IsAuthenticated,)
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    

