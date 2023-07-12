from django.urls import path
from .views import UserViewSet
from .views import UserLoginViewSet

urlpatterns = [
    path('', UserViewSet.as_view()),
    path('auth/', UserLoginViewSet.as_view()),
    path('<int:id>', UserViewSet.as_view()),
]
