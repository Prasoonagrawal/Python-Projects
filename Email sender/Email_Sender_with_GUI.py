from functools import partial
import tkinter as tk
import smtplib
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk



def mailsend():

    user_name=(str(user_Id.get()))
    user_password = (str(user_pass.get()))
    sender_name = (str(user_Id.get()))
    message_sent=(str(message_main.get()))

    print(message_sent)
    print(user_name,user_password,sender_name)

    print("login start")
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user_name, user_password)
    print("login success")
    server.sendmail(user_name, sender_name.split(','),message_sent)
    print("Email sent")
    server.close()


root=tk.Tk()
canvas1=tk.Canvas(root,width=600,height=500)
canvas1.pack()
canvas1.config(bg="red")
label1 = tk.Label(root, text='Email-Sender',bg="yellow")
label1.config(font=('helvetica', 14))
canvas1.create_window(300, 25, window=label1)



label2 = tk.Label(root, text='Ennter sender Email',bg="yellow")
label2.config(font=('helvetica', 10))
canvas1.create_window(70, 90, window=label2)

user_Id=StringVar()
e1 = tk.Entry(root, textvariable=user_Id )
canvas1.create_window(200,90, window=e1)

label2 = tk.Label(root, text='Enter password',bg="yellow")
label2.config(font=('helvetica', 10))
canvas1.create_window(70, 150, window=label2)

user_pass=StringVar()
e2 = tk.Entry(root, textvariable=user_pass)
canvas1.create_window(200,150, window=e2)

label1 = tk.Label(root, text='Compose Mail',bg="yellow")
label1.config(font=('helvetica', 14))
canvas1.create_window(300, 190, window=label1)

label2 = tk.Label(root, text='reciver mail',bg="yellow")
label2.config(font=('helvetica', 10))
canvas1.create_window(70, 240, window=label2)

sender_Id=StringVar()
e3 = tk.Entry(root, textvariable=sender_Id)
canvas1.create_window(200,240, window=e3)

label2 = tk.Label(root, text='Message',bg="yellow")
label2.config(font=('helvetica', 10))
canvas1.create_window(300, 280, window=label2)

message_main=StringVar()
e3 = tk.Entry(root, textvariable=message_main)
canvas1.create_window(300,350, window=e3,width=500,height=100)
#message_main=Text()
#TextArea = Text(root)
#canvas1.create_window(300,350,window=TextArea,width=500,height=100)

button1 = tk.Button(text='Send mail', command=mailsend)
canvas1.create_window(300, 450, window=button1)

#button1.pack(side=tk.RIGHT)
button2 = tk.Button(text='exit', command=quit,bg='pink',height = 1,
          width = 400)

canvas1.create_window(300, 490, window=button2)
root.mainloop()







