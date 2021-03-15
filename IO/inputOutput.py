# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 16:44:00 2021

@author: GL503GE
"""
print("Creating simple txt file!")

fileTxt = open("part1.txt", "w+")
for i in range(3):
    fileTxt.write("This line {idx} \n".format(idx = i+1))
fileTxt.close()