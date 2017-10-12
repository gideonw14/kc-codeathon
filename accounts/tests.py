import re
from django.test import TestCase, Client, RequestFactory
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.utils import timezone
from django.urls import reverse
from .models import Profile

"""
Notes:
anon = anonymous
authed = authenticated
"""

class _BaseViewTests(TestCase):
    def setUp(self):
        self.c = Client()
        self.u = "test_admin"
        self.e = "test@123.nowhere"
        self.p = "Sooper_Secret1234"
        self.f = "Test"
        self.l = "Admin"
        self.factory = RequestFactory()
        self.create_test_user()

    # -----------------------------------
    #       Helper Functions for Tests
    # -----------------------------------
    # Helper function to create a mock user
    def create_test_user(self):
        user = User.objects.create_user(username=self.u, password=self.p)
        user.email = self.e
        user.first_name = self.f
        user.last_name = self.l
        user.save()
        profile = Profile()
        profile.activation_key = '123'
        profile.key_expires = timezone.now()
        profile.user = user
        profile.save()

    # Helper function to login said mock user
    def login_test_user(self):
        self.c.post(reverse('accounts:login'), {'username': self.u,
                                                'password': self.p})
        return User.objects.get(username=self.u)

    # Returns a list of users that are currently logged in
    def get_all_logged_in_users(self):
        # Query all non-expired sessions
        sessions = Session.objects.filter(expire_date__gte=timezone.now())
        uid_list = []

        # Build a list of user ids from that query
        for session in sessions:
            data = session.get_decoded()
            uid_list.append(data.get('_auth_user_id', None))

        # Query all logged in users based on id list
        return User.objects.filter(id__in=uid_list)

class LoginRequiredTests(_BaseViewTests):
    def test_true_is_true(self):
        self.assertTrue(True)

    def test_redirect_to_login_when_login_required(self):
        response = self.c.get(reverse('accounts:edit'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual("{}?next={}".format(reverse('accounts:login'),
                                             reverse('accounts:edit')),
                         response.url)

        response = self.c.get(reverse('accounts:profile'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual("{}?next={}".format(reverse('accounts:login'),
                                             reverse('accounts:profile')),
                         response.url)

        response = self.c.get(reverse('accounts:change_password'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual("{}?next={}".format(reverse('accounts:login'),
                                             reverse('accounts:change_password')),
                         response.url)

    def test_can_access_with_login_when_login_required(self):
        self.login_test_user()
        response = self.c.get(reverse('accounts:edit'))
        self.assertEqual(response.status_code, 200)
        response = self.c.get(reverse('accounts:profile'))
        self.assertEqual(response.status_code, 200)
        response = self.c.get(reverse('accounts:change_password'))
        self.assertEqual(response.status_code, 200)

class IndexViewTests(_BaseViewTests):
    def test_index_with_anon_user(self):
        response = self.c.get(reverse('index'))
        self.assertIn("Log in", str(response.content))
        self.assertIn("Register", str(response.content))
        self.assertNotIn("Log out", str(response.content))

    def test_index_with_authed_user(self):
        self.login_test_user()
        response = self.c.get(reverse('index'))
        self.assertNotIn("Log in", str(response.content))
        self.assertNotIn("Register", str(response.content))
        self.assertIn("Log out", str(response.content))

class RegisterViewTests(_BaseViewTests):
    def setUp(self):
        super(RegisterViewTests, self).setUp()
        self.password = "Password123!"
        self.new_account = {
            'username': "my_user",
            'password1': self.password,
            'password2': self.password,
            'email': "email@123.nowhere",
            'first_name': "Some",
            'last_name': "Guy"
        }
    def post_new_user(self):
        self.c.post(reverse('accounts:register'), self.new_account)
        return User.objects.filter(username=self.new_account['username']).get()

    def test_authed_user_redirect(self):
        self.login_test_user()
        response = self.c.get(reverse('accounts:register'))
        self.assertEqual(response.status_code, 302,
                         "Auth'ed users don't need to see register")

    def test_correct_input(self):
        user = self.post_new_user()
        self.assertEqual(User.objects.count(), 3, "We have a 'test_admin' in the setup, and default 'anon_user'")
        user = User.objects.get(username=user.username)
        self.assertEqual(user.username, self.new_account['username'])
        self.assertEqual(user.first_name, self.new_account['first_name'])

    def test_account_activate(self):
        user = self.post_new_user()
        profile = Profile.objects.get(user=user)
        response = self.c.get(reverse('accounts:activation', kwargs={'key': profile.activation_key}))
        self.assertEqual(response.url, reverse('accounts:login'))
        user = User.objects.get(id=user.id)
        self.assertTrue(user.is_active)

    def test_input_existing_user(self):
        self.new_account['username'] = self.u
        response = self.c.post(reverse('accounts:register'), self.new_account)
        self.assertEqual(response.status_code, 200, "Stay on page if failed input")
        self.assertIn("This username is already", str(response.content),
                      "Error should display if username is already taken.")

    def test_input_different_passwords(self):
        self.new_account['password2'] += "fail"
        response = self.c.post(reverse('accounts:register'), self.new_account)
        self.assertEqual(response.status_code, 200, "Stay on page if failed input.")
        self.assertIn("The two password fields didn", str(response.content),
                      "Error should display if passwords don't match.")

    def test_input_existing_email(self):
        self.new_account['email'] = self.e
        response = self.c.post(reverse('accounts:register'), self.new_account)
        self.assertEqual(response.status_code, 200, "Stay on page if failed input.")
        self.assertIn("This email is already", str(response.content),
                      "Error should display if email is already in use.")

    def test_form_fields_are_there(self):
        response = self.c.get(reverse('accounts:register'))
        result = re.findall('<input', str(response.content))
        self.assertEqual(len(result), 7, "6 inputs + hidden csrf token = 7")

class LoginUserTests(_BaseViewTests):
    def test_user_login_with_wrong_pass(self):
        response = self.c.post(reverse('accounts:login'),
                               {'username': self.u, 'password': "Wrong_Password"})
        self.assertEqual(response.status_code, 200, "Stay on login page")
        self.assertIn("Please enter a correct username and password",
                      str(response.content), "If login fails, an error should appear")

    def test_user_login_correct_input(self):
        response = self.c.post(reverse('accounts:login'), {'username': self.u,
                                                             'password': self.p})
        self.assertEqual(response.url, reverse('accounts:profile'),
                         "Will redirect to user profile")
        response = self.c.get(reverse('accounts:profile'))
        self.assertEqual(response.status_code, 200, "Logged in user can reach profile")

class UserChangePasswordTests(_BaseViewTests):
    def setUp(self):
        super(UserChangePasswordTests, self).setUp()
        self.new_password = "MyNewPassword123"
        self.pass_data = {
            'old_password': self.p,
            'new_password1': self.new_password,
            'new_password2': self.new_password
        }

    def test_correct_input(self):
        self.login_test_user()
        response = self.c.post(reverse('accounts:change_password'), self.pass_data)
        self.assertEqual(response.url, reverse('accounts:profile'),
                         "Should redirect to profile")

    def test_incorrect_input(self):
        self.pass_data['new_password2'] += "4"
        self.login_test_user()
        response = self.c.post(reverse('accounts:change_password'), self.pass_data)
        self.assertEqual(response.status_code, 200, "Should stay on same page")
        self.assertIn("The two password fields didn", str(response.content),
                      "Error message should display")

class EditProfileTest(_BaseViewTests):
    def setUp(self):
        super(EditProfileTest, self).setUp()
        self.new_info = {
            'first_name': "Different",
            'last_name': "Guy",
            'email': "newemail@123.nowhere"
        }
        self.same_info = {
            'first_name': self.f,
            'last_name': self.l,
            'email': self.e
        }

    def test_correct_input(self):
        self.login_test_user()
        response = self.c.post(reverse('accounts:edit'), self.new_info)
        self.assertEqual(response.url, reverse('accounts:register_done'),
                         "Redirect to register done page")
        test_admin = User.objects.get(username=self.u)
        self.assertEqual(self.new_info['first_name'], test_admin.first_name)
        self.assertEqual(self.new_info['last_name'], test_admin.last_name)
        self.assertEqual(self.new_info['email'], test_admin.email)

    def test_no_change(self):
        self.login_test_user()
        response = self.c.post(reverse('accounts:edit'), self.same_info)
        test_admin = User.objects.get(username=self.u)
        self.assertEqual(self.same_info['first_name'], test_admin.first_name)
        self.assertEqual(self.same_info['last_name'], test_admin.last_name)
        self.assertEqual(self.same_info['email'], test_admin.email)
        self.assertEqual(response.url, reverse('accounts:profile'))