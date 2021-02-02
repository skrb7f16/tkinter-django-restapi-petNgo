from tkinter import *
from tkinter import messagebox
import requests
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog
import base64
import json

import os,shutil
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'a.txt')
usernameFile=os.path.join(THIS_FOLDER,'username.txt')

class Report:
    def __init__(self,root):
        self.root=root
        f=open(usernameFile,'r')
        self.F1=Label(self.root,text="Welcome to Pet NGO "+f.readline(),font=("times new roman",30,"bold"),bg="#4b0082",fg="white",relief=GROOVE)
        self.F1.pack(fill=X)
        f.close()

        #=========variables=========#
        self.report=StringVar()
        self.type=StringVar()
        self.breed=StringVar()
        self.fileName=StringVar()


        self.F2=LabelFrame(self.root,text="Report about a pet",font=("arial",18,"bold"),fg="gold",bg="#4b0082")
        self.F2.place(x=100,y=60,relwidth=0.8)
        reportLabel=Label(self.F2,text="Report",font="arial 22 bold").grid(row=0,column=0,sticky="n")
        self.reportText=Text(self.F2,width=40,font="arial 18 bold",height=5)
        self.reportText.grid(row=0,column=1)
        typeLabel=Label(self.F2,text="type",font="arial 22 bold").grid(row=1,column=0,)
        typeText=Entry(self.F2,width=40,font="arial 18 bold",textvariable=self.type).grid(row=1,column=1)
        breedLabel=Label(self.F2,text="breed",font="arial 22 bold").grid(row=2,column=0,)
        breedText=Entry(self.F2,width=40,font="arial 18 bold",textvariable=self.breed).grid(row=2,column=1)
        buttonupload=Button(self.F2,text="image", command=self.fileDailog,font="arial 15 bold").grid(row=3,column=0)
        button=Button(self.F2,text="upload",command=self.reportByUser).grid(row=4,column=0)


    def fileDailog(self):
        self.fileName = filedialog.askopenfilename(initialdir = "/", title="Select A File",filetype=(("jpeg","*.jpg"),("png","*.png")))
        self.label = Label(self.F2, text="",font="arial 18 bold",bg="#4b0082",fg="white")
        self.label.grid(column =1,row = 3)
        self.label.configure(text = self.fileName)
        # os.chdir('e:\\')
        # os.system('mkdir BACKUP')
        # shutil.move(self.fileName,'e:\\')




    def reportByUser(self):
        with open(self.fileName,'rb') as f:
            im_bytes=f.read()
        imb64=base64.b64encode(im_bytes).decode('utf-8')
        f=open(my_file,'r')
        token=f.readline()
        f.close()
        headers = {'Content-type': 'application/json',"Authorization": 'token {}'.format(token)}
        self.report=self.reportText.get("1.0",'end-1c')
        payload = {"image": imb64, "report": self.report,"type":self.type.get(),"breed":self.breed.get()}

        response = requests.post('https://donation-app-pet.herokuapp.com/api/user/reports', json=payload, headers=headers)
        print(response.text)





        


        