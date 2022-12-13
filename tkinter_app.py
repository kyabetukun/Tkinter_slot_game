from tkinter import Tk
from tkinter import ttk
import random

root = Tk()
root.title("数字スロットゲーム")

count = random.randint(1,10)
after_id = None

def stop():
  global root
  global after_id
  root.after_cancel(after_id)


def restart(event):
  after_id = root.after(200, repeat_3)
  after_id = root.after(200, repeat_2)
  after_id = root.after(200, repeat_1)
  
def repeat_1():
    global root
    global label_1
    global count
    global after_id
    
    if count == 10:
      count = 0
      after_id = root.after(200, repeat_1)
    else: 
      count += 1
      label_1.config(text=str(count))
      after_id = root.after(200, repeat_1)
      
def repeat_2():
    global root
    global label_2
    global count
    global after_id
    
    if count == 10:
      count = 0
      after_id = root.after(200, repeat_2)
    else: 
      count += 1
      label_2.config(text=str(count))
      after_id = root.after(200, repeat_2)

def repeat_3():
    global root
    global label_3
    global count
    global after_id
    
    if count == 10:
      count = 0
      after_id = root.after(200, repeat_3)
    else: 
      count += 1
      label_3.config(text=str(count))
      after_id = root.after(200, repeat_3)


def label(text,size):
  return ttk.Label(root, text=text, font=("Helvetica",size,"bold"))

def button():
  return ttk.Button(root, text="押せ!", command=stop)
label_1 = label("0",80)
label_2 = label("0",80)
label_3 = label("0",80)
label_4 = label("何かキーを押したらリスタート！！",100)

button_1 = ttk.Button(root, text="押せ!", command=stop)
button_2= ttk.Button(root,text="押せ!", command=stop)
button_3 = ttk.Button(root,text="押せ!", command=stop)

label_1.place(x=80,y=30)
label_2.place(x=220,y=30)
label_3.place(x=360,y=30)
label_4.place(x=100,y=250)

button_1.place(x=60,y=200)
button_2.place(x=200,y=200)
button_3.place(x=340,y=200)

root.bind("<KeyPress>", restart)

repeat_3()
repeat_2()
repeat_1()

root.mainloop()