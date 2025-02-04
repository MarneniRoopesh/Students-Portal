import mysql.connector as mysql
import tkinter as gui
import tkinter.messagebox

cn=mysql.connect(database="userdatabase1",user="root",password="sql123")
w=gui.Tk()
w.geometry("300x200")
w.title("Login")

l1=gui.Label(w,text="UserName",font=("Arial",14))
l2=gui.Label(w,text="Password",font=("Arial",14))
e1=gui.Entry(w,width=20,font=("Arial",14))
e2=gui.Entry(w,width=20,font=("Arial",14),show='*')
def login():
    try:
        user=e1.get()
        pwd=e2.get()
        c=cn.cursor()
        c.execute("select * from user_register where uname=%s and pwd=%s",params=(user,pwd))
        row=c.fetchone()
        if row==None:
            tkinter.messagebox.showinfo(title="info",message="Invalid username or password")
        else:
            tkinter.messagebox.showinfo(title="Welcome",message="Welcome to Application")
    except mysql.Error as e:
        tkinter.messagebox.showerror(title="Error",message=f"MySQL Error: {e}:")
    finally:
        if c:
            c.close()
        if cn:
            cn.close()

def close():
    w.destroy()


b1=gui.Button(w,text="Login",font=("Arial",14),command=login)
b2=gui.Button(w,text="Exit",width=10,font=("Arial",14),command=close)
l1.grid(row=1,column=1)
l2.grid(row=2,column=1)
e1.grid(row=1,column=2)
e2.grid(row=2,column=2)
b1.grid(row=3,column=1)
b2.grid(row=3,column=2)
