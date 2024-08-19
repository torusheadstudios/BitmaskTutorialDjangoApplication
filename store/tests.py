from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import OrderItem

class OrderItemTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.url = reverse('create_order_items')
        self.valid_payload = {
            "order_name": "Test Order",
            "items": [
                {"product": "shirt", "bitmask": 2129921},
                {"product": "pants", "bitmask": 2359300}
            ]
        }

    def test_order_item_creation(self):
        """Test that OrderItem objects are correctly created"""
        response = self.client.post(self.url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(OrderItem.objects.count(), 2)
        order_item = OrderItem.objects.first()
        self.assertEqual(order_item.order_name, 'Test Order')
        self.assertEqual(order_item.product, 'shirt')
        self.assertEqual(order_item.bitmask, 2129921)

    def test_order_item_deletion(self):
        """Test that an OrderItem can be deleted"""
        # Create an order item first
        response = self.client.post(self.url, self.valid_payload, format='json')
        order_item = OrderItem.objects.first()
        
        # Delete the order item
        delete_url = reverse('delete_order_item', kwargs={'pk': order_item.pk})
        delete_response = self.client.delete(delete_url)
        self.assertEqual(delete_response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(OrderItem.objects.count(), 1)  # Only one item should remain
        