from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import get_user_model
from .serializers import UserRegistrationSerializer, UserSerializer

User = get_user_model()

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny] 

# --- NEW VIEW ---

class UserProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    # This acts as the "Bouncer" - no token, no entry!
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # Automatically grabs the user attached to the token
        return self.request.user