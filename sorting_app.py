from tkinter import *
from tkinter import ttk,filedialog,messagebox
import os,shutil


class Sorting_App:
    def __init__(self,root):
        self.root=root
        self.root.title(" ")
        self.root.geometry("1350x900+0+0")
        self.root.config(bg="white")
        self.logo_icon=PhotoImage(file="image/minecraft.png")
        self.root.iconphoto(False,self.logo_icon)
        title=Label(self.root,text="Files Organizing Application",font=("impact",40),bg="#023548",fg="white").place(x=0,y=0,relwidth=1)

        #====================Section1=====================

        self.var_foldername=StringVar()
        select_folder = Label(self.root,text="Select Folder",font=("times new roman",18,"normal"),bg="white").place(x=45,y=105)
        txt_folder_name = Entry(self.root,textvariable=self.var_foldername,font=("times new roman",15),state="readonly").place(x=210,y=105,width="600",height="35")
        select_btn = Button(self.root,text="BROWSE",command=self.browse_function,font=("times new roman",11,"bold"),bg="#262626",fg="white",cursor="hand2",activebackground="#262626",activeforeground="white").place(x=850,y=105,width="120",height="35")
        hr = Label(self.root,bg="#023548").place(x=50,y=160,height=1,width=1250)


        #====================Section2=====================

        #================all extensions===================

        self.image_extensions = ["Image Extensions",".png",".jpg"]
        self.audio_extensions = ["Audio Extensions",".mp3"]
        self.video_extensions = ["Video Extensions",".mp4"]
        self.doc_extensions = ["Document Extensions",".docx",".xlsx",".xls",".pdf",".txt"]

        self.folders={
                'videos' :self.video_extensions,
                'audios' :self.audio_extensions,
                'images' :self.image_extensions,
                'documents' :self.doc_extensions,

            }

        extn = Label(self.root,text="Supported Extensions",font=("times new roman",17,"normal"),bg="white").place(x=45,y=175)
        self.image_box = ttk.Combobox(self.root,values=self.image_extensions,font=("times new roman",11,"bold"),state="readonly",justify="center")
        self.image_box.place(x=110,y=230,width=220,height=30)   
        self.image_box.current(0)

        self.audio_box = ttk.Combobox(self.root,values=self.audio_extensions,font=("times new roman",11,"bold"),state="readonly",justify="center")
        self.audio_box.place(x=410,y=230,width=220,height=30)   
        self.audio_box.current(0)  

        self.video_box = ttk.Combobox(self.root,values=self.video_extensions,font=("times new roman",11,"bold"),state="readonly",justify="center")
        self.video_box.place(x=710,y=230,width=220,height=30)   
        self.video_box.current(0) 

        self.doc_box = ttk.Combobox(self.root,values=self.doc_extensions,font=("times new roman",11,"bold"),state="readonly",justify="center")
        self.doc_box.place(x=1010,y=230,width=220,height=30)   
        self.doc_box.current(0)   


        #======================All ImageIcons======================


        self.image_icon = PhotoImage(file="image/photo.png")
        self.audio_icon = PhotoImage(file="image/music.png")
        self.video_icon = PhotoImage(file="image/media.png")
        self.document_icon = PhotoImage(file="image/docs.png")
        self.other_icon = PhotoImage(file="image/questions.png")

        Frame1 = Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Frame1.place(x=50,y=320,width=1250,height=300)
        self.lbl_total_files = Label(Frame1,text="Total Files",font=("impact",15),bg="white")
        self.lbl_total_files.place(x=10,y=10)

        self.lbl_total_image = Label(Frame1,bd=1,image=self.image_icon,compound=TOP,font=("impact",12),bg="white",fg="#023548")
        self.lbl_total_image.place(x=10,y=50,width=230,height=240)
        
        self.lbl_total_audio = Label(Frame1,bd=1,image=self.audio_icon,compound=TOP,font=("impact",12),bg="white",fg="#023548")
        self.lbl_total_audio.place(x=260,y=50,width=230,height=240)

        self.lbl_total_video = Label(Frame1,bd=1,image=self.video_icon,compound=TOP,font=("impact",12),bg="white",fg="#023548")
        self.lbl_total_video.place(x=510,y=50,width=230,height=240)

        self.lbl_total_document = Label(Frame1,bd=1,image=self.document_icon,compound=TOP,font=("impact",12),bg="white",fg="#023548")
        self.lbl_total_document.place(x=760,y=50,width=230,height=240)

        self.lbl_total_other = Label(Frame1,bd=1,image=self.other_icon,compound=TOP,font=("impact",12),bg="white",fg="#023548")
        self.lbl_total_other.place(x=1010,y=50,width=230,height=240)


        #==================Section3======================


        self.lbl_status = Label(self.root,text="STATUS",font=("times new roman",15),bg="white")
        self.lbl_status.place(x=110,y=640)
        self.lbl_st_total = Label(self.root,text="",font=("times new roman",13),bg="white",fg="green")
        self.lbl_st_total.place(x=320,y=640)
        self.lbl_st_moved = Label(self.root,text="",font=("times new roman",13),bg="white",fg="blue")
        self.lbl_st_moved.place(x=450,y=640)
        self.lbl_st_left = Label(self.root,text="",font=("times new roman",13),bg="white",fg="orange")
        self.lbl_st_left.place(x=600,y=640)

        #=================Buttons========================

        self.clear_btn = Button(self.root,text="CLEAR",command=self.clear,font=("times new roman",11,"bold"),bg="#607d8b",fg="white",cursor="hand2",activebackground="#607d8b",activeforeground="white")
        self.clear_btn.place(x=850,y=640,width=180,height=35)
        self.start_btn = Button(self.root,state=DISABLED,text="START",command=self.start_function,font=("times new roman",11,"bold"),bg="#ff5722",fg="white",cursor="hand2",activebackground="#ff5722",activeforeground="white")
        self.start_btn.place(x=1050,y=640,width=180,height=35)


    def Total_count(self):
        images = 0
        audios = 0
        videos = 0
        documents = 0
        others = 0
        self.count = 0
        combine_list = []
        for i in self.all_files:
            if os.path.isfile(os.path.join(self.directry,i))==True:
                self.count+=1
                ext = "."+i.split(".")[-1]
                for folder_name in self.folders.items():
                    for x in folder_name[1]:
                        combine_list.append(x)
                    if ext.lower() in folder_name[1] and folder_name[0] == "images":
                        images+=1
                    if ext.lower() in folder_name[1] and folder_name[0] == "audios":
                        audios+=1
                    if ext.lower() in folder_name[1] and folder_name[0] == "videos":
                        videos+=1
                    if ext.lower() in folder_name[1] and folder_name[0] == "documents":
                        documents+=1

        #===================for calculating other files===========================

        for i in self.all_files:
            if os.path.isfile(os.path.join(self.directry,i))==True:
                ext = "."+i.split(".")[-1]
                if ext.lower() not in combine_list:                        
                    others+=1
                    

        self.lbl_total_image.config(text="Total Images\n"+str(images))
        self.lbl_total_audio.config(text="Total Audios\n"+str(audios))
        self.lbl_total_video.config(text="Total Videos\n"+str(videos))
        self.lbl_total_document.config(text="Total Documents\n"+str(documents))
        self.lbl_total_other.config(text="Other Files\n"+str(others))
        self.lbl_total_files.config(text="Total Files : "+str(self.count))



    
    def browse_function(self):
        op = filedialog.askdirectory(title="SELECT FOLDER FOR ORGANIZING FILES")  
        if op!=None:
            self.var_foldername.set(str(op))         
            self.directry = self.var_foldername.get()
            self.other_name = "others"
            self.rename_folder()
            self.all_files = os.listdir(self.directry)
            length = len(self.all_files)
            count=1
            self.Total_count()
            self.start_btn.config(state=NORMAL)

    def start_function(self):
        self.clear_btn.config(state=DISABLED)
        if self.var_foldername.get()!="":
            c=0
            for i in self.all_files:
                if os.path.isfile(os.path.join(self.directry,i))==True:      
                    c+=1   
                    self.create_move(i.split(".")[-1],i)
                    self.lbl_st_total.config(text="TOTAL : "+str(self.count))
                    self.lbl_st_moved.config(text="MOVED : "+str(c))
                    self.lbl_st_left.config(text="LEFT : "+str(self.count-c))

                    self.lbl_st_total.update()
                    self.lbl_st_moved.update()
                    self.lbl_st_left.update()

                    
            messagebox.showinfo("Success","All Files Has moved Successfully")
            self.start_btn.config(state=DISABLED)
            self.clear_btn.config(state=NORMAL)
        else:
            messagebox.showerror("Error","Please Select Folder")

    def clear(self):
        self.start_btn.config(state=DISABLED)
        self.var_foldername.set("")
        self.lbl_st_total.config(text="")
        self.lbl_st_moved.config(text="")
        self.lbl_st_left.config(text="")
        self.lbl_total_image.config(text="")
        self.lbl_total_audio.config(text="")
        self.lbl_total_video.config(text="")
        self.lbl_total_document.config(text="")
        self.lbl_total_other.config(text="")
        self.lbl_total_files.config(text="Total Files")

    def rename_folder(self):
        for folder in os.listdir(self.directry):
            if os.path.isdir(os.path.join(self.directry,folder))==True:
                os.rename(os.path.join(self.directry,folder),os.path.join(self.directry,folder.lower()))


    def create_move(self,ext,filename):
        find=False
        for folder_name in self.folders:
            if "."+ext in self.folders[folder_name]:
                if folder_name not in os.listdir(self.directry):
                    os.mkdir(os.path.join(self.directry,folder_name))
                shutil.move(os.path.join(self.directry,filename),os.path.join(self.directry,folder_name))
                find=True
                break
        if find!=True:
            if self.other_name not in os.listdir(self.directry):
                os.mkdir(os.path.join(self.directry,self.other_name))
            shutil.move(os.path.join(self.directry,filename),os.path.join(self.directry,self.other_name))




root=Tk() 
obj=Sorting_App(root)
root.mainloop()