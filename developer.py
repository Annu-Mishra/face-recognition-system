from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import PIL
from tkinter import messagebox
import mysql.connector
import cv2

# from student import Student



class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x790+0+0")
        self.root.title("face Recognition System")

        title_lbl=Label(self.root,text="DEVELOPER ",font=("times new Roman",25,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1400,height=45)

        img_top=Image.open("pic7.jpg")
        img_top=img_top.resize((1400,720),PIL.Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1400,height=720)

        main_frame=Frame(f_lbl,bd=2)
        main_frame.place(x=850,y=0,width=400,height=450)

        img_top1=Image.open("f4.jpg")
        img_top1=img_top1.resize((100,150),PIL.Image.Resampling.LANCZOS)
        self.photoimg_top1=ImageTk.PhotoImage(img_top1)

        f_lbl=Label(main_frame,image=self.photoimg_top1)
        f_lbl.place(x=300,y=0,width=100,height=150)

        #Developer info
        dev_label=Label(main_frame,text="Hello We are Developers",font=("times new roman",12,"bold"))
        dev_label.place(x=0,y=5)




if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()