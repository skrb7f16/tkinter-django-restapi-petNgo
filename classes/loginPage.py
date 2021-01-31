from . import frontPage
from tkinter import *
import requests
import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'a.txt')
myusername=os.path.join(THIS_FOLDER,'username.txt')


class LoginPage:
    def __init__(self,root):
        self.root=root

        #=========textvarialbles==========#
        self.username=StringVar()
        self.password=StringVar()

        self.F1=Label(self.root,text="Welcome to Pet NGO",font=("times new roman",30,"bold"),bg="#4b0082",fg="white",relief=GROOVE)
        self.F1.pack(fill=X)

        F2=LabelFrame(self.root,text="Please Login",font=("arial",15,"bold"),fg="gold",bg="#4b0080",bd=7,relief=GROOVE)
        F2.place(x=200,y=200,relwidth=0.5)
        usernameLabel=Label(F2,text="Username",font="arial 18 bold",bd=4).grid(row=0,column=0)
        usernameEntry=Entry(F2,width=15,font="arial 18 bold",bd=4,relief=SUNKEN,textvariable=self.username).grid(row=0,column=1,sticky="e")
        passwordLabel=Label(F2,text="Password",font="arial 18 bold",bd=4).grid(row=1,column=0,pady=10)
        passwordEntry=Entry(F2,width=15,font="arial 18 bold",bd=4,relief=SUNKEN,textvariable=self.password,show="*").grid(row=1,column=1,pady=10)
        loginButton=Button(F2,width=10,text="Login",font="arial 10 bold",relief=GROOVE,command=self.login).grid(row=2,column=0,sticky="w")
        self.F2=F2
        # self.F1=F1

    def login(self):
        myob={"username": self.username.get(),"password":self.password.get()}
        a=requests.post('https://donation-app-pet.herokuapp.com/auth-token/',json=myob,headers={'Content-type': 'application/json; charset=UTF-8'})
        if(a.status_code==200):
            f=open(my_file,'w')
            f.write(a.json()['token'])
            f.close()
            f=open(myusername,'w')
            f.write(self.username.get())
            f.close()
            self.F2.destroy()
            self.F1.destroy()
            frontPage.FrontPage(self.root)
            

