from django.test import TestCase
from django.test import Client

from django.contrib.auth.models import User


class UserTestSignupCase(TestCase):
    """
    Check different situations when an user try to sign up:
        1) username is already exist;
        2) password1 and password2 is not matched;
        3) all data for singing up is correct.
    TEST IS PASSED!!!
    """
    def setUp(self) -> None:
        self.user_data = dict(username='test',
                              username_wrong='testos',
                              email='test@gmail.com',
                              password='passwordOK',
                              password_wrong='passwordWRONG')
        self.client = Client()

    def test_signup_with_different_password(self):
        # checking what will be if password1 != password2 when user register
        response = self.client.post('http://127.0.0.1:8000/accounts/signup/', dict(
            username=self.user_data['username'],
            email=self.user_data['email'],
            password1=self.user_data['password'],
            password2=self.user_data['password_wrong'],
        ))

        # should get status 200, not 500
        self.assertEquals(response.status_code, 200)
        # if password1 != password2 message "You must type the same password each time." should be displayed
        self.assertIn("You must type the same password each time.", response.content.decode('utf-8'))

    def test_signup_with_exits_user(self):
        # create a user which will have the same username
        exist_user = User.objects.create(username=self.user_data['username'])

        response = self.client.post('http://127.0.0.1:8000/accounts/signup/', dict(
            username=self.user_data['username'],
            email=self.user_data['email'],
            password1=self.user_data['password'],
            password2=self.user_data['password'],
        ))

        # should get status 200, not 500
        self.assertEquals(response.status_code, 200)
        self.assertIn("A user with that username already exists.", response.content.decode('utf-8'))

    def test_signup_works_correct(self):
        response = self.client.post('http://127.0.0.1:8000/accounts/signup/', dict(
            username=self.user_data['username'],
            email=self.user_data['email'],
            password1=self.user_data['password'],
            password2=self.user_data['password'],
        ))

        # after successful registration should get status 302 and redirect to home page
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, '/')
        # in DB should be one user
        self.assertEquals(User.objects.count(), 1)


class UserTestLoginCase(TestCase):
    """
    Check different situations when an user try to login:
        1) input wrong password;
        2) input wrong username;
        3) all data for login is correct.
    TEST IS PASSED!!!
    """

    def setUp(self) -> None:
        self.user_data = dict(username='test',
                              username_wrong='testos',
                              email='test@gmail.com',
                              password='passwordOK',
                              password_wrong='passwordWRONG')
        user = User.objects.create(username=self.user_data['username'])
        user.set_password(raw_password=self.user_data['password'])
        user.save()
        self.client = Client()

    def test_login_with_wrong_password(self):
        # login
        response = self.client.post('http://127.0.0.1:8000/accounts/login/', dict(
            login=self.user_data['username'],
            password=self.user_data['password_wrong'],
        ))
        # after wrong login's data should get status 200 and error message
        self.assertEquals(response.status_code, 200)
        self.assertIn("The username and/or password you specified are not correct.", response.content.decode('utf-8'))

    def test_login_with_wrong_username(self):
        # login
        response = self.client.post('http://127.0.0.1:8000/accounts/login/', dict(
            login=self.user_data['username_wrong'],
            password=self.user_data['password'],
        ))

        # after wrong login's data should get status 200 and error message
        self.assertEquals(response.status_code, 200)
        self.assertIn("The username and/or password you specified are not correct.", response.content.decode('utf-8'))

    def test_login_works_correct(self):
        # QUESTION! AssertionError: 200 != 302
        # login
        response = self.client.post('http://127.0.0.1:8000/accounts/login/', dict(
            login=self.user_data['username'],
            password=self.user_data['password'],
        ))
        # after successful login should get status 302 and redirect to home page, and there is a session
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, '/')
        self.assertTrue(hasattr(self.client.session, 'session_key'))


class UserTestLogoutCase(TestCase):
    """
    Check how logout work.
    TEST IS PASSED!!!
    """
    def setUp(self) -> None:
        self.user_data = dict(username='test',
                              username_wrong='testos',
                              email='test@gmail.com',
                              password='passwordOK',
                              password_wrong='passwordWRONG')
        self.exist_user = User.objects.create(username=self.user_data['username'])
        self.exist_user.set_password(raw_password=self.user_data['password'])
        self.client = Client()
        # login
        self.client.post('http://127.0.0.1:8000/accounts/login/', dict(
            login=self.user_data['username'],
            password=self.user_data['password'],
        ))

    def test_logout_works_correct(self):
        # logout
        response = self.client.post('http://127.0.0.1:8000/accounts/logout/',)

        # after successful login should get status 302 and redirect to home page
        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.url, '/')



