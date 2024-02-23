from django.test import TestCase
from restaurant.models import menu

class MenuTest(TestCase):
    def test_create_item(self):
        item = menu.objects.create(title="Icecream", price=5, inventory=100)
        
        self.assertEqual(str(item), "Icecream : 5")
        