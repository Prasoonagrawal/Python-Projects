import cv2
import tkinter as tk
from tkinter import *
import numpy as np
from PIL import ImageGrab
import pyautogui as pgi
def screen_recorder():
    root.iconify()
    z=pgi.size()
    fourcc=cv2.VideoWriter_fourcc(*'XVID')
    out=cv2.VideoWriter('output1.avi',fourcc,25.0,z)

    while True:
        img=pgi.screenshot()
        frame=np.array(img)
        frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        out.write(frame)
        cv2.imshow("Recording ", frame)
        if cv2.waitKey(1)==ord("q"):
            break


    cv2.destroyAllWindows()
    out.release()


#screen_recorder()
root=tk.Tk()
canvas1=tk.Canvas(root,width=600,height=500)
canvas1.pack()
canvas1.config(bg="red")
label1 = tk.Label(root, text='Screen recoder',bg="yellow")
label1.config(font=('helvetica', 14))
canvas1.create_window(300, 25, window=label1)

button2 = tk.Button(text='Start Recording', command=screen_recorder,bg='pink',height = 10,
          width = 50)

canvas1.create_window(300, 300, window=button2)

label2 = tk.Label(root, text='To exit please press q after recording start',bg="yellow")
label2.config(font=('helvetica', 14))
canvas1.create_window(300, 180, window=label2)

root.mainloop()
