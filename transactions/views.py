from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from django.db import models
from .models import Transaction
from .serializers import TransactionSerializer

class SendMoneyView(generics.CreateAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        sender = self.request.user
        receiver = serializer.validated_data['receiver']
        amount = serializer.validated_data['amount']

        # THE FIX: Remove 'receiver_email' so Django doesn't try to save it to the DB
        serializer.validated_data.pop('receiver_email', None)

        with transaction.atomic():
            # 1. Deduct from sender
            sender.wallet.balance -= amount
            sender.wallet.save()

            # 2. Add to receiver
            receiver.wallet.balance += amount
            receiver.wallet.save()

            # 3. Create the permanent receipt
            serializer.save(
                sender=sender,
                receiver=receiver,
                status='COMPLETED'
            )
class TransactionHistoryView(generics.ListAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # Get all transactions where the user is either the sender OR the receiver
        return Transaction.objects.filter(models.Q(sender=user) | models.Q(receiver=user))            