from tkinter import*
from tkinter import ttk
import tkinter
from PIL import Image,ImageTk
import PIL
from student import Student 
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
from chatbot import ChatBot



class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x790+0+0")
        self.root.title("face Recognition System")
#first image
        img=Image.open("f1.jpg")
        img=img.resize((400,130),PIL.Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=400,height=130)

#second image
        img1=Image.open("f2.jpg")
        img1=img1.resize((450,130),PIL.Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=400,y=0,width=450,height=130)

#third image
        img2=Image.open("pic11.jpg")
        img2=img2.resize((500,130),PIL.Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=850,y=0,width=500,height=130)

#background image
        img3=Image.open("fbg.jpg")
        img3=img3.resize((1400,660),PIL.Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1400,height=660) 

        title_lbl=Label(bg_img,text="Student Attendance  by Using Face Recognition ",font=("times new Roman",35,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1400,height=45)

#student button
        img4=Image.open("f4.jpg")
        img4=img4.resize((150,150),PIL.Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=150,y=100,width=150,height=150)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",12,"bold"),bg="blue")
        b1_1.place(x=150,y=250,width=150,height=25)

#detect face
        img5=Image.open("f5.jpg")
        img5=img5.resize((150,150),PIL.Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
        b1.place(x=400,y=100,width=150,height=150)

        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",12,"bold"),bg="blue")
        b1_1.place(x=400,y=250,width=150,height=25)


#Attendance face button
        img6=Image.open("f6.jpg")
        img6=img6.resize((150,150),PIL.Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
        b1.place(x=650,y=100,width=150,height=150)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",12,"bold"),bg="blue")
        b1_1.place(x=650,y=250,width=150,height=25)

#Help face button
        img7=Image.open("f7.jpg")
        img7=img7.resize((150,150),PIL.Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.chatbot)
        b1.place(x=900,y=100,width=150,height=150)
        b1_1=Button(bg_img,text="Help",cursor="hand2",command=self.chatbot,font=("times new roman",12,"bold"),bg="blue")
        b1_1.place(x=900,y=250,width=150,height=25)

#Train face button
        img8=Image.open("pic3.jpg")
        img8=img8.resize((150,150),PIL.Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=150,y=320,width=150,height=150)
        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",12,"bold"),bg="blue")
        b1_1.place(x=150,y=470,width=150,height=25)

#photos face button
        img9=Image.open("f3.jpg")
        img9=img9.resize((150,150),PIL.Image.Resampling.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=400,y=320,width=150,height=150)
        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",12,"bold"),bg="blue")
        b1_1.place(x=400,y=470,width=150,height=25)

#Developer button
        img10=Image.open("f10.png")
        img10=img10.resize((150,150),PIL.Image.Resampling.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
        b1.place(x=650,y=320,width=150,height=150)
        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",12,"bold"),bg="blue")
        b1_1.place(x=650,y=470,width=150,height=25)

#Exit button
        img11=Image.open("f11.jpg")
        img11=img11.resize((150,150),PIL.Image.Resampling.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=900,y=320,width=150,height=150)
        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",12,"bold"),bg="blue")
        b1_1.place(x=900,y=470,width=150,height=25)

    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Do you want to exit this project",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return
            


        #functions button
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)


    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)  

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)    

    def chatbot(self):
        self.new_window=Toplevel(self.root)
        self.app=ChatBot(self.new_window)    
            




         
if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
   
    