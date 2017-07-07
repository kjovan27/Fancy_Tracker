from main import User
from unittest import TestCase


class TestUserClass(TestCase):

    def setUp(self):
        try:
            self.new_user = User("Thegaijin")
        except NameError as e:
            raise 'Check the class name and try again'

    def test_User_instance(self):
        self.assertIsInstance(
            self.new_user, User, msg='The object should be an instance of the User class')

    def test_number_of_arguments_passed_to_object(self):
        self.assertRaises(TypeError, self.new_user, 'Thegaijin')

    def test_argument_data_types_for_User(self):
        self.assertIsInstance(
            self.new_user.user_name, str, msg="Argument should be a string")

    def test_if_class_has_add_skills_method(self):
        getattr(User, 'add_skills', 'None')

    def test_argument_data_types_for_add_skills_function(self):
        add_skills_call = self.new_user.add_skills(['Python', 'JavaScript'])
        self.assertEqual(type(add_skills_call), list)
