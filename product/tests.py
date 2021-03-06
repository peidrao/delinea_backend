from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from model_bakery import baker
from oauth2_provider.settings import oauth2_settings
from oauth2_provider.models import get_access_token_model, get_application_model
from django.utils import timezone
from authentication.models import User

from .models import Product


Application = get_application_model()
AccessToken = get_access_token_model()


class ProductTests(APITestCase):

    def setUp(self):

        oauth2_settings._SCOPES = [
            "read", "write", "scope1", "scope2", "resource1"]

        self.test_user = baker.make(
            User, email="test@gmail.com", password='tecarch123')

        self.application = Application.objects.create(
            name="Test Application",
            redirect_uris="http://localhost http://example.com http://example.org",
            user=self.test_user,
            client_type=Application.CLIENT_CONFIDENTIAL,
            authorization_grant_type=Application.GRANT_AUTHORIZATION_CODE,
        )

        self.access_token = AccessToken.objects.create(
            user=self.test_user,
            scope="read write",
            expires=timezone.now() + timezone.timedelta(seconds=300),
            token="secret-access-token-key",
            application=self.application
        )
        # read or write as per your choice
        self.access_token.scope = "read"
        self.access_token.save()

        # correct token and correct scope
        self.auth = "Bearer {0}".format(self.access_token.token)

    def test_create_product(self):

        url = reverse('products_urls:products-list')

        body = {
            "title": "Monkey D Luffy: Action Figure",
            "content": "The best action figure",
            "price": 129.99
        }

        response = self.client.post(url, body,  HTTP_AUTHORIZATION=self.auth)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.get().title,
                         'Monkey D Luffy: Action Figure')

    def test_destroy_product(self):
        product = baker.make(Product, owner=self.test_user)

        url = reverse('products_urls:products-detail', args=[product.id])

        response = self.client.delete(url, HTTP_AUTHORIZATION=self.auth)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_search_product_by_title(self):
        for _ in range(0, 5):
            baker.make(Product, title='Macbook', owner=self.test_user)
        for _ in range(0, 5):
            baker.make(Product, title='Iphone', owner=self.test_user)

        url = f"{reverse('products_urls:products-list')}?title=Iphone"

        response = self.client.get(
            url, format='json', HTTP_AUTHORIZATION=self.auth)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(5, len(response.data))

    def test_search_product_by_price(self):
        for _ in range(0, 5):
            baker.make(Product, price=11.90, owner=self.test_user)
        for _ in range(0, 5):
            baker.make(Product, price=11.91, owner=self.test_user)
        for _ in range(0, 5):
            baker.make(Product, price=11.95, owner=self.test_user)
        for _ in range(0, 5):
            baker.make(Product, price=12.90, owner=self.test_user)

        url = f"{reverse('products_urls:products-list')}?price=11.91"

        response = self.client.get(
            url, format='json', HTTP_AUTHORIZATION=self.auth)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(5, len(response.data))

    def test_patch_product(self):
        product = baker.make(Product, owner=self.test_user,
                             title='xyz', content='teste', price=125.99)

        url = reverse('products_urls:products-detail', args=[product.id])

        body = {
            'title': 'New Product',
            'content': 'New Content',
            'price': 259.35
        }

        response = self.client.patch(url, body,  HTTP_AUTHORIZATION=self.auth)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Product.objects.get().title, 'New Product')
        self.assertEqual(Product.objects.get().content, 'New Content')
        self.assertEqual(Product.objects.get().price, 259.35)

    def test_user_not_authorized_to_destroy(self):
        product = baker.make(Product)
        url = reverse('products_urls:products-detail', args=[product.id])

        response = self.client.delete(url, HTTP_AUTHORIZATION=self.auth)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_not_authorized_to_patch(self):
        product = baker.make(Product, title='xyz',
                             content='teste', price=125.99)

        url = reverse('products_urls:products-detail', args=[product.id])

        body = {
            'title': 'New Product',
            'content': 'New Content',
            'price': 259.35
        }

        response = self.client.patch(url, body, HTTP_AUTHORIZATION=self.auth)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
