from tkinter import *
from tkinter import messagebox
 # PIL -- python image library
from PIL import Image, ImageTk

def Login():
    if UsernameEntry.get()=="" or PasswordEntry.get()=="":
        messagebox.showerror("Error","Fields cannot be empty")
    elif UsernameEntry.get()=="nikhitha" and PasswordEntry.get()=="1234":
        messagebox.showinfo("success","Welcome")
        window.destroy()
        import main
        
    else:
        messagebox.showerror("Error","Please enter correct credentials")
        
        

window = Tk()
window.geometry('1280x730+0+0')
window.resizable(False,False)
window.title("Login System of Student Management System")

# Load image
img = Image.open("C:/Users/Nikhitha/OneDrive/Desktop/student_management/bg.jpg")

# Resize to window size
img = img.resize((1280, 730) )

# Convert to tkinter format
backgroundImage = ImageTk.PhotoImage(img)

# Display image
bglabel = Label(window, image=backgroundImage)
bglabel.place(x=0, y=0)

loginFrame = Frame(window,bg="white")
loginFrame.place(x=400, y=200)

logoImage = PhotoImage(file="C:/Users/Nikhitha/OneDrive/Desktop/student_management/boy.png")

logoLabel = Label(loginFrame, image=logoImage)
logoLabel.grid(row=0, column=0,columnspan=2,pady=10)

usernameLabel=Label(loginFrame,text="Username",font=("times new roman",20,"bold"),bg="white")
usernameLabel.grid(row=1,column=0,pady=10,padx=20)

UsernameEntry=Entry(loginFrame,font=("times new roman",20,"bold"),bd=5,fg="royalblue")
UsernameEntry.grid(row=1,column=1,pady=10,padx=20)


passwordLabel=Label(loginFrame,text="Password",font=("times new roman",20,"bold"),bg="white")
passwordLabel.grid(row=2,column=0,pady=10,padx=20)

PasswordEntry=Entry(loginFrame,font=("times new roman",20,"bold"),bd=5,fg="royalblue")
PasswordEntry.grid(row=2,column=1,pady=10,padx=20)

loginButton=Button(loginFrame,text="Login",font=("times new roman",20,"bold"),width=15,fg="white",bg="cornflowerblue",activebackground="cornflowerblue",activeforeground="white",cursor="hand2",command=Login)
loginButton.grid(row=3,column=1,pady=10)


window.mainloop()