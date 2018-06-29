# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 13:48:12 2018

@author: 1804002
"""

class Human:
    def __init__(self,h=0,w=0):
        self.height=h
        self.weight=w
    def BMI(self):
        return self.weight / ((self.height/100)**2)

class Woman(Human):
    def __init__(self,h,w,bust=0,waist=0,hip=0):
        super().__init__(h,w)
        self.bust=bust
        self.waist=waist
        self.hip=hip
    def printBWH(self):
        print("bust={},waist={},hip={}".format(self.bust,self.waist,self.hip))




