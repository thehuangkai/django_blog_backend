from rest_framework import serializers
from .models import Portfolio

class PortfolioSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Portfolio 
        fields = '__all__'

    def to_representation(self, instance):
        row = super(PortfolioSerializer, self).to_representation(instance)
        return {row["id"]:row}
