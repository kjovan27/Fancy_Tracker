class User(object):

    def __init__(self, user_name):
        self.user_name = user_name
        self.skills = []
        self.done_skills = []

    def add_skills(self, skills_to_learn):
        if skills_to_learn == None:
            for skill in skills_to_learn:
                if isinstance(skill, str):
                    self.skills.append(skill)
                    
    def add_completed_skills(self):#@kidepo
        count = 1
        #############--- 50%
        allSkillList = self.skills
        for skill in allSkillList :
            print("["+str(count)+"]: {}".format(skill))
            count+=1
        while True:
            chose = input("Enter No. of skill to mark ('Hit 0 to exit'): ")
            #make some validations
            if int(chose) != 0:
                
                self.done_skills.append(allSkillList[int(chose)-1])
            
                count=1
                for skill in allSkillList :
                    if skill in self.done_skills:
                        print("["+str(count)+"]: {}*".format(skill))
                    else:
                        print("["+str(count)+"]: {}".format(skill))
                    count+=1
            elif int(chose) == 0:
                break
