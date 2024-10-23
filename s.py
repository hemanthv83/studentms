from tkinter import*
from tkinter import ttk
import sqlite3


'''v= sqlite3.connect("Student.db")
curses=v.cursor()
curses.execute("CREATE TABLE IF NOT EXISTS Student(ID INTEGER,NAME VARCHAR(20),AGE INTEGER, DOB VARCHAR(20),GENDER VARCHAR(20),CITY VARCHAR(20))")
v.commit()
v.close()
print("Table created")'''

class Student:
    def __init__(self,main):
        self.main = main
        self.T_Frame=Frame(self.main,height=50,width=1200,background="red" ,bd=2,relief=GROOVE)
        self.T_Frame.pack()
        self.Title = Label(self.T_Frame,text="STUDENT MANAGEMENT SYSTEM", font="arial 20 bold",width=1200,bg="red")
        self.Title.pack()
        self.Frame_1 = Frame(self.main,height=580,width=500,bd=2,relief=GROOVE,background="red")
        self.Frame_1.pack(side=LEFT)
        self.Frame_1.pack_propagate(0)

        Label(self.Frame_1,text="Student Details",background="red",font="arial 12 bold").place(x=20,y=20)
        self.Id=Label(self.Frame_1,text="Id",background="red",font="arial 11 bold")
        self.Id.place(x=40,y=60)
        self.Id_Entry= Entry(self.Frame_1,width=40)
        self.Id_Entry.place(x=150,y=60)

        self.Name=Label(self.Frame_1,text="Name",background="red",font="arial 11 bold")
        self.Name.place(x=40,y=100)
        self.Name_Entry= Entry(self.Frame_1,width=40)
        self.Name_Entry.place(x=150,y=100)

        self.Age=Label(self.Frame_1,text="Age",background="red",font="arial 11 bold")
        self.Age.place(x=40,y=140)
        self.Age_Entry= Entry(self.Frame_1,width=40)
        self.Age_Entry.place(x=150,y=140)

        self.DOB=Label(self.Frame_1,text="DOB",background="red",font="arial 11 bold")
        self.DOB.place(x=40,y=180)
        self.DOB_Entry= Entry(self.Frame_1,width=40)
        self.DOB_Entry.place(x=150,y=180)

        self.Gender=Label(self.Frame_1,text="Gender",background="red",font="arial 11 bold")
        self.Gender.place(x=40,y=220)
        self.Gender_Entry= Entry(self.Frame_1,width=40)
        self.Gender_Entry.place(x=150,y=220)

        self.City=Label(self.Frame_1,text="City",background="red",font="arial 11 bold")
        self.City.place(x=40,y=260)
        self.City_Entry= Entry(self.Frame_1,width=40)
        self.City_Entry.place(x=150,y=260)

        self.Button_Frame= Frame(self.Frame_1,height=250,width=250,background="red",relief=GROOVE,bd=2)
        self.Button_Frame.place(x=80, y=300)

        self.add=Button(self.Button_Frame,text="Add",font="arial 11 bold",width=25,command=self.Add)
        self.add.pack()
        self.delete=Button(self.Button_Frame,text="Delete",font="arial 11 bold",width=25,command=self.Delete)
        self.delete.pack()
        self.update=Button(self.Button_Frame,text="Update",font="arial 11 bold",width=25,command=self.update)
        self.update.pack()
        self.Clear=Button(self.Button_Frame,text="Clear",font="arial 11 bold",width=25,command=self.Clear)
        self.Clear.pack()

   


        
                      

        self.Frame_2 = Frame(self.main,height=700,width=800,bd=2,relief=GROOVE,background="red")
        self.Frame_2.pack(side=RIGHT)

        self.tree= ttk.Treeview(self.Frame_2,columns=("c1","c2","c3","c4","c5","c6"), show="headings",height=25)
        self.tree.column("#1",anchor=CENTER,width=60)
        self.tree.heading("#1",text="ID")
        self.tree.column("#2",anchor=CENTER,width=100)
        self.tree.heading("#2",text="Name")
        self.tree.column("#3",anchor=CENTER,width=115)
        self.tree.heading("#3",text="DOB")
        self.tree.column("#4",anchor=CENTER,width=110)
        self.tree.heading("#4",text="Age")
        self.tree.column("#5",anchor=CENTER,width=110)
        self.tree.heading("#5",text="Gender")
        self.tree.column("#6",anchor=CENTER)
        self.tree.heading("#6",text="City")
        self.tree.insert("",index=0,values=(1,"hemanth",18,"08-05-2003","male","chennai"))
        self.tree.pack()

    def Add(self):
        id=self.Id_Entry.get()
        name=self.Name_Entry.get()
        age=self.Age_Entry.get()
        dob=self.DOB_Entry.get()
        gender=self.Gender_Entry.get()
        city=self.City_Entry.get()
        v= sqlite3.connect("Student.db")
        curses=v.cursor()
        curses.execute("INSERT INTO Student(ID,NAME,AGE,DOB,GENDER,CITY) VALUES(?,?,?,?,?,?)",(id,name,age,dob,gender,city))
        v.commit()
        v.close()
        print("Values Inserted")
        self.tree.insert("",index=0,values=(id,name,age,dob,gender,city))
        
    def Delete(self):
        item= self.tree.selection()[0]
        self.tree.delete(item)
        v = sqlite3.connect("Student.db")
        cursor=v.cursor()
        cursor.execute(item)

    def update(self):
        id=self.Id_Entry.get()
        name=self.Name_Entry.get()
        age=self.Age_Entry.get()
        dob=self.DOB_Entry.get()
        gender=self.Gender_Entry.get()
        city=self.City_Entry.get()
        item=self.tree.selection()[0]
        self.tree.item(item,values=(id ,name,age,dob,gender,city))

    def Clear(self):
        self.Id_Entry.delete(0,END)
        self.Name_Entry.delete(0,END)
        self.Age_Entry.delete(0,END)
        self.DOB_Entry.delete(0,END)
        self.Gender_Entry.delete(0,END)
        self.City_Entry.delete(0,END)




    


     



main=Tk()
main.title('student Management System')
main.resizable(False,False)
main.geometry("1200x600")

Student(main)
main.mainloop()