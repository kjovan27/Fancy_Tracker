# -*- coding: utf-8 -*-
"""
Created on Wed Jul 05 23:45:54 2017

@author: Kidepo# Kiyingi Denis Paul
"""
#import numpy as np
#import pandas as pd
#from scipy import stats, integrate
#import matplotlib.pyplot as plt
#import seaborn as sns
#import matplotlib.pyplot as plt; 

class User():
    allTrainees = []
    
    def __init__(self,name,skills={}):
        
        self.user_name = name
        self.skills =skills
        self.done_skills = []
        
    def view_skills(self):#Add code here
        print (self.skills)
        
    def add_completed_skills(self):#@kidepo
        count = 1
        
        AddedList = self.skills[self.user_name]
        for skill in AddedList :
            print("["+str(count)+"]: {}".format(skill))
            count+=1
        while True:
            chose = raw_input("Enter No. of skill to mark: ('Hit 0 to exit')")
            #make some validations
            if int(chose) != 0:
                
                self.done_skills.append(AddedList[int(chose)-1])
            
                count=1
                for skill in AddedList :
                    if skill in self.done_skills:
                        print("["+str(count)+"]: {}*".format(skill))
                    else:
                        print("["+str(count)+"]: {}".format(skill))
                    count+=1
            elif int(chose) == 0:
                break
            
    def view_completed_skills(self):#Add code here
        print(self.done_skills)
        
    def view_incomplete_skills(self):#Add code here
        Unfinished = set(self.skills[self.user_name])-set(self.done_skills)
        print(Unfinished)
    
    def view_progress(self):#@kjovan27
        percent = (float(len(self.done_skills))/float(len(self.skills[self.user_name])))*100
        
#        print(self.skills[self.user_name])
        print(str(percent)+"%")
        mark = percent//10
        
#        activities = ['Unfinished', 'Completed']
#        slices = [(100-percent),percent]
#        colors = ['r', 'g']
#        plt.pie(slices, labels = activities, colors=colors, 
#                startangle=90, shadow = True, explode = (0, 0),
#                radius = 1.2, autopct = '%1.1f%%')
#        plt.legend()
#        plt.show()
        
      
        
if __name__ == "__main__":
    
    print("Start Tracking your program")
    name = ""
    name  = raw_input("Enter your Name: ")
    print("Enter All your Skills to be studied:(Hit '0' if done)\n")
    
    skill = ""
    count=1
    skillList=[]
    while True:
        skill = raw_input(str(count) +":")
        if skill.isdigit():
            break
        skillList.append(skill)
        count +=1
     
    mySkills = {name:skillList}
    user = User(name,mySkills)
    User.allTrainees.append(user)#Store instances in a List
    
    
    #Menu
    while True:
        print("\n_______Menu_______")
        print("[1]:See Added Skills\n[2]:Mark achieved Skills\n[3]:See achieved Skills\n[4]:View Skills I havent Studied\n[5]:View my progress\n[6]:Create New Account")
        
        choice = input("Enter Choice:")
        
        if int(choice) == 1:
            user.view_skills()   
        elif int(choice) == 2:
            user.add_completed_skills()
        elif int(choice) == 3:
            user.view_completed_skills()
        elif int(choice) == 4:
            user.view_incomplete_skills()
        elif int(choice) == 5:
            user.view_progress()
        elif int(choice) == 0:
            print("Exiting...")
            break
        else:
            print("Please Enter right choice,(Hit '0' to exit)")
    
        
        