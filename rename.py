#!/usr/bin/python3
import os

def rename():
    path=#'replace your own path'
    i = 0
    for file in os.listdir(path):  
        if os.path.isfile(os.path.join(path,file))==True:  
            i+=1
            filename = os.path.splitext(file)[0]
            filetype = os.path.splitext(file)[1]
            newname=str(i)+filetype            
            os.rename(os.path.join(path,file),os.path.join(path,newname)) 
            print(newname)
           
rename()
