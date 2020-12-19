from rest_framework import serializers
from .models import Project,File,Contractor,Owner,Architect,Address

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields=(
            '__all__'
            )
        depth = 1




        





    


