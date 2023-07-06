from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TodoSerializer
from .models import Todo

# Create your views here.

class TodoViewSet(APIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
    """
    GET /user/{user_id}
    """
    def get(self, request, **kwargs):
        if kwargs.get('id') is None:
            todo_queryset = Todo.objects.all() #모든 User의 정보를 불러온다.
            todo_queryset_serializer = TodoSerializer(todo_queryset, many=True)
            return Response(todo_queryset_serializer.data, status=status.HTTP_200_OK)
        else:
            todo_id = kwargs.get('id')
            try:
                todo_object = Todo.objects.get(id = todo_id)
            except Todo.DoesNotExist:
                return Response("Don't have Id", status=status.HTTP_400_BAD_REQUEST)
            todo_serializer = TodoSerializer(todo_object)
            return Response(todo_serializer.data, status=status.HTTP_200_OK)
    
    """
    POST /user/{user_id}
    """
    def post(self, request, **kwargs):
        if kwargs.get('id') is not None:
            return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
        else:
            todo_serializer = TodoSerializer(data = request.data)
            if(todo_serializer.is_valid()):
                todo_serializer.save()
                return Response(todo_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
            
    """
    PUT /user/{user_id}
    """
    def put(self, request, **kwargs):
        if kwargs.get('id') is None:
            return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
        else:
            todo_id = kwargs.get('id')
            todo_object = Todo.objects.get(id = todo_id)
            
            update_todo_serializer = TodoSerializer(todo_object, data = request.data)
            if update_todo_serializer.is_valid():
                update_todo_serializer.save()
                return Response(update_todo_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)