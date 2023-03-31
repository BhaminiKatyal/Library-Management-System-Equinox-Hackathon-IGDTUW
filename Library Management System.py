from datetime import datetime, date, timedelta      
import mysql.connector as sqltor
from mysql.connector import errorcode

mycon=sqltor.connect(host="localhost",user="root",passwd="mysql",database="equinox")
cursor=mycon.cursor(buffered=True)

class student:
    def __init__(self,enrollment_no,name,year,fine,password):
        self.enrollment_no=enrollment_no
        self.name=name
        self.year=year
        self.fine=fine
        self.password=password
    
    def view_profile(self):
        print("enrollment no:",self.enrollment_no)
        print("name:",self.name)
        print("year:",self.year)
        print("fine:",self.fine)
        
    def change_password(self):
        self.password=new_password
        change_pass_query="update student set password='"+new_password+"' where enrollment_no="+str(stu.enrollment_no)
        cursor.execute(change_pass_query)
        mycon.commit()
        print()
        print("                          Password has been changed")
        print()

    def issue_book(self):
        cursor.execute("update BOOK set copy_issued=copy_issued+1 where book_name='"+book_req+"'")
        mycon.commit()
        issue_book_insert="insert into issue_book values(%s,'%s','%s','%s')"%(stu.enrollment_no,book_det[0],date.today(),(date.today()+timedelta(days=15)))
        cursor.execute(issue_book_insert)
        mycon.commit()
        cursor.execute("select * from BOOK where book_name='"+book_req+"'")
        book=cursor.fetchone()
        cursor.execute("delete from return_book where book_id='"+book[0]+"'")
        mycon.commit()
        print("The book has been issued to you for 15 days")

    def return_book(self):
        date1 = datetime.strptime(str(date.today()), "%Y-%m-%d")
        date2 = datetime.strptime(str(book_ret_det[3]), "%Y-%m-%d")
        difference=date1-date2
        
        if difference.days>0:
            
            cursor.execute("update student set fine=fine+"+str(difference.days)+" where enrollment_no="+str(stu.enrollment_no))
            mycon.commit()
            stu.fine=stu.fine+difference.days
            
        ret_book_query="insert into return_book values (%s,'%s','%s')"%(stu.enrollment_no,book_ret_id,date.today())
        cursor.execute(ret_book_query)
        mycon.commit()
        cursor.execute("delete from issue_book where book_id='"+book_ret_id+"'")
        mycon.commit()
        cursor.execute("update BOOK set copy_issued=copy_issued-1 where book_id='"+book_ret_id+"'")
        mycon.commit()
            
            
        print("                          The book has been returned")

    def view_fine(self):
        
        query=("select fine from student where enrollment_no={}".format(stu.enrollment_no))
        print("Fine is")
        cursor.execute(query)
        fine=cursor.fetchone()
        print(fine[0])

    
    def book_recommend(self):
        abc=input("Enter the subject whose recommendation you want:")
        cursor.execute("select book_id from return_book where enrollment_no="+str(stu.enrollment_no))
        book_id=cursor.fetchone()
        cursor.execute("select * from book where book_id='"+book_id[0]+"'")
        book=cursor.fetchone()
        query="Select * from BOOK where subject='%s' and author='%s'"%(abc,book[2])
        cursor.execute(query)
        book2=cursor.fetchone()
        print(book2[1])

def insertstudent():
        
            enrollment_no=int(input("enter enrollment no. of  the student:"))
            name=input("enter the name of the student")
            year=int(input("enter year:"))
            password=input("enter password")
            fine=int(input("enter fine due:"))
            s="insert into student values(%s,'%s',%s,%s,'%s')"%(enrollment_no,name,year,fine,password)
            cursor.execute(s)
            mycon.commit()
            
            print("record inserted successfully")
            
        
            
def  show_book_details():
        
            query ="select * from book"
            cursor.execute(query)
            for (book_id,book_name,author,subject,quantity,copy_issued)in cursor:
                print("***********************************************************")
                print("book_id:",book_id)
                print("book_name:",book_name)
                print("author:",author)
                print("subject",subject)
                print("quantity of books:",quantity)
                print("copy_issued:",copy_issued)
                print("***********************************************************")
            
            print("completed!!!")
        
            
def issued_books():
        
            query ="select * from issue_book"
            cursor.execute(query)
            for (enrollment_no,book_id,date_of_issue,date_of_return)in cursor:
                print("***********************************************************")
                print("enrollment_no:",enrollment_no)
                print("book_id:",book_id)
                print("date_of_issue:",date_of_issue)
                print("date_of_return:",date_of_return)
                print("***********************************************************")
            
            print("completed!!!")
       
def student_details():
        
            query ="select * from student"
            cursor.execute(query)
            for (enrollment_no,name,year,fine,password)in cursor:
                print("***********************************************************")
                print("enrollment_no:",enrollment_no)
                print("name:",name)
                print("year:",year)
                print("fine",fine)
                print("password",password)
                print("***********************************************************")
            print("completed!!!")
       
def searchfind_book():
       
        book_id=input("enter book code to be searched")
        query="select* from BOOK where book_id='%s'"
        t=(book_id,)
        cursor.execute(query%t)
        for (book_id,book_name,author,subject,quantity,copy_issued)in cursor:
            print("**********************************************************")
            print("book_id:",book_id)
            print("book_name:",book_name)
            print("author:",author)
            print("subject:",subject)
            print("quantitys:",quantity)
            print("copy_issued:",copy_issued)
            print("*********************************************************")
            print(cursor.rowcount,"RECORD(s) found")
            mycon.commit()

def searchbook():
    book_name=input("enter book name to be searched")
    query="select* from BOOK where book_name='%s'"
    t=(book_name,)
    cursor.execute(query%t)
    for (book_id,book_name,author,subject,quantity,copy_issued)in cursor:
        print("**********************************************************")
        print("book_id:",book_id)
        print("book_name:",book_name)
        print("author:",author)
        print("subject:",subject)
        print("quantitys:",quantity)
        print("copy_issued:",copy_issued)
        print("*********************************************************")
        print(cursor.rowcount,"RECORD(s) found")
        mycon.commit()
    
def searchfind_student():
       
        enrollment_no=input("enter enrollment no to be searched")
        query="select* from student where enrollment_no=%s"
        t=(enrollment_no,)
        cursor.execute (query%t)
        for (enrollment_no,name,year,fine,password)in cursor:
            print("**********************************************************")
            print("enrollment no:",enrollment_no)
            print("name:",name)
            print("year:",year)
            print("fine:",fine)
            print("password:",password)
            print("*********************************************************")
            print(cursor.rowcount,"RECORD(s) found")
            mycon.commit()


def view_fine():
    enrollment_no=input("enter enrollment number of the student:")  
    query=("select fine from student where enrollment_no={}".format(enrollment_no))
    print("Fine is")
    cursor.execute(query)
    for (fine,) in cursor:
        print(fine)

def add_book():
    
    book_id=input("Enter book id")
    book_name=input("Enter book name")
    author=input("Enter author name")
    subject=input("Enter subject")
    quantity=int(input("Enter quantity"))
    copy_issued=int(input("Enter no of copies issued"))
    query="insert into BOOK values('{}','{}','{}','{}',{},{})".format(book_id,book_name,author,subject,quantity,copy_issued)
    cursor.execute(query)
    mycon.commit()
    print("Book added successfully")
   

def searchfind_issue():

    book_id=input("enter book_id to be searched")
    query="select* from issue_book where book_id='"+book_id+"'"
    cursor.execute(query)
    for (enrollment_no,book_id,date_of_issue,date_of_return)in cursor:
        print("**********************************************************")
        print("enrollment no:",enrollment_no)
        print("date of issue:",date_of_issue)
        print("book id:",book_id)
        print("date of return:",date_of_return)
        print("*********************************************************")
        print(cursor.rowcount,"RECORD(s) found")
        mycon.commit()

def updatebook():
      
    book_id=input("enter Book code of the book table whose details are to be updated")
       
    print("*** enter new data***")
    
    book_name=input("enter book name:")
    author=input("enter author's name:")
    subject=input("enter subject:")
    quantity=int(input("enter the quantity of books:"))
    copy_issued=input("enter copy issued:")
    s=("UPDATE BOOK SET book_name='%s',author='%s',subject='%s',quantity=%s,copy_issued=%s where book_id='%s'"%(book_name,author,subject,quantity,copy_issued,book_id))
    cursor.execute(s)
    mycon.commit()
       
    print(cursor.rowcount,"Record(s) updated successfully")

def update_student():
        
        enrollment_no=input("enter enrollment no of student")
       
        print("*** enter new data***")
        name=input("enter name of student:")
        year=int(input("enter year:"))
        fine=int(input("enter fine:"))
        password=input("enter new password")
       
        s=("UPDATE student SET name='%s',year=%s,fine=%s,password='%s' where enrollment_no=%s"%(name,year,fine,password,enrollment_no))
        cursor.execute(s)
        cursor.execute("commit")
       
        print("Record updated successfully")
    
def deletebook():

    book_id=input("enter book code whose details are to be deleted")
    s=("delete from BOOK where book_id='%s'"%(book_id,))
    cursor.execute(s)
    cursor.execute("commit")
    print("record deleted successfully")

def deletestudent():

    enrollment_no=int(input("enter enrollment no of students whose detail is to be deleted"))
    s=("delete from student where enrollment_no=%s"%(enrollment_no,))
    cursor.execute(s)
    cursor.execute("commit")
    print("record deleted successfully")

def check2():
    ad_password = resultadmin[2]

    if ad_password != admin_passwd.get():
        my_text=Label(root,text="Wrong Credentials",font=("Ariel",10),fg="red")
        my_text.pack(pady=5)
    else:
        my_text=Label(root,text="You have been logged in, please check the previous screen",font=("Ariel",10),fg="red")
        my_text.pack(pady=5)
        global connection
        connection=1
        root.destroy()
        return connection
        
def check():
    
    cursor.execute("select * from admin where admin_id="+str(admin_id.get()))
    global resultadmin
    resultadmin=cursor.fetchone()
    
    if resultadmin is None:
        my_text=Label(root,text="Invalid ID",font=("Ariel",10),fg="red")
        my_text.pack(pady=5)
            
    else:
        my_text=Label(root,text="Enter password",font=("Ariel",10),fg="black")
        my_text.pack(pady=5)
        global admin_passwd
        admin_passwd= Entry(root)
        admin_passwd.pack()
        button2=Button(root,text="Next",command=check2).pack()
        
def check4():
    stu_password = resultstudent[4]

    if stu_password != student_passwd.get():
        my_text=Label(root,text="Wrong Credentials",font=("Ariel",10),fg="red")
        my_text.pack(pady=5)
    else:
        my_text=Label(root,text="You have been logged in, please check the previous screen",font=("Ariel",10),fg="red")
        my_text.pack(pady=5)
        global connection
        connection=2
        root.destroy()
        return connection
    
def check3():
    cursor.execute("select * from student where enrollment_no="+str(enrollment_no.get()))
    global resultstudent
    resultstudent=cursor.fetchone()
    
    if resultstudent is None:
        my_text=Label(root,text="Invalid Enrollment No.",font=("Ariel",10),fg="red")
        my_text.pack(pady=5)
            
    else:
        my_text=Label(root,text="Enter password",font=("Ariel",10),fg="black")
        my_text.pack(pady=5)
        global student_passwd
        student_passwd= Entry(root)
        student_passwd.pack()
        button4=Button(root,text="Next",command=check4).pack()
        


def login():
    text=clicked.get()
    entered_val=my_label.config(text=clicked.get())
    
    if text=="Login as Admin":
        my_text=Label(root,text="Enter admin_id:",font=("Ariel",10),fg="black")
        my_text.pack(pady=5)
        global admin_id
        admin_id = Entry(root)
        admin_id.pack()
        
        button3=Button(root,text="Next",command=check).pack()
        

            
    else:
        my_text=Label(root,text="Enter enrllment_no:",font=("Ariel",10),fg="black")
        my_text.pack(pady=5)
        global enrollment_no
        enrollment_no = Entry(root)
        enrollment_no.pack()
        
        button=Button(root,text="Next",command=check3).pack()
        

import os
from tkinter import *
from PIL import ImageTk, Image
root=Tk()
root.title("Colour testing")
root.geometry("1000x800")
img = ImageTk.PhotoImage(Image.open("library.png"))  # PIL solution


my_label=Label(root,image=img)
my_label.place(x=0,y=0,relwidth=1,relheight=1)

my_text=Label(root,text="LIBRARY MANAGEMENT SYSTEM, IGDTUW",font=("Ariel",20),fg="blue")
my_text.pack(pady=50)
my_text=Label(root,text="WELCOME",font=("Ariel",20),fg="black")
my_text.pack(pady=5)
   
clicked=StringVar()
clicked.set("Please select an option")

drop=OptionMenu(root, clicked,"Login as Admin","Login as student")
drop.pack()

login_button=Button(root,text="Next",command=login).pack()


#set background color
drop.configure(padx=10,pady=10,background='white')


def myClick():
    myLabel=Label(root, text="Successfully exited")
    myLabel.pack()
    os._exit(0)
    
exit_button = Button(root, text="Exit",command=myClick,fg="blue",bg="red")
exit_button.place(relx=1.0, rely=0.0, anchor=NE)

root.mainloop()


if connection==1:
    while True:
        print("\n")
        print("choose an option:")
        print("\t\t\t\t\t1. Add student\n\t\t\t\t\t2. Show details of all books\n\t\t\t\t\t3. Show details of all issued books")
        print("\t\t\t\t\t4. Show details of all students\n\t\t\t\t\t5. Search a book\n\t\t\t\t\t6. Details of a student\n\t\t\t\t\t7.View fine on a student")
        print("\t\t\t\t\t8. Add a book\n\t\t\t\t\t9. View issue requests of a book\n\t\t\t\t\t10. Update book details\n\t\t\t\t\t11. Update Student Details")
        print("\t\t\t\t\t12. Remove a Book\n\t\t\t\t\t13. Remove a student\n\t\t\t\t\t14. Log Out")
        choice=int(input("enter an option:"))    
       
        if choice==8:
            add_book()
        elif choice==1:
            insertstudent()
        elif choice==2:
            show_book_details()
        elif choice==3:
            issued_books()
        elif choice==4:
            student_details()    
        elif choice==5:
            searchfind_book()
        elif choice==6:
            searchfind_student()
        elif choice==7:
            view_fine()
        elif choice==9:
            searchfind_issue()
        elif choice==10:
            updatebook()
        elif choice==14:
            break
        elif choice==11:
            update_student()
        elif choice==12:
            deletebook()
        elif choice==13:
            deletestudent()
else:
    stu=student(resultstudent[0],resultstudent[1],resultstudent[2],resultstudent[3],resultstudent[4])
    print("welcome "+stu.name)
    while True:
        print("choose an option:\n                          1. My profile\n                          2.Change Password\n                          3.Issue a book\n                          4.Return a book\n                          5.View Fines\n                          6.Search a Book\n                          7.Book Recommendation\n                          8.Log out")
        choice=int(input("enter an option:"))
        if choice==1:
            stu.view_profile()
            print("\n")
        elif choice==2:
            new_password=input("enter new password:")
            stu.change_password()
            print("\n")
        elif choice==3:
            book_req=input("enter name of the book required:")
            cursor.execute("select * from BOOK where book_name='"+book_req+"'")
            book_det=cursor.fetchone()
            if book_det[4]>book_det[5]:
                stu.issue_book()
                print("\n")
            elif book_det[4]==book_det[5]:
                print("Sorry "+stu.name+" no copies of the book are available but the book, "+book_req+", can be reserved for you ")
                book_id=input("enter Book id that u want to be reserved")
                x=book_det[5]+1
                s=("UPDATE BOOK SET copy_issued=%s where book_id='%s'"%(x,book_id))
                cursor.execute(s)
                cursor.execute("commit")
                print("books reserved successfully")
                print("\n")
            elif book_det[5]>book_det[4]:
                print("this book is issued as well as reserved ,please try after some time")
                        
        elif choice==4:
            book_ret_id=input("enter id of the book to be returned:")
            cursor.execute("select * from issue_book where book_id='"+book_ret_id+"' and enrollment_no="+str(stu.enrollment_no))
            book_ret_det=cursor.fetchone()
            if book_ret_det==None:
                print("Invalid id")
                print("\n")
            else:
                stu.return_book()
                print("\n")
        elif choice==5:
            stu.view_fine()
            
        elif choice==6:
            searchbook()

        elif choice==7:
            stu.book_recommend()
            
        elif choice==8:
            break

        else:
            print("enter valid choice")
            print("\n")

