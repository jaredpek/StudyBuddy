from django.test import TestCase
from products.models import Product
from rest_framework.test import APIClient
from django.contrib.auth.models import User

from django.core.files.uploadedfile import SimpleUploadedFile

import datetime
import json

# Create your tests here.
class CartTestCase(TestCase):
    '''
    Test cases for Cart model
    '''
    def setUp(self):
        '''
        The method responsible for setting up the required data for the tests
        '''
        self.client = APIClient()
        self.user_test = User.objects.create_user(username="tester", email="test@gmail.com", password="123")

        product1 = {
            'name' : 'Book 1',
            'price' : 20,
            'image' : SimpleUploadedFile("face.jpg", b"")
        }

        product2 = {
            'name' : 'Book 2',
            'price' : 40,
            'image' : SimpleUploadedFile("face.jpg", b"")
        }

        self.product_1 = Product.objects.create(**product1)
        self.product_2 = Product.objects.create(**product2)

        user = User.objects.get(username="tester")

        self.client.login(username="tester", password="123")
        self.client.force_authenticate(user=user)

    def add_product_to_cart(self, cart_data):
        response = self.client.post(f'/api/cart/', cart_data, format='json')

        return response

    def update_product_in_cart(self, cart_data):
        response = self.client.put(f'/api/cart/', cart_data, format='json')

        return response

    def remove_product_from_cart(self, cart_data):
        response = self.client.put(f'/api/cart/', cart_data, format='json')

        return response

    def checkout_cart(self, checkout_data):
        response = self.client.post(f'/api/cart/checkout/', checkout_data, format='json')

        return response

    def test_cart(self):
        '''
        Testing the following:
        - Adding product to cart
        - Adding invalid product to cart
        - Updating product quantity in cart
        - Deleting product from cart
        - Placing order for cart items
        '''

        # Adding products to cart
        cart_data_1 = {
            'product' : 1,
            'quantity' : 1
        }

        cart_data_2 = {
            'product' : 2,
            'quantity' : 3
        }

        response_1 = self.add_product_to_cart(cart_data_1)
        response_2 = self.add_product_to_cart(cart_data_2)

        response_1_data = response_1.content.decode('ascii')
        response_1_data = json.loads(response_1_data)

        response_2_data = response_2.content.decode('ascii')
        response_2_data = json.loads(response_2_data)

        self.assertEqual(response_1.status_code, 200)
        self.assertEqual(response_1_data["status"], "success")

        self.assertEqual(response_2.status_code, 200)
        self.assertEqual(response_2_data["status"], "success")

        # Adding invalid product to cart with quantity

        cart_data_invalid = {
            'product' : 3,
            'quantity' : 2
        }

        response_invalid = self.add_product_to_cart(cart_data_invalid)

        invalid_data = response_invalid.content.decode('ascii')
        invalid_data = json.loads(invalid_data)

        self.assertEqual(response_invalid.status_code, 400)
        self.assertEqual(invalid_data["status"], "error")

        # Updating product quantity in cart

        cart_data_update = {
            'product' : 2,
            'quantity' : 1
        }

        response_update = self.update_product_in_cart(cart_data_update)

        update_data = response_update.content.decode('ascii')
        update_data = json.loads(update_data)

        self.assertEqual(response_update.status_code, 200)
        self.assertEqual(update_data["status"], "success")

        # Deleting product from cart

        cart_data_delete = {
            'product' : 1,
            'quantity' : 0
        }

        response_delete = self.remove_product_from_cart(cart_data_delete)

        delete_data = response_delete.content.decode('ascii')
        delete_data = json.loads(delete_data)

        self.assertEqual(response_delete.status_code, 200)
        self.assertEqual(delete_data["status"], "success")

        # Placing order for cart items

        checkout_data = {
            'address' : '66 Nanyang Crescent',
            'postal_code' : 636960
        }

        checkout_response = self.checkout_cart(checkout_data)

        checkout_data = checkout_response.content.decode('ascii')
        checkout_data = json.loads(checkout_data)
        
        self.assertEqual(checkout_response.status_code, 200)
        self.assertEqual(checkout_data["status"], "success")