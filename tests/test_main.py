from unittest import TestCase
from src.main import User


class TestUserClass(TestCase):

    def setUp(self):
        self.new_user = User("Thegaijin")

    def test_User_instance(self):
        self.assertIsInstance(
            self.new_user, User, msg='The object should be an instance of the User class')

    def test_number_of_arguments_passed_to_object(self):
        self.assertRaises(TypeError, self.new_user, 'Thegaijin')

    def test_argument_data_types_for_User(self):
        self.assertIsInstance(
            self.new_user.user_name, str, msg="Argument should be a string")
