from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient

from django.contrib.auth.models import User


class UserSignUpTestAPI(APITestCase):
    """
    TEST IS PASSED!!!
    """
    def setUp(self) -> None:
        self.client = APIClient()

    def test_user_registration_ok(self):
        """
        Ensure we can create a new user.
        TEST IS PASSED!!!
        """
        data = dict(username='test',
                    email='test@gmail.com',
                    password1='test2020',
                    password2='test2020')
        response = self.client.post('/rest-auth/registration/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.first().username, 'test')

    def test_user_registration_with_diff_passwords(self):
        """
        Ensure we can not create a new user if pass1 != pass2.
        TEST IS PASSED!!!
        """
        data = dict(username='test',
                    email='test@gmail.com',
                    password1='test2020',
                    password2='test2021')
        response = self.client.post('/rest-auth/registration/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 0)
        self.assertIn("The two password fields didn't match.", response.content.decode('utf-8'))

    def test_user_registration_with_exist_user(self):
        """
        Ensure we can not create a new user if the same username is exist.
        TEST IS PASSED!!!
        """
        # create a user which will have the same username
        exist_user = User.objects.create(username='test')
        data = dict(username='test',
                    email='test@gmail.com',
                    password1='test2020',
                    password2='test2020')
        response = self.client.post('/rest-auth/registration/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # The second user should not be created
        self.assertEqual(User.objects.count(), 1)
        self.assertIn("A user with that username already exists.", response.content.decode('utf-8'))


class UserLogInTestAPI(APITestCase):
    """
    TEST IS PASSED!!!
    """
    def setUp(self) -> None:
        self.client = APIClient()
        user = User.objects.create(username='test', email='test@gmail.com')
        user.set_password(raw_password='test2020')
        user.save()

    def test_user_login_ok(self):
        """
        Ensure that user can login.
        TEST IS PASSED!!!
        """
        data = dict(username='test',
                    email='test@gmail.com',
                    password='test2020')
        response = self.client.post('/rest-auth/login/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('key', response.data)

    def test_user_login_with_wrong_pwd(self):
        """
        Ensure that user can not login with wrong pwd.
        TEST IS PASSED!!!
        """
        data = dict(username='test',
                    email='test@gmail.com',
                    password='test20201')
        response = self.client.post('/rest-auth/login/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("Unable to log in with provided credentials.", response.content.decode('utf-8'))

    def test_user_login_with_wrong_username(self):
        """
        Ensure that user can not login with wrong username.
        TEST IS PASSED!!!
        """
        data = dict(username='testos',
                    email='test@gmail.com',
                    password='test2020')
        response = self.client.post('/rest-auth/login/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("Unable to log in with provided credentials.", response.content.decode('utf-8'))


class UserLogOutTestAPI(APITestCase):
    """
    TEST IS PASSED!!!
    """
    def setUp(self) -> None:
        self.client = APIClient()
        user = User.objects.create(username='test', email='test@gmail.com')
        user.set_password(raw_password='test2020')
        user.save()
        # login
        data = dict(username='test',
                    email='test@gmail.com',
                    password='test2020')
        self.client.post('/rest-auth/login/', data, format='json')

    def test_user_login_ok(self):
        """
        Ensure that user can logout.
        TEST IS PASSED!!!
        """
        response = self.client.post('/rest-auth/logout/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Successfully logged out.", response.content.decode('utf-8'))