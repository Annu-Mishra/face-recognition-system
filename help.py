from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import PIL
from tkinter import messagebox
import mysql.connector
import cv2

# from student import Student



class  Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x790+0+0")
        self.root.title("face Recognition System")

        title_lbl=Label(self.root,text="HELP DESK ",font=("times new Roman",25,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1400,height=45)

        img_top=Image.open("f7.jpg")
        img_top=img_top.resize((1400,720),PIL.Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1400,height=720)

        dev_label=Label(f_lbl,text="Email : annu120503@gmail.com",font=("times new roman",16,"bold"),fg="black")
        dev_label.place(x=550,y=170)

        dev_label2=Label(f_lbl,text="Email : abhi170703@gmail.com",font=("times new roman",16,"bold"),fg="black")
        dev_label2.place(x=550,y=200)

        dev_label3=Label(f_lbl,text="Email : ayush200903@gmail.com",font=("times new roman",16,"bold"),fg="black")
        dev_label3.place(x=550,y=230)

        


if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()