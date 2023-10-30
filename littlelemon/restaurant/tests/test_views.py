from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu1 = Menu.objects.create(title='IceCream', price=80, inventory=100)
        self.menu2 = Menu.objects.create(title='Cake', price=100, inventory=50)
        self.menu3 = Menu.objects.create(title='Coffee', price=50, inventory=200)

    def test_getall(self):
        response = self.client.get(reverse('menu-list'))  # Change 'menu-list' to the correct url name for your Menu list view
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    