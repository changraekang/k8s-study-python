from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from .models import Users

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'  # Serialize all fields
        extra_kwargs = {
            'user_id': {'validators': []},  # Assuming you handle uniqueness in the view or model
        }
    
    def create(self, validated_data):
        user = Users(**validated_data)
        user.password = make_password(validated_data['password'])  # Hash the password using Django's hasher
        user.save()
        return user

