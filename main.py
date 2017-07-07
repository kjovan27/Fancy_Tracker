# -*- coding: utf-8 -*-
"""
Created on Fri Jul 07 10:13:53 2017

@author: Don Quan
"""

def view_progress(self):
    
    progress_percentage = (float(len(self.done_skills))/float(len(self.skills))) * 100
    
    return str(progress_percentage + "%")
