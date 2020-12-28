from rest_framework import serializers
from .models import Project,File,Contractor,Owner,Architect,Address


class OwnerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields=(
            '__all__'
            )

class ArchitectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Architect
        fields=(
            '__all__'
            )


class AddressSerializers(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields=(
            '__all__'
            )

class ContractorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contractor
        fields=(
            '__all__'
            )

class FileSerializers(serializers.ModelSerializer):
        project=serializers.HyperlinkedRelatedField(read_only=True,view_name='project')
        class Meta:
            model = File
            fields=(
             '__all__'
                )







class ProjectSerializer(serializers.ModelSerializer):
    owner=serializers.HyperlinkedRelatedField(read_only=True,view_name='owner')
    contractor=serializers.HyperlinkedRelatedField(read_only=True,view_name='contractor')
    address=serializers.HyperlinkedRelatedField(read_only=True,view_name='address')
    architect=serializers.HyperlinkedRelatedField(read_only=True,view_name='architect')
    file=FileSerializers(many=True,read_only=True)
    class Meta:
        model = Project
        fields=(
           '__all__'
            )
    
   

        



