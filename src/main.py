class User(object):

    def __init__(self, user_name):
        self.user_name = user_name
        self.skills = []
        self.done_skills = []

    def add_skills(self, skills_to_learn):
        if skills_to_learn != None:
            if isinstance(skills_to_learn, list):
                for skill in skills_to_learn:
                    if isinstance(skill, str):
                        self.skills.append(skill)
                return (self.skills)
        else:
            raise TypeError


new = User('Hon')
print(new.add_skills(4))
