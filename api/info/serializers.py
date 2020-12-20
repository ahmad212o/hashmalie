from rest_framework import serializers
from .models import Info


class InfoSerializers(serializers.ModelSerializer):
    class Meta:
        model=Info
        fields=(
            '__all__'
            )
        depth = 1


