from rest_framework import serializers
from .models import CreditRisk

class CreditRiskSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditRisk
        fields = '__all__'