from tkinter import *
from .loginPage import LoginPage
from .donation import Donate
from .report import Report

import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'a.txt')


class FrontPage:
    def __init__(self,root):
        self.root=root
        self.root.geometry("800x800+0+0")
        f=open(my_file,"r")
        if f.readline()=='':
            LoginPage(self.root)
            return
        self.F1=Label(self.root,text="Welcome to Pet NGO",font=("times new roman",30,"bold"),bg="#4b0082",fg="white",relief=GROOVE)
        self.F1.pack(fill=X)
        self.F2=LabelFrame(self.root,text="Choose Your Path",font=("arial",15,"bold"),fg="gold",bg="#4b0080",bd=7,relief=GROOVE)
        self.F2.place(x=200,y=200,relwidth=0.5)
        donate=Button(self.F2,width=22,text="Donate",font="arial 20 bold",relief=GROOVE,command=self.donate).grid(row=0,column=0,sticky="e",pady=10)
        report=Button(self.F2,width=22,text="Report",font="arial 20 bold",relief=GROOVE,command=self.report).grid(row=1,column=0,sticky="e",pady=10)

    def donate(self):
        self.F1.destroy()
        self.F2.destroy()
        Donate(self.root)

    def report(self):
        self.F1.destroy()
        self.F2.destroy()
        Report(self.root)



