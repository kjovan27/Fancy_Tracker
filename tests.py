import unittest
from main import User

class tests_for_undone:
	def test_all_undone_tasks_are_diplayed(self):
		self.skills=["OOP in python","C++", "Java","PHP"]
		self.done_skills =["C++"]
		self.assertEqual(unstudied_skills(),["OOP in python","Java","PHP"],msg = "expected less of more members in the list" )
	def test_undone_is_empty(self):
		self.skills = ["mountain climbing","biking","swimming","jogging"]
		self.done_skills = []
		self.assertEqual(unstudied_skills(),["mountain climbing","biking","swimming","jogging"],msg="no skills done yet, should return the entire skills list")
	def test_both_lists_empty(self):
		self.skills =[]
		self.done_skills=[]
		self.assertEqual(unstudied_skills(),[],msg="No skills added, expected an empty list")

