from django.test import TestCase
from django.contrib.auth import get_user_model
from authenticate.forms import GroupAdminForm
from django.contrib.auth.models import Group

class UsersManagersTests(TestCase):


    def setUp(self):
        # Group setup
        group_name = "admins"
        self.group = Group(name=group_name)
        self.group.save()

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email='normal@user.com',
                                        password='foo')
        self.assertEqual(user.email, 'normal@user.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password="foo")

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(email='super@user.com',
                                                   password='foo')
        self.assertEqual(admin_user.email, 'super@user.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(admin_user.username)
            self.assertEqual(admin_user.email, str(admin_user.__str__()))
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email='super@user.com', password='foo', is_superuser=False)
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email='super@user.com', password='foo', is_staff=False)


    def test_forms_valid_new(self):
        form_data = {'name': 'test group'}
        form = GroupAdminForm(data=form_data)
        self.assertTrue(form.is_valid())
        

    def test_forms_valid(self):
        form_data = {'name': self.group.name}
        form = GroupAdminForm(data=form_data, instance=self.group)
        self.assertTrue(form.is_valid())
        inst = form.save()
        self.assertEqual(inst, self.group)

    def test_forms_invalid(self):
        form_data = {'name': ''}
        form = GroupAdminForm(data=form_data)
        self.assertFalse(form.is_valid())
            
