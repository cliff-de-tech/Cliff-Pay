from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # This routes any URL starting with api/accounts/ to the accounts app
    path('api/accounts/', include('accounts.urls')), 
    path('api/transactions/', include('transactions.urls')),
]