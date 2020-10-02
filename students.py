from re import search
from tkinter import *
import tkinter as tk
import psycopg2

root = Tk()

def get_data(Name,Reg,Age,Class,Address):
    conn = psycopg2.connect(dbname="postgres",user="postgres", password="1234", host="localhost", port="8888")
    cur = conn.cursor()
    query = ''' INSERT INTO students(NAME,REG,AGE,CLASS,ADDRESS) VALUES(%s,%s,%s,%s,%s);'''
    cur.execute(query,(Name,Reg,Age,Class,Address))
    print("Form Submitted Successfully")
    conn.commit()
    conn.close()
    display_all()


def search(*name):
    conn = psycopg2.connect(dbname="postgres",user="postgres", password="1234", host="localhost", port="8888")
    cur = conn.cursor()
    query= '''SELECT * FROM  students WHERE name LIKE %s '''
    cur.execute(query,(name))
    row = cur.fetchone()
    display_search_result(row)
    conn.commit()
    conn.close()

def display_search_result(row):
    listbox = Listbox(frame,height=1,width=50)
    listbox.grid(row=15,column=1)
    listbox.insert(END,row)


def display_all():
    conn = psycopg2.connect(dbname="postgres",user="postgres", password="1234", host="localhost", port="8888")
    cur = conn.cursor()
    query = ''' SELECT * FROM students '''
    cur.execute(query)
    row = cur.fetchall()

    listbox = Listbox(frame,height=10,width=50)
    listbox.grid(row=16,column=1)
    for i in row:
        listbox.insert(END,i)

    conn.commit()
    conn.close()


canvas = Canvas(root,height=500,width=950)
canvas.pack()

frame = Frame()
frame.place(relx=0.3,rely=0.1,relwidth=0.8,relheight=0.8)


label = Label(frame,text="Students Registration Form")
label.grid(row=0,column=1)

label = Label(frame,text="Name")
label.grid(row=1,column=0)
entry_name = Entry(frame)
entry_name.grid(row=1,column=1)

label = Label(frame,text="Registration")
label.grid(row=2,column=0)
entry_Reg = Entry(frame)
entry_Reg.grid(row=2,column=1)

label = Label(frame,text="Age")
label.grid(row=3,column=0)
entry_age = Entry(frame)
entry_age.grid(row=3,column=1)

label = Label(frame,text="Class")
label.grid(row=4,column=0)
entry_class = Entry(frame)
entry_class.grid(row=4,column=1)

label = Label(frame,text="Address")
label.grid(row=5,column=0)
entry_address = Entry(frame)
entry_address.grid(row=5,column=1)

button = Button(frame,text="Cancle",command=root.quit())
button.grid(row=6,column=1)
button = Button(frame,text="Submt",command=lambda: get_data(entry_name.get(),entry_Reg.get(),entry_age.get(),entry_class.get(),entry_address.get()))
button.grid(row=6,column=2)


label = Label(frame,text="Search Here")
label.grid(row=10,column=1)

label = Label(frame,text="Search")
label.grid(row=11,column=0)
entry_search = Entry(frame)
entry_search.grid(row=11,column=1)
button = Button(frame,text="Search",command=lambda: search(entry_search.get()))
button.grid(row=11,column=2)


display_all()


root.mainloop()