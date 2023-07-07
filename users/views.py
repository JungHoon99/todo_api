from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from .models import User

# Create your views here.

class UserViewSet(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get(self, request, **kwargs):
        if kwargs.get('id') is None:
            return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
        else:
            todo_id = kwargs.get('id')
            try:
                todo_object = User.objects.get(id = todo_id)
            except User.DoesNotExist:
                return Response("Don't have Id", status=status.HTTP_400_BAD_REQUEST)
            user_serializer = UserSerializer(todo_object)
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        
    """
    POST /todo
    """
    def post(self, request, **kwargs):
        if kwargs.get('id') is not None:
            return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
        else:
            user_serializer = UserSerializer(data = request.data)
            if(user_serializer.is_valid()):
                user_serializer.save()
                return Response(user_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)