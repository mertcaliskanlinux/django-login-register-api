import jwt 
from .models import Jwt
from user.models import CustomUser,CustomUserManager
from datetime import datetime,timedelta
from django.conf import settings
import random
import string
from rest_framework.views import APIView
from .serializers import LoginSerializer,RegisterSerializer
from django.contrib.auth import authenticate
from rest_framework.response import Response


def get_random(length):
    ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))

def get_access_token(payload):
    
    return jwt.encode(
        
        
        {"exp":datetime.now() + timedelta(minutes=5),**payload},
        settings.SECRET_KEY,
        algorithm="HS256"
        
    )
    
def get_refresh_token():
    
    return jwt.encode(
        
        
        {"exp":datetime.now() + timedelta(days=365),"data":get_random(10)},
        settings.SECRET_KEY,
        algorithm="HS256"
        
    )
    
class LoginView(APIView):
    serializer_class = LoginSerializer
    
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        print("burasi view")
        
        user = authenticate(username = serializer._validated_data['email'],
                            password = serializer.validated_data['password'])
        
        print(user)
        
        
        if not user:
            return Response({
                'error':"/gateway/login,Invalid email or password"
            },status="400")
            
        access = get_access_token({"user_id":user.id})
        refresh = get_refresh_token()
        Jwt.objects.create(
            user_id = user.id,access=access,refresh=refresh
        )
        return Response({
            
            'access': access,
            'refresh': refresh
        })
        
        
        


class RegisterView(APIView):
    serializer_class = RegisterSerializer
    
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        CustomUser.object._create_user(**serializer.validated_data)
        
        return Response({'success':'/gateway/register, Kayıt İşleminiz Tamamlandı'})
        
        