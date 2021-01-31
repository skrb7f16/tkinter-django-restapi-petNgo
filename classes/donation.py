from tkinter import *
from tkinter import messagebox
import requests
from tkinter.scrolledtext import ScrolledText

import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'a.txt')







class Donate:
    def __init__(self,root):
        self.root=root
        self.allDonations=[]

        #==========variables======#
        self.money=StringVar()

        self.F1=Label(self.root,text="Welcome to Pet NGO",font=("times new roman",30,"bold"),bg="#4b0082",fg="white",relief=GROOVE)
        self.F1.pack(fill=X)
        self.F2=LabelFrame(self.root,text="Donations",font=("arial 18 bold"),fg="gold",bg="#4b0080",relief=GROOVE)
        self.F2.place(x=100,y=150,relwidth=0.8)
        moneyLabel=Label(self.F2,text="Money",font="arial 18 bold",bd=4).grid(row=0,column=0,padx=10)
        moneyEntry=Entry(self.F2,width=15,font="arial 18 bold",bd=4,relief=SUNKEN,textvariable=self.money).grid(row=0,column=1,padx=10)
        donateButton=Button(self.F2,width=15,font="arial 15 bold",text="Donate",relief=GROOVE,command=self.donateMoney).grid(row=0,column=2,padx=10)
        self.makeF3()
        self.loadAllDonations()
        
    def donateMoney(self):
        if(self.money.get()==''or not str.isdigit(self.money.get())):
            self.money.set('')
            messagebox.showwarning("Type error","Your either didnt put any money or its not a valid amount")
            return
        myob={"amount":self.money.get()}
        f=open(my_file,'r')
        token=f.readline()
        f.close()
        a=requests.post('https://donation-app-pet.herokuapp.com/api/user/donations',json=myob,headers={"Content-Type": "application/json","Authorization": 'token {}'.format(token)})
        if(a.status_code==201):
            self.money.set('')
            self.F3.destroy()
            self.allDonations=[]
            self.makeF3()
            self.loadAllDonations()
            messagebox.showinfo("Success",a.json()['msg'])

        
    def loadAllDonations(self):
        f=open(my_file,'r')
        token=f.readline()
        f.close()
        a= requests.get('https://donation-app-pet.herokuapp.com/api/user/donations',headers={"Content-Type": "application/json","Authorization": 'token {}'.format(token)})
        self.allDonations=a.json()
        i=0
        for j in self.allDonations:
            self.make(j)

    
    def make(self,obj):
        temp=LabelFrame(self.F3,fg="gold",bg="#4b0080",text=obj['doneOn'].split('T')[0])
        temp.pack(fill=X,pady=10)
        temp1=Label(temp,text="Done a generaous donation of "+str(obj['amount']),fg="white",bg="#4b0080",font=("arial 20 bold")).pack(fill=X)
        temp2=Label(temp,text="At "+obj['doneOn'].split('T')[1].split('.')[0],fg="white",bg="#4b0080",font=("arial 18 italic")).pack(fill=X)
        self.F3.window_create(END, window=temp)
        self.F3.insert(END,'\n')


    def makeF3(self):
        self.F3=ScrolledText(self.root,bg="#4b0080")
        self.F3.place(x=100,y=300,relwidth=0.8,relheight=0.5)
        self.F3.configure(state=DISABLED)

        







