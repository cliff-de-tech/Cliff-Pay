from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings  # <--- NEW IMPORT

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    # We can add more fields later (like phone_number)
    
    # These settings help Django avoid conflicts
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
    
class Wallet(models.Model):
    # OneToOneField means: One User = Exactly One Wallet
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='wallet')
    
    # Always use DecimalField for money (Float is bad for math!)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    currency = models.CharField(max_length=3, default='GHS')
    
    # The daily limit feature
    daily_limit = models.DecimalField(max_digits=12, decimal_places=2, default=1000.00)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email}'s Wallet - {self.currency} {self.balance}"