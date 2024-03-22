from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import PIL

class ChatBot:
    def __init__(self,root):
        self.root=root
        self.root.title("ChatBot")
        self.root.geometry("700x600+0+0")
        self.root.bind('<Return>',self.enter_func)
        
        main_frame=Frame(self.root,bd=4,bg='green',width=610)
        main_frame.pack()

        img_chat=Image.open('chatbot.png')
        img_chat=img_chat.resize((120,50),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img_chat)

        Title_label=Label(main_frame,bd=3,relief=RAISED,anchor="nw",width=700,compound=LEFT,image=self.photoimg,text="CHAT ME",font=('arial',30,'bold'),bg="white",fg="blue")
        Title_label.pack(side=TOP)

        self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text=Text(main_frame,width=65,height=20,bd=3,relief=RAISED,font=('arial',14),yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()

        btn_frame=Frame(self.root,bd=4,bg='white',width=730)
        btn_frame.pack()

        label_1=Label(btn_frame,text="Type Something",font=('arial',14,'bold'),bg="white",fg="blue")
        label_1.grid(row=0,column=0,padx=5,sticky=W)

        self.entry=StringVar()
        self.entry1=ttk.Entry(btn_frame,textvariable=self.entry,width=30,font=('arial',15,'bold'))
        self.entry1.grid(row=0,column=1,padx=5,sticky=W)

        self.send=Button(btn_frame,text="Send>>",command=self.send ,font=('arial',14,'bold'), width=8,bg="green")
        self.send.grid(row=0,column=2,padx=5,sticky=W)
        
        self.clear=Button(btn_frame,text="Clear Data",command=self.clear,font=('arial',12,'bold'), width=8,bg="green",fg='white')
        self.clear.grid(row=1,column=0,padx=5,sticky=W)

        self.msg=''
        self.label_2=Label(btn_frame,text=self.msg,font=('arial',12,'bold'), bg="white",fg='red')
        self.label_2.grid(row=1,column=1,padx=5,sticky=W)

    #=====Function Declaration======
        
    def enter_func(self,event):
        self.send.invoke()
       # self.entry.set('')
        
    def clear(self):
        self.text.delete('1.0',END)
        self.entry.set('')

    def send(self):
        send='\t\t\t'+'You: '+self.entry.get()
        self.text.insert(END,'\n'+send) 
        self.text.yview(END)
        
        if(self.entry.get()==''):
            self.msg='Please enter some input'
            self.label_2.config(text=self.msg,fg='red')

        else:
            self.msg=''
            self.label_2.config(text=self.msg,fg='red')

        if(self.entry.get()=='hello'):
            self.text.insert(END,'\n\n'+'Bot: Hi')

        elif(self.entry.get()=='hi'):
            self.text.insert(END,'\n\n'+'Bot: Hello')

        elif(self.entry.get()=='how are you'):
            self.text.insert(END,'\n\n'+'Bot: fine and you')

        elif(self.entry.get()=='Fantastic'):
            self.text.insert(END,'\n\n'+'Bot: Nice to hear')

        elif(self.entry.get()=='Who created you?'):
            self.text.insert(END,'\n\n'+'Bot: Abhishek,Annu and Ayush.')

        elif(self.entry.get()=='How does face recognition work?'):
            self.text.insert(END,'\n\n'+'Bot: Facial recognition is a way of\nrecognizing a human face throough\ntechnology. A facial recognition\nsystem uses biometric to map\nfacial features from a pic \nor videao. It compres the information\nwith')
        
        elif(self.entry.get()=='how does facial recognition work step by step?'):
            self.text.insert(END,'\n\n'+'Bot: Face Detction. The camera detects and locates the imag of a face,\neither alone or in a crowd. ...\nStep 2: Face analysis. Next,an image of\n the face is captured and analyzed. ...\nStep 3:  ')

        elif(self.entry.get()=='Hoew many countries use facial recognition?'):
            self.text.insert(END,'\n\n'+'Bot: In use 98\nApproved, but not implemented 12\nConsidering facial recognition.')
        
        elif(self.entry.get()=='bye'):
            self.text.insert(END,'\n\n'+'Bot: Thank you for chatting')
        else:
            self.text.insert(END,"\n\n"+"Bot: Sorry I didn't get it")



if __name__=='__main__':
    root=Tk()
    obj=ChatBot(root)
    root.mainloop()
