import mysql.connector as mysql
import tkinter as gui
import tkinter.messagebox

cn=mysql.connect(database="userdatabase1",user="root",password="sql123")
w=gui.Tk()
w.geometry("300x200")
w.title("User Register")
l1=gui.Label(w,text="Name",font=("Arial",14))
l2=gui.Label(w,text="UserName",font=("Arial",14))
l3=gui.Label(w,text="Password",font=("Arial",14))
l4=gui.Label(w,text="Rollno",font=("Arial",14))
e1=gui.Entry(w,width=20,font=("Arial",14))
e2=gui.Entry(w,width=20,font=("Arial",14))
e3=gui.Entry(w,width=20,font=("Arial",14),show='*')
e4=gui.Entry(w,width=20,font=("Arial",14))
def register():
    c=cn.cursor()
    try:
        name=e1.get()
        user=e2.get()
        pwd=e3.get()
        rollno=e4.get()
        c.execute("insert into user_register values(%s,%s,%s,%s)",params=(rollno,name,user,pwd))
        tkinter.messagebox.showinfo(title="info",message="User Registered...")
        cn.commit()
        e1.delete(0,gui.END)
        e2.delete(0,gui.END)
        e3.delete(0,gui.END)
        e4.delete(0,gui.END)
    except:
        tkinter.messagebox.showerror(title="error",message="Error in registering user")
    
def close():
    w.destroy()
    
b1=gui.Button(w,text="Register",font=("Arial",14),command=register)
b2=gui.Button(w,text="Exit",width=10,font=("Arial",14),command=close)
l1.grid(row=1,column=1)
e1.grid(row=1,column=2)
l2.grid(row=2,column=1)
e2.grid(row=2,column=2)
l3.grid(row=3,column=1)
e3.grid(row=3,column=2)
l4.grid(row=4,column=1)
e4.grid(row=4,column=2)
b1.grid(row=5,column=1)
b2.grid(row=5,column=2)
