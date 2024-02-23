from django.test import TestCase, Client
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status
from restaurant.models import menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        menu.objects.create(title="Burger", price=4, inventory=50)
        menu.objects.create(title="Coke", price=2, inventory=125)
        
    def test_getall(self):
        response = self.client.get(reverse('menu'))
        menus = menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.assertEqual(response.data, serializer.data)