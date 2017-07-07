
	def unstudied_skills(self):
		""" this method enables the user view undone tasks"""
		undone = [task for task in self.skills if task not in self.done_skills]
		print("Hello "+ self.user_name+" :)\nHere are the skills that are still incomplete: ")
		for task in undone:
			num = 1
			print(num+". "+ task)
			num += 1
		return undone


