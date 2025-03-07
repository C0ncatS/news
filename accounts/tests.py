from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class UsersManagersTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="test1234",
        )
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testuser@example.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        superuser = User.objects.create_superuser(
            username="testsuperuser",
            email="testsuperuser@example.com",
            password="testpass1234",
        )
        self.assertEqual(superuser.username, "testsuperuser")
        self.assertEqual(superuser.email, "testsuperuser@example.com")
        self.assertTrue(superuser.is_active)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)


class SignupPageTests(TestCase):
    def test_url_exists_at_correct_location_signupview(self):
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)

    def test_signup_view_name(self):
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/signup.html")

    def test_signup_form(self):
        response = self.client.post(
            reverse("signup"),
            {
                "username": "testuser",
                "email": "testuser@example.com",
                "password1": "testpass123",
                "password2": "testpass123",
            },
        )
        User = get_user_model()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(User.objects.all().count(), 1)
        self.assertEqual(User.objects.last().username, "testuser")
        self.assertEqual(User.objects.last().email, "testuser@example.com")
