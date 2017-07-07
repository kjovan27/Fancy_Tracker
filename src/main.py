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
    def add_completed_skills(self):#@kidepo
        count = 1
        
        allSkillList = self.skills
        for skill in allSkillList :
            print("["+str(count)+"]: {}".format(skill))
            count+=1
        while True:
            chose = input("Enter No. of skill to mark ('Hit 0 to exit'): ")
            
            if int(chose) != 0 and int(chose)<=len(allSkillList):
                print('im good')
                
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
                
    def unstudied_skills(self):
        """ this method enables the user view undone tasks"""
        undone = [task for task in self.skills if task not in self.done_skills]
        print("Hello "+ str(self.user_name)+" :)\nHere are the skills that are still incomplete: ")
        for task in undone:
                num = 1
                print("["+str(num)+"]:"+ str(task))
                num += 1   
                
    def view_progress(self):
        progress_percentage = (float(len(self.done_skills))/float(len(self.skills))) * 100
        print ( str(progress_percentage) + "%")


      
        
if __name__ == "__main__":
    
    print("Start Tracking your program")
    name = ""
    name  = input("Enter your Name: ")
    print("Enter All your Skills to be studied:(Hit '0' if done)\n")
    
    skill = ""
    count=1
    skillList=[]
    while True:
        skill = input(str(count) +":")
        if skill.isdigit():
            break
        skillList.append(skill)
        count +=1
     
    #Adding user
    newUser = User(name)
    newUser.add_skills(skillList)
    User.allUsers.append(newUser)#Store instances in a List

    #Menu
    while True:
        print("\n_______Menu_______")
        print("[1]:See Added Skills\n[2]:Mark achieved Skills\n[3]:See achieved Skills\n[4]:View Skills I havent Studied\n[5]:View my progress\n[6]:Create New Account")
        
        choice = input("Enter Choice:")
        
        if int(choice) is 1:
            #newUser.view_skills()
            print ("")
            
        elif int(choice) == 2:
            newUser.add_completed_skills()
            
        elif int(choice) == 3:
            #newUser.view_completed_skills()
            print("")
        elif int(choice) == 4:
            newUser.unstudied_skills()
            print("")
        elif int(choice) == 5:
            #newUser.view_progress()
            print("")
        elif int(choice) == 0:
            print("Exiting...")
            break
        else:
            print("Please Enter right choice,(Hit '0' to exit)")
