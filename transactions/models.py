from django.db import models
from django.conf import settings
import uuid

class Transaction(models.Model):
    # Using UUIDs for transaction IDs makes them unguessable and secure
    transaction_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    
    # Who is sending and who is receiving?
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sent_transactions', on_delete=models.RESTRICT)
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='received_transactions', on_delete=models.RESTRICT)
    
    # Financial data
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    # Status tracking (Pending, Completed, Failed)
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('COMPLETED', 'Completed'),
        ('FAILED', 'Failed'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    
    # Description (e.g., "Dinner refund")
    description = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ['-timestamp'] # Newest transactions show up first

    def __str__(self):
        return f"{self.sender.email} -> {self.receiver.email}: {self.amount} ({self.status})"