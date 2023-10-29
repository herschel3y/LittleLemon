from django.urls import path
from . import views
from .views import UserCreateView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('register/', UserCreateView.as_view(), name='user-register'),
    path('api-token-auth/', obtain_auth_token),
]
