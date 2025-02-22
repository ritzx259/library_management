from tkinter import messagebox
from tkinter import *
import tkinter as tk
import sqlalchemy
import pandas as pd
from PIL import Image, ImageTk

# img.show()
root = tk.Tk()
root.geometry('425x400')
root.configure(bg='#FFCCCB')

# Adding logo
logo = Image.open(r"/Users/ritzmk/Documents/library_folds/library_logo.jpeg")
logo = ImageTk.PhotoImage(logo)
#logo_label = tk.Label(image=logo,height=20,width=22)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=4, row=1)

# authors = pd.read_csv(r'C:\Users\Thispc\OneDrive\Desktop\PYTHON\ipauthors (1).csv')
mydb = sqlalchemy.create_engine('mysql+pymysql://root:Ritz6669@localhost:3306/library')


def authors():
    global b
    b = e2.get()
    q = ('select * from authors_details where Author_Name =')
    q1 = (str(q) + ('"') + str(b) + ('"'))
    author = pd.read_sql_query(q1, mydb)
    messagebox.showinfo("Author Details", str(author))


def students():
    b = e2.get()
    q = ('select * from students_details where STUDENT_NAME =')
    q1 = (str(q) + ('"') + str(b) + ('"'))
    student = pd.read_sql_query(q1, mydb)
    messagebox.showinfo("Student Details", str(student))


def books():
    b = e2.get()
    q = ('select * from books_details where book_name =')
    q1 = (str(q) + ('"') + str(b) + ('"'))
    book = pd.read_sql_query(q1, mydb)
    messagebox.showinfo("Book Details", str(book))


def publishers():
    b = e2.get()
    q = ('select * from publishers_details where publisher_name =')
    q1 = (str(q) + ('"') + str(b) + ('"'))
    publisher = pd.read_sql_query(q1, mydb)
    messagebox.showinfo("Publisher details", str(publisher))


def orders():
    b = e2.get()
    q = ('select * from order_details where order_id =')
    q1 = (str(q) + str(b))
    order = pd.read_sql_query(q1, mydb)
    messagebox.showinfo("Order details", str(order))


def credits():
    b2.destroy()
    b3.destroy()
    b4.destroy()
    b5.destroy()
    b6.destroy()
    b7.destroy()
    e2.destroy()
    l4.destroy()
    l2.destroy()
    l3.destroy()
    Label(root, text="Made By:", bg='#FFCCCB', fg='red', bd=26, font="ariel").grid(row=4,column=4)
    Label(root, text="Aryan Kanjilal", bg='#FFCCCB', fg='black', bd=22, font="ariel").grid(row=6,column=4)
    messagebox.showinfo("", "Thank you")


def confirmation():
    global a,c
    a = e1.get()
    c = e3.get()
    if a == '6996' and c=='zac'or a=='9546' and c=='Admin' :
        # messagebox.showinfo("confirmation","correct password")
        def screen2():
            l2.destroy()
            b1.destroy()
            e1.destroy()
            e3.destroy()
            l7.destroy()
            l3.grid(row=5, column=4)
            b2.grid(row=10, column=4, sticky=W)  # button to search author details
            b3.grid(row=10, column=4, sticky=E)  # button to search student details
            b4.grid(row=15, column=4, sticky=W)  # button to search publisher details
            b5.grid(row=15, column=4, sticky=E)  # button to search book details
            b6.grid(row=20, column=4, sticky=S)  # button to search order details
            b7.grid(row=25, column=4, sticky=S)
            e2.grid(row=6, column=4)

        screen2()

    else:
        messagebox.showinfo("", "Incorrect Password or Username")


e1 = Entry(root, width=50, borderwidth=6)
e2 = Entry(root, width=50, borderwidth=6)
e3 = Entry(root, width=50, borderwidth=6)
l2 = Label(root, text='Password', )
l7 = Label(root, text='Username', )
b1 = Button(root, text='Confirm', command=lambda: confirmation(), activebackground='red')
l4 = Label(root, text="LIBRARY MANAGEMENT SYSTEM", bg='powder blue', fg='green', bd=20, font="ariel")
b2 = Button(root, text='Search Author', command=lambda: authors(), activebackground='red')
b3 = Button(root, text='Search Student', command=lambda: students(), activebackground='red')
b4 = Button(root, text='Search Publisher', command=lambda: publishers(), activebackground='red')
b5 = Button(root, text='Search Book', command=lambda: books(), activebackground='red')
b6 = Button(root, text='Search Order ID', command=lambda: orders(), activebackground='red')
b7 = Button(root, text="Check Credits", command=lambda: credits(), activebackground='red')
l3 = Label(root, text="Searching details", font='ariel', bg='light green', fg='black')
l2.grid(row=8, column=4,sticky=W)
l7.grid(row=7,column=4,sticky=W)
l4.grid(row=2, column=4)
b1.grid(row=10, column=4)
e1.grid(row=8, column=4,sticky=E)
e3.grid(row=7, column=4,sticky=E)
root.mainloop()