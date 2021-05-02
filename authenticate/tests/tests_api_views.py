from rest_framework.test import APITestCase
from rest_framework import status
from django.test import TestCase

from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

User = get_user_model()


class AuthenticateTest(APITestCase):

    def test_create_valid_user(self):
        data = {
                'email': 'johndoe@example.com',
                'password': 'foo12345',
                'first_name': 'John',
                'last_name': 'Doe'
        }

        response = self.client.post(reverse('create_user'), data,
                                    format='json')
        self.assertEqual(response.data['email'], 'johndoe@example.com')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_user_invalid_email(self):
        data = {
                'email': 'invalid-email',
                'password': 'foo12345',
                'first_name': 'John',
                'last_name': 'Doe'
        }

        response = self.client.post(reverse('create_user'), data,
                                    format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_invalid_password(self):
        data = {
                'email': 'johndoe2@example.com',
                'password': 'wrong',
                'first_name': 'John',
                'last_name': 'Doe'
        }

        response = self.client.post(reverse('create_user'), data,
                                    format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_invalid_name_letters(self):
        data = {
                'email': 'johndoe2@example.com',
                'password': 'foo12345',
                'first_name': '12345 12345',
                'last_name': '12345678'
        }

        response = self.client.post(reverse('create_user'), data,
                                    format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_invalid_name_numbers(self):
        data = {
                'email': 'johndoe2@example.com',
                'password': 'foo12345',
                'first_name': 123456,
                'last_name': '12345678'
        }

        response = self.client.post(reverse('create_user'), data,
                                    format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user_already_exists(self):
        user = {
                'email': 'johndoe2@example.com',
                'password': 'foo12345',
                'first_name': 'John',
                'last_name': 'Doe'
        }

        create_user = self.client.post(reverse('create_user'), user,
                                       format='json')

        data = {
                'email': 'johndoe2@example.com',
                'password': 'foo12345',
                'first_name': 'John',
                'last_name': 'Doe'
        }

        response = self.client.post(reverse('create_user'), data,
                                    format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_update_user_password(self):
        user = {
                'email': 'changepassword@email.com',
                'password': 'old_password',
                'first_name': 'John',
                'last_name': 'Doe'
        }

        self.client.post(reverse('create_user'), user,
                         format='json')

        update_user = {
            'email': 'changepassword@email.com',
            'old_password': 'old_password',
            'new_password': 'new_password',
            'password_confirmation': 'new_password'
        }

        update_user_response = self.client.put(reverse('update_user'),
                                               update_user,
                                               format='json')

        token_data = {
                'email': 'changepassword@email.com',
                'password': 'old_password'
        }

        token_response = self.client.post(reverse('token_create'), token_data,
                                          format='json')

        self.assertEqual(update_user_response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(token_response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_invalid_update_user_password(self):
        user = {
                'email': 'changepassword@email.com',
                'password': 'old_password',
                'first_name': 'John',
                'last_name': 'Doe'
        }

        self.client.post(reverse('create_user'), user,
                         format='json')

        update_user = {
            'email': 'changepassword@email.com',
            'old_password': 'wrong_old_password',
            'new_password': 'new_password',
            'password_confirmation': 'new_password'
        }

        update_user_response = self.client.put(reverse('update_user'),
                                               update_user,
                                               format='json')

        token_data = {
                'email': 'changepassword@email.com',
                'password': 'new_password'
                
        }

        token_response = self.client.post(reverse('token_create'), token_data,
                                          format='json')

        self.assertEqual(update_user_response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(token_response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_invalid_update_user_new_password(self):
        user = {
                'email': 'changepassword@email.com',
                'password': 'old_password',
                'first_name': 'John',
                'last_name': 'Doe'
        }

        self.client.post(reverse('create_user'), user,
                         format='json')

        update_user = {
            'email': 'changepassword@email.com',
            'old_password': 'old_password',
            'new_password': 'new_password',
            'password_confirmation': 'wrong_confirmation'
        }

        update_user_response = self.client.put(reverse('update_user'),
                                               update_user,
                                               format='json')

        token_data = {
                'email': 'changepassword@email.com',
                'password': 'new_password'
        }

        token_response = self.client.post(reverse('token_create'), token_data,
                                          format='json')

        self.assertEqual(update_user_response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(token_response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_invalid_update_user_wrong_json(self):
        user = {
                'email': 'changepassword@email.com',
                'password': 'old_password',
                'first_name': 'John',
                'last_name': 'Doe'
        }

        self.client.post(reverse('create_user'), user,
                         format='json')

        update_user = {
            'email': 'changepassword@email.com',
            'old_password': 'old_password',
            'new_password': 'new_password',
        }

        update_user_response = self.client.put(reverse('update_user'),
                                               update_user,
                                               format='json')

        self.assertEqual(update_user_response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_token_obtain_valid_user(self):
        user = {
                'email': 'johndoe@example.com',
                'password': 'foo12345',
                'first_name': 'John',
                'last_name': 'Doe'
        }

        self.client.post(reverse('create_user'), user,
                         format='json')

        data = {
                'email': 'johndoe@example.com',
                'password': 'foo12345'
        }

        response = self.client.post(reverse('token_create'), data,
                                    format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_token_obtain_invalid_user(self):
        data = {
                'email': 'not-valid-user@example.com',
                'password': 'foo'
        }

        response = self.client.post(reverse('token_create'), data,
                                    format='json')

        self.assertEqual(response.data['detail'], "No active account found with the given credentials")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_refresh_valid_token(self):
        user = {
                'email': 'johndoe@example.com',
                'password': 'foo12345',
                'first_name': 'John',
                'last_name': 'Doe'
        }

        self.client.post(reverse('create_user'), user,
                         format='json')

        data = {
                'email': 'johndoe@example.com',
                'password': 'foo12345'
        }

        token = self.client.post(reverse('token_create'), data,
                                 format='json')

        token_data = {
                'refresh': token.data['refresh'],
        }

        response = self.client.post(reverse('token_refresh'), token_data,
                                    format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_refresh_invalid_token(self):
        data = {
                'email': 'johndoe@example.com',
                'password': 'foo12345'
        }

        token = self.client.post(reverse('token_create'), data,
                                 format='json')

        token_data = {
                'refresh': 'invalid.token',
        }

        response = self.client.post(reverse('token_refresh'), token_data,
                                    format='json')

        self.assertEqual(response.data['detail'], "Token is invalid or expired")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
