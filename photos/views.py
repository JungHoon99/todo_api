from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import datetime

from .serializers import PhotoSerializer
from .models import Photo
# Create your views here.

class PhotoViewSet(APIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    
    def get(self, request, **kwargs):
        photo_queryset = Photo.objects.all() #모든 User의 정보를 불러온다.
        photo_queryset_serializer = PhotoSerializer(photo_queryset, many=True)
        return Response(photo_queryset_serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, **kwargs):
        data = request.data.copy()
        
        now = datetime.datetime.now()
        
        data['image'].name = now.strftime('%Y-%m-%d %H:%M:%S')+'.png'
        
        photo_serializer = PhotoSerializer(data = data)
        if(photo_serializer.is_valid()):
            photo_serializer.save()
            return Response(photo_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)