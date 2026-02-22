from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Wallet

User = get_user_model()

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        # We only expose what the user needs to see
        fields = ['balance', 'currency', 'daily_limit', 'created_at']
        # Make everything read-only so users can't artificially inflate their balance via API
        read_only_fields = ['balance', 'currency', 'daily_limit', 'created_at']


class UserSerializer(serializers.ModelSerializer):
    # This nests the wallet data inside the user data automatically
    wallet = WalletSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'first_name', 'last_name', 'wallet']


class UserRegistrationSerializer(serializers.ModelSerializer):
    # Write-only ensures the password is never returned in the API response
    password = serializers.CharField(write_only=True, min_length=8, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'first_name', 'last_name']

    def create(self, validated_data):
        # We must use create_user() here, not regular create(), so Django hashes the password
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        return user