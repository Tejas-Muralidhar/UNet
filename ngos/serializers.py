from rest_framework import serializers
from .models import NGO

class NGODetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = NGO
        fields = ['id', 'name', 'purpose', 'address', 'contact_person', 'email', 'mobile_number']  # Ensure all required fields are included
