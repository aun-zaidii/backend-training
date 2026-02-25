from rest_framework import serializers

from .models import CensusLog


class CensusLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = CensusLog
        fields = "__all__"
