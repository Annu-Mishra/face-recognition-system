from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import PIL
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np
from tkinter import filedialog
from sys import path





class Face_Recognition:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x790+0+0")
        self.root.title("face Recognition System")

        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new Roman",25,"bold"),bg="white",fg="black")
        title_lbl.place(x=0,y=0,width=1400,height=45)


       #left image 
        img_top=Image.open("pic114.png")
        img_top=img_top.resize((700,650),PIL.Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=50,width=700,height=650)

      #right image
        img_bottom=Image.open("pic113.png")
        img_bottom=img_bottom.resize((700,650),PIL.Image.Resampling.LANCZOS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=640,y=50,width=700,height=650)

        
        b1_1=Button(self.root,text="Face Recognition",cursor="hand2",command=self.face_recog,font=("times new roman",18,"bold"),bg="white",fg="black")
        b1_1.place(x=560,y=500,width=200,height=40)
        
#Attendance
    def mark_attendance(self,i,r,n,d): 
        file_path = "Attendance.csv"
        if os.path.exists(file_path):
               mode="r"
        else:
               mode="w"
        try:   
           with open(file_path,"r+",newline="\n") as f:
              myDataList=f.readlines()
              name_list=[]
              for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
              if((i not in name_list)) and ((r not in name_list)) and ((n not in name_list)) and ((d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")
        except Exception as e:
            print("error opening",e)



       
####Face  Recognition
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]
            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                roi=gray_image[y:y+h,x:x+w]
                id,predict=clf.predict(roi)
                
                confidence=int((100*(1-predict/300)))

                conn=mysql.connector.connect(host="localhost",username="root",password="mishra@120503",database="face_recognition")
                my_cursor=conn.cursor()

                my_cursor.execute("select Name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)
                # n=n[0]

                my_cursor.execute("select Roll from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)
                # r=r[0]

                my_cursor.execute("select dep from student where Student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)
                # d=d[0]

                my_cursor.execute("select Student_id from student where Student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)
                # i=i[0]
                

                    

                if confidence <77:
                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(64,15,223),2)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255),2)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face - Confidence: {}".format(confidence),(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255),0)
                coord=[x,y,w,h]

            return coord
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        faceCascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read('classifier.xml')

        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=cv2.flip(img,1)
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To Face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()






        


if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()        