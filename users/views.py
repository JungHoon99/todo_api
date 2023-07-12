from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import bcrypt
import jwt
from todo_api.settings import SECRET_KEY

from .serializers import UserSerializer
from .models import User
from .validators import password_validate

# Login view
# /user/login
class UserLoginViewSet(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def post(self, request, **kwargs):
        if('email' not in request.data or 'pw' not in request.data):
            return Response("Not correct request data", status=status.HTTP_400_BAD_REQUEST)
        if not User.objects.filter(email = request.data['email']).exists():
            return Response("wrong email try again", status=status.HTTP_400_BAD_REQUEST)
        
        user_object = User.objects.get(email = request.data['email'])
        
        pw_encode = request.data['pw'].encode('utf-8')
        
        if not bcrypt.checkpw(pw_encode, user_object.pw.encode('utf-8')):
            return Response("wrong password try again", status=status.HTTP_400_BAD_REQUEST)
        
        data = jwt.encode({'user_id' : user_object.id, 
                    'user_email' : user_object.email}, SECRET_KEY, algorithm='HS256')
        
        return Response(data, status=status.HTTP_200_OK)
        
        
        
        
# user basic view
# /user or /user/<int:id>
class UserViewSet(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get(self, request, **kwargs):
        if kwargs.get('id') is None:
            return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
        else:
            user_id = kwargs.get('id')
            try:
                user_object = User.objects.get(id = user_id)
            except User.DoesNotExist:
                return Response("Don't have Id", status=status.HTTP_400_BAD_REQUEST)
            user_serializer = UserSerializer(user_object)
            return Response(user_serializer.data, status=status.HTTP_200_OK)

    """
    POST /todo
    """
    def post(self, request, **kwargs):
        #접근 url 제어
        if kwargs.get('id') is not None:
            return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
        
        #등록된 id인지 확인
        if User.objects.filter(email = request.data['email']).exists():
            return Response("already sign up email", status=status.HTTP_400_BAD_REQUEST)
        
        #비밀번호 유효성 검사
        try:
            password_validate(request.data['pw'])
        except:
            return Response("wrong password", status=status.HTTP_400_BAD_REQUEST)
        
        data = request.data.copy() #request.data는 QueryDict 데이터로 immutable해서 mutable하게 바꿔야함
        
        #password 암호화
        password = request.data['pw'].encode('utf-8')
        password_crypt = bcrypt.hashpw(password, bcrypt.gensalt())
        data['pw'] = password_crypt.decode('utf-8')
        
        user_serializer = UserSerializer(data = data)
        if(user_serializer.is_valid()):
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)