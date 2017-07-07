""" class containing all the methods of the app  """
class User:
    def __init__(self, username):
        self.username = username
        self.skills   = ['reading', 'writing']
        self.done_skills =['reading', 'writing']

    """method for skills studied """
    def view_completd_skills(self):
        if len(self.done_skills) == 0:
            print('No skill has been completed')
        else:
            print('The following skills have been completed:\n')
            for skill in self.done_skills:
                print(skill+'\n')
