from django.urls import path
from .views import SendMoneyView, TransactionHistoryView # Import the new view for transaction history

urlpatterns = [
    path('send/', SendMoneyView.as_view(), name='send_money'),
    path('history/', TransactionHistoryView.as_view(), name='history'), # Add a new URL pattern for transaction history
]