from tkinter import *
from tkinter import font
from tkinter import ttk
from PIL import ImageTk,Image
import random
from tkinter import messagebox
w=Tk()
w.geometry('450x450')
w.resizable(False,False)
w.title('games')
f1=font.Font(w,family="Inter",size=14)
f2=font.Font(w,family="Inter Display",size=20)

img=Image.open(r"C:\Users\hp\Pictures\images.jpg")
img=img.resize((175,175))
scissors=ImageTk.PhotoImage(img)

img1=Image.open(r"C:\Users\hp\Pictures\paper.jpg")
img1=img1.resize((175,175))
paper=ImageTk.PhotoImage(img1)

img2=Image.open(r"C:\Users\hp\Pictures\rock.jpg")
img2=img2.resize((175,175))
rock=ImageTk.PhotoImage(img2)

pick=[rock,paper,scissors]
com=random.randint(0,2)
l1=Label(w,image=pick[com],font=f2).grid(row=0,column=0,padx=75,pady=25)
def spin():
    com=random.randint(0,2)
    l1=Label(w,image=pick[com],font=f2).grid(row=0,column=0)
    if t1.get()=="rock":
        choice=0
    elif t1.get()=="paper":
        choice=1
    elif t1.get()=="scissors":
        choice=2
    else:
        l2.config(text="Select Your Option!..")

    try:
        if choice==0:
            if com==0:
                l2.config(text="The Match Tie!...")
            elif com==1:
                l2.config(text="You Won")
            else:
                l2.config(text="You lose!...")
        elif choice==1:
            if com==0:
                l2.config(text="You Won!")
            elif com==1:
                l2.config(text="The Match Tie!...")
            else:
                l2.config(text="You Lose!")
        elif choice==2:
            if com==0:
                l2.config(text="You Lose")
            elif com==1:
                l2.config(text="You Won")
            else:
                l2.config(text="The Match Tie!..")
    except:
        messagebox.showinfo("Info","Want to Select an Option!")


b1=Button(w,text="Spin",fg="white",bg="blue",font=f1,width=10,bd=1,command=spin).grid(row=1,column=0,padx=25,pady=20)
t1=ttk.Combobox(w,values=("rock","paper","scissors"),font=f1)
t1.grid(row=2,column=0)
l2=Label(w,text="Let's Play",font=f1)
l2.grid(row=3,column=0,padx=35,pady=20)



w.mainloop()
