from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Transaction
from decimal import Decimal

User = get_user_model()

class TransactionSerializer(serializers.ModelSerializer):
    # We ask for an email, not a user ID, because it's much better for UX
    receiver_email = serializers.EmailField(write_only=True)
    
    class Meta:
        model = Transaction
        fields = ['transaction_id', 'receiver_email', 'amount', 'timestamp', 'status', 'description']
        read_only_fields = ['transaction_id', 'timestamp', 'status']

    def validate(self, data):
        sender = self.context['request'].user
        amount = data['amount']
        receiver_email = data['receiver_email']

        # 1. No negative or zero amounts
        if amount <= Decimal('0.00'):
            raise serializers.ValidationError("Amount must be greater than zero.")

        # 2. Check if receiver exists
        try:
            receiver = User.objects.get(email=receiver_email)
        except User.DoesNotExist:
            raise serializers.ValidationError("Receiver with this email does not exist.")

        # 3. Can't send to yourself
        if sender == receiver:
            raise serializers.ValidationError("You cannot send money to yourself.")

        # 4. Check balance
        if sender.wallet.balance < amount:
            raise serializers.ValidationError("Insufficient balance.")

        # 5. Check daily limit 
        if amount > sender.wallet.daily_limit:
            raise serializers.ValidationError("Amount exceeds your daily limit.")

        # Pass the actual receiver object to the view
        data['receiver'] = receiver
        return data