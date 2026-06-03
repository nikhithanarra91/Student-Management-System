from tkinter import *
import time
import ttkthemes
from tkinter import ttk,messagebox,filedialog
import pymysql
import pandas
#functionality part

def iexit():
    result=messagebox.askyesno('Confirm','Do you want to exit?')
    if result:
        root.destroy()
    else:
        pass

def export_data():
    url=filedialog.asksaveasfilename(defaultextension='.csv')
    indexing=studentTable.get_children()
    print("Indexing:", indexing)
    print("Number of rows:", len(indexing))
    newlist=[]
    for index in indexing:
        content=studentTable.item(index)
        datalist=content['values']
        newlist.append(datalist)
        
    table=pandas.DataFrame(newlist,columns=['id','Name','Mobile','Email','Address','Gender','DOB','Added Date','Added Time'])
    table.to_csv(url,index=False)
    messagebox.showinfo('Success','Data is saved Successfully')

def toplevel_data(title,button_text,command):
    global idEntry,nameEntry,phoneEntry,addressEntry,emailEntry,genderEntry,dobEntry,screen
    screen=Toplevel()
    screen.title(title)
    screen.grab_set()
    screen.resizable(False,False)
    idLabel=Label(screen,text='ID',font=('times new roman',20,'bold'))
    idLabel.grid(row=0,column=0,padx=30,pady=15,sticky=W)
    idEntry=Entry(screen,font=('roman',15,'bold'),width=24)
    idEntry.grid(row=0,column=1,pady=15,padx=10)
    
    nameLabel=Label(screen,text='Name',font=('times new roman',20,'bold'))
    nameLabel.grid(row=1,column=0,padx=30,pady=15,sticky=W)
    nameEntry=Entry(screen,font=('roman',15,'bold'),width=24)
    nameEntry.grid(row=1,column=1,pady=15,padx=10)
    
    phoneLabel=Label(screen,text='Phone Number',font=('times new roman',20,'bold'))
    phoneLabel.grid(row=2,column=0,padx=30,pady=15,sticky=W)
    phoneEntry=Entry(screen,font=('roman',15,'bold'),width=24)
    phoneEntry.grid(row=2,column=1,pady=15,padx=10)
    
    emailLabel=Label(screen,text='Email',font=('times new roman',20,'bold'))
    emailLabel.grid(row=3,column=0,padx=30,pady=15,sticky=W)
    emailEntry=Entry(screen,font=('roman',15,'bold'),width=24)
    emailEntry.grid(row=3,column=1,pady=15,padx=10)
    
    addressLabel=Label(screen,text='Address',font=('times new roman',20,'bold'))
    addressLabel.grid(row=4,column=0,padx=30,pady=15,sticky=W)
    addressEntry=Entry(screen,font=('roman',15,'bold'),width=24)
    addressEntry.grid(row=4,column=1,pady=15,padx=10)
    
    genderLabel=Label(screen,text='Gender',font=('times new roman',20,'bold'))
    genderLabel.grid(row=5,column=0,padx=30,pady=15,sticky=W)
    genderEntry=Entry(screen,font=('roman',15,'bold'),width=24)
    genderEntry.grid(row=5,column=1,pady=15,padx=10) 
  
    dobLabel=Label(screen,text='D.O.B',font=('times new roman',20,'bold'))
    dobLabel.grid(row=6,column=0,padx=30,pady=15,sticky=W)
    dobEntry=Entry(screen,font=('roman',15,'bold'),width=24)
    dobEntry.grid(row=6,column=1,pady=15,padx=10)
    
    student_button=ttk.Button(screen,text=button_text,command=command)
    student_button.grid(row=7,columnspan=2,pady=15)
    
    if title=='Update Student':
        
        indexing=studentTable.focus()
        
        content=studentTable.item(indexing)
        listdata=content['values']
        idEntry.insert(0,listdata[0])
        nameEntry.insert(0,listdata[1])
        phoneEntry.insert(0,listdata[2])
        emailEntry.insert(0,listdata[3])
        addressEntry.insert(0,listdata[4])
        genderEntry.insert(0,listdata[5])
        dobEntry.insert(0,listdata[6])
    
def update_data():
    query= 'update student set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s, date=%s,time=%s where id=%s'
    mycursor.execute(query,(nameEntry.get(),phoneEntry.get(),emailEntry.get(),addressEntry.get(),genderEntry.get(),dobEntry.get(),date,currenttime,idEntry.get()))
    con.commit()
    messagebox.showinfo('Success',f'Id {idEntry.get()} is modified successfully',parent=screen)
    screen.destroy()
    show_student()
     
def show_student():
    query='select * from student'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    
    for data in fetched_data:
        studentTable.insert('',END,values=data)

def delete_student():
    indeixing=studentTable.focus()
    print(indeixing)
    content=studentTable.item(indeixing)
    content_id=content['values'][0]
    query='delete from student where id=%s'
    mycursor.execute(query,content_id)
    con.commit()
    messagebox.showinfo('Deleted',f'Id {content_id} is deleted succesfully')
    query='select * from student'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    
    for data in fetched_data:
        studentTable.insert('',END,values=data)
    
def search_data():
    query='select * from student where id=%s or name=%s or email=%s or mobile=%s or address=%s or gender=%s or dob=%s'
    mycursor.execute(query,(idEntry.get(),nameEntry.get(),emailEntry.get(),phoneEntry.get(),addressEntry.get(),genderEntry.get(),dobEntry.get()))
    studentTable.delete(*studentTable.get_children())
    fetched_data=mycursor.fetchall()
    
    for data in fetched_data:
        studentTable.insert('',END,values=data)
            
def add_data():
    if idEntry.get()=='' or nameEntry.get()=='' or phoneEntry.get()=='' or emailEntry.get()=='' or addressEntry.get()=='' or genderEntry.get()=='' or dobEntry.get()=='':
        messagebox.showerror('Error', 'All fields are required',parent=screen)
    else:
        
        try:
            
            query='insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(query,(idEntry.get(),nameEntry.get(),phoneEntry.get(),emailEntry.get(),addressEntry.get(),genderEntry.get(),dobEntry.get(),date,currenttime))
            con.commit()
            result=messagebox.askyesno('confirm','Data added successfully. Do you want to clean the form?',parent=screen)
            if result:
                idEntry.delete(0,END)
                nameEntry.delete(0,END)
                phoneEntry.delete(0,END)
                emailEntry.delete(0,END)
                addressEntry.delete(0,END)
                genderEntry.delete(0,END)
                dobEntry.delete(0,END)
            else:
                pass
        except:
            messagebox.showerror('Eror','Id cannot be repeated',parent=screen)
            return
        
        query='select * from student'
        mycursor.execute(query)
        fetched_data=mycursor.fetchall()
        studentTable.delete(*studentTable.get_children())
        for data in fetched_data:
            
            studentTable.insert('',END,values=data)
            
def clock():
    global date,currenttime
    date=time.strftime('%d/%m/%Y')
    currenttime=time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f' Date: {date}\nTime:{currenttime}')
    datetimeLabel.after(1000,clock)
    
def connect_Database():
    def connect():
        global mycursor,con
        try:
           con=pymysql.connect(host=hostEntry.get(),user=usernameEntry.get(),password=passwordEntry.get(),database="studentmanagementsystem")
           mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Invalid Details',parent=connectWindow)   
            return
        try: 
            query='create database studentmanagementsystem'
            mycursor.execute(query)
            query='use studentmanagementsystem'
            mycursor.execute(query)
            query='create table student(id int not null primary key,name varchar(30),mobile varchar(10),email varchar(30),address varchar(100),gender varchar(20),dob varchar(20),date varchar(50),time varchar(50))'
            mycursor.execute(query)
        except:
            query='use studentmanagementsystem'
            mycursor.execute(query)
            messagebox.showinfo('Success','Database Connection is Successful',parent=connectWindow)
            connectWindow.destroy()
        
        addstudentButton.config(state=NORMAL)
        searchstudentButton.config(state=NORMAL)
        updatestudentButton.config(state=NORMAL)
        showstudentButton.config(state=NORMAL)
        exportstudentButton.config(state=NORMAL)
        deletestudentButton.config(state=NORMAL)  
        
                  
    connectWindow=Toplevel()
    connectWindow.grab_set()
    connectWindow.geometry('470x250+730+230')
    connectWindow.title('Database connection')
    connectWindow.resizable(0,0)
    
    hostNameLabel=Label(connectWindow,text="Host Name",font=('arial',20,'bold'))
    hostNameLabel.grid(row=0,column=0,padx=20)
    
    hostEntry=Entry(connectWindow,font=('roman',15,'bold'),bd=2)
    hostEntry.grid(row=0,column=1,padx=40,pady=20)

    userNameLabel=Label(connectWindow,text="User Name",font=('arial',20,'bold'))
    userNameLabel.grid(row=1,column=0,padx=20)
    
    usernameEntry=Entry(connectWindow,font=('roman',15,'bold'),bd=2)
    usernameEntry.grid(row=1,column=1,padx=40,pady=20)
    
    passwordLabel=Label(connectWindow,text="Password",font=('arial',20,'bold'))
    passwordLabel.grid(row=2,column=0,padx=20)
    
    passwordEntry=Entry(connectWindow,font=('roman',15,'bold'),bd=2)
    passwordEntry.grid(row=2,column=1,padx=40,pady=20)
    
    connectButton=ttk.Button(connectWindow,text=('CONNECT'),command=connect)
    connectButton.grid(row=3,columnspan=2)
    
    
#GUI part
root=ttkthemes.ThemedTk()

root.get_themes()

root.set_theme('radiance')

root.geometry("1200x700+0+0")
root.title("Student Management System")
root.resizable(0,0)

datetimeLabel=Label(root,font=("times new roman",18,"bold"))
datetimeLabel.place(x=5,y=5)
clock()
s='Student Management Sysytem'
sliderLabel=Label(root,text=s,font=("arial",28,"italic bold"))
sliderLabel.place(x=350,y=0)

connectButton=ttk.Button(root,text='Connect Database',command=connect_Database)
connectButton.place(x=1000,y=5)

leftFrame=Frame(root)
leftFrame.place(x=50,y=80,width=300,height=600)

logo_image=PhotoImage(file="students.png")
logo_Label=Label(leftFrame,image=logo_image)
logo_Label.grid(row=0,column=0)

addstudentButton=ttk.Button(leftFrame,text='Add Student',width=25,state=DISABLED,command=lambda: toplevel_data('Add Student','Add',add_data))
addstudentButton.grid(row=1,column=0,pady=20)

searchstudentButton=ttk.Button(leftFrame,text='Search Student',width=25,state=DISABLED,command=lambda: toplevel_data('Search Student','Search',search_data))
searchstudentButton.grid(row=2,column=0,pady=20)

deletestudentButton=ttk.Button(leftFrame,text='Delete Student',width=25,state=DISABLED,command=delete_student)
deletestudentButton.grid(row=3,column=0,pady=20)

updatestudentButton=ttk.Button(leftFrame,text='Update Student',width=25,state=DISABLED,command=lambda: toplevel_data('Update Student','Update',update_data))
updatestudentButton.grid(row=4,column=0,pady=20)

showstudentButton=ttk.Button(leftFrame,text='Show Student',width=25,state=DISABLED,command=show_student)
showstudentButton.grid(row=5,column=0,pady=20)

exportstudentButton=ttk.Button(leftFrame,text='Export Data',width=25,state=DISABLED,command=export_data)
exportstudentButton.grid(row=6,column=0,pady=20)

exitstudentButton=ttk.Button(leftFrame,text='Exit',width=25,command=iexit)
exitstudentButton.grid(row=7,column=0,pady=20)

rightFrame=Frame(root,)
rightFrame.place(x=350,y=80,width=820,height=600)

ScrollBarX=Scrollbar(rightFrame,orient=HORIZONTAL)
ScrollBarY=Scrollbar(rightFrame,orient=VERTICAL)

studentTable=ttk.Treeview(rightFrame,columns=('ID','Name','Mobile No','Email','Address','Gender','DOB','Added Date','Added Time'),
                                              xscrollcommand=ScrollBarX.set,yscrollcommand=ScrollBarY.set)
ScrollBarX.config(command=studentTable.xview)
ScrollBarY.config(command=studentTable.yview)


ScrollBarX.pack(side=BOTTOM,fill=X)
ScrollBarY.pack(side=RIGHT,fill=Y)

studentTable.pack(fill=BOTH,expand=1)

studentTable.heading('ID',text="ID")
studentTable.heading('Name',text="Name")
studentTable.heading('Mobile No',text="Mobile No")
studentTable.heading('Email',text="Email")
studentTable.heading('Address',text="Address")
studentTable.heading('Gender',text="Gender")
studentTable.heading('DOB',text="DOB")
studentTable.heading('Added Date',text="Added Date")
studentTable.heading('Added Time',text="Added Time")

studentTable.column('ID',width=50, anchor=CENTER)
studentTable.column('Name',width=280, anchor=CENTER)
studentTable.column('Email',width=300, anchor=CENTER)
studentTable.column('Mobile No',width=200, anchor=CENTER)
studentTable.column('Address',width=300, anchor=CENTER)
studentTable.column('Gender',width=100, anchor=CENTER)
studentTable.column('DOB',width=150, anchor=CENTER)
studentTable.column('Added Date',width=150, anchor=CENTER)
studentTable.column('Added Time',width=150, anchor=CENTER)
style=ttk.Style()
style.configure('Treeview',rowheight=40,font=('arial',12,'bold'),foreground='Black',background='White',fieldbackground='White')
style.configure('Treeview.Heading',font=('arial',14,'bold'))

studentTable.heading('ID',text="ID")
studentTable.config(show="headings")

root.mainloop()