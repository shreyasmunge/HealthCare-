from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

'''
#Endpoint: http://127.0.0.1:8000/api/auth/register/
#Body:
{
  "email": "test@example.com",
  "username": "testuser",
  "password": "securepassword123"
}
#Respond
{
  "message": "User registered successfully!"
}'''
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

'''
#Endpoint: http://127.0.0.1:8000/api/auth/login/
#Body:
{
  "email": "test@example.com",
  "password": "securepassword123"
}
#Respond:
{
  "refresh": "your_refresh_token_here",
  "access": "your_access_token_here"
}'''
# Login view using built-in JWT view
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email  # optional: add email to token
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
