from tkinter import *
import time
import pandas
from tkinter import ttk, messagebox,filedialog
import pymysql



def iexit():
    result=messagebox.askyesno('Confirm','Do youwant?')
    if result:
        root.destroy()
    else:
        pass


def export_data():
    url=filedialog.asksaveasfilename(defaultextension='.csv')
    indexing=studentTable.get_children()
    newlist=[]
    for index in indexing:
        contend=studentTable.item(index)
        datalist=contend['values']
        newlist.append(datalist)


    table=pandas.DataFrame(newlist,columns=['Id','Name','Mobile','Email','Address','Gender','DOB','Added Date','Added Time'])
    table.to_csv(url,index=False)
    messagebox.showinfo('Data is saved successfully')

def update_student():
    def update_data():
        query = 'UPDATE student SET name=%s, email=%s, mobile=%s, address=%s, gender=%s, dob=%s WHERE id=%s'
        mycursor.execute(query, (
            name_entry.get(), email_entry.get(), phone_entry.get(),
            address_entry.get(), gender_entry.get(), dob_entry.get(),
            id_entry.get()
        ))
        con.commit()
        messagebox.showinfo('Data Updated', f'ID {id_entry.get()} has been modified')
        update_window.destroy()
        show_student()




    update_window = Toplevel()
    update_window.title('update')
    update_window.grab_set()
    update_window.resizable(0, 0)
    idLabel = Label(update_window, text='Id', font=('times new roman', 20, 'bold'))
    idLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    id_entry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    id_entry.grid(row=0, column=1, pady=15, padx=10)

    nameLabel = Label(update_window, text='name', font=('times new roman', 20, 'bold'))
    nameLabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    name_entry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    name_entry.grid(row=1, column=1, pady=15, padx=10)

    phoneLabel = Label(update_window, text='phone', font=('times new roman', 20, 'bold'))
    phoneLabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    phone_entry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    phone_entry.grid(row=2, column=1, pady=15, padx=10)

    emailLabel = Label(update_window, text='email', font=('times new roman', 20, 'bold'))
    emailLabel.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    email_entry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    email_entry.grid(row=3, column=1, pady=15, padx=10)

    addressLabel = Label(update_window, text='address', font=('times new roman', 20, 'bold'))
    addressLabel.grid(row=4, column=0, padx=30, pady=15, sticky=W)
    address_entry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    address_entry.grid(row=4, column=1, pady=15, padx=10)

    genderLabel = Label(update_window, text='gender', font=('times new roman', 20, 'bold'))
    genderLabel.grid(row=5, column=0, padx=30, pady=15, sticky=W)
    gender_entry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    gender_entry.grid(row=5, column=1, pady=15, padx=10)

    dobLabel = Label(update_window, text='D.O.B', font=('times new roman', 20, 'bold'))
    dobLabel.grid(row=6, column=0, padx=30, pady=15, sticky=W)
    dob_entry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    dob_entry.grid(row=6, column=1, pady=15, padx=10)

    update_student_button = Button(update_window, text='update STUDENT',command=update_data)
    update_student_button.grid(row=7, columnspan=2, pady=10)

    indexing=studentTable.focus()
    print(indexing)
    contend=studentTable.item(indexing)
    listdata=contend['values']
    id_entry.insert(0,listdata[0])
    name_entry.insert(0,listdata[1])
    phone_entry.insert(0,listdata[2])
    email_entry.insert(0, listdata[3])
    address_entry.insert(0, listdata[4])
    gender_entry.insert(0, listdata[5])
    dob_entry.insert(0, listdata[6])









def show_student():
    query = 'SELECT * FROM student'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())  # Clear existing data
    for data in fetched_data:
        studentTable.insert('', END, values=data)





def delete_student():
    indexing = studentTable.focus()
    print(indexing)
    content = studentTable.item(indexing)
    content_id = content['values'][0]
    query = 'DELETE FROM student WHERE id=%s'
    mycursor.execute(query, (content_id,))
    con.commit()
    messagebox.showinfo('Deleted', f'Id {content_id} is deleted successfully')

    # Refresh the table after deletion
    query = 'SELECT * FROM student'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children()) # Clear existing data
    for data in fetched_data:
        studentTable.insert('', END, values=data)







def search_student():
    def search(mycursor, id_entry, name_entry, phone_entry, email_entry, address_entry, gender_entry, dob_entry):
        query = 'SELECT * FROM student WHERE id=%s OR name=%s OR email=%s OR mobile=%s OR address=%s OR gender=%s OR dob=%s'
        mycursor.execute(query, (
            id_entry.get(), name_entry.get(), email_entry.get(), phone_entry.get(), address_entry.get(),
            gender_entry.get(), dob_entry.get()))
        studentTable.delete(*studentTable.get_children())
        fetched_data = mycursor.fetchall()
        for data in fetched_data:
            studentTable.insert('', END, values=data)

    search_window = Toplevel()
    search_window.title('search student')
    search_window.grab_set()
    search_window.resizable(0, 0)
    idLabel = Label(search_window, text='Id', font=('times new roman', 20, 'bold'))
    idLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    id_entry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    id_entry.grid(row=0, column=1, pady=15, padx=10)

    nameLabel = Label(search_window, text='name', font=('times new roman', 20, 'bold'))
    nameLabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    name_entry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    name_entry.grid(row=1, column=1, pady=15, padx=10)

    phoneLabel = Label(search_window, text='phone', font=('times new roman', 20, 'bold'))
    phoneLabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    phone_entry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    phone_entry.grid(row=2, column=1, pady=15, padx=10)

    emailLabel = Label(search_window, text='email', font=('times new roman', 20, 'bold'))
    emailLabel.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    email_entry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    email_entry.grid(row=3, column=1, pady=15, padx=10)

    addressLabel = Label(search_window, text='address', font=('times new roman', 20, 'bold'))
    addressLabel.grid(row=4, column=0, padx=30, pady=15, sticky=W)
    address_entry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    address_entry.grid(row=4, column=1, pady=15, padx=10)

    genderLabel = Label(search_window, text='gender', font=('times new roman', 20, 'bold'))
    genderLabel.grid(row=5, column=0, padx=30, pady=15, sticky=W)
    gender_entry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    gender_entry.grid(row=5, column=1, pady=15, padx=10)

    dobLabel = Label(search_window, text='D.O.B', font=('times new roman', 20, 'bold'))
    dobLabel.grid(row=6, column=0, padx=30, pady=15, sticky=W)
    dob_entry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    dob_entry.grid(row=6, column=1, pady=15, padx=10)

    search_student_button = Button(search_window, text='search STUDENT', command=lambda: search(
        mycursor, id_entry, name_entry, phone_entry, email_entry, address_entry, gender_entry, dob_entry))
    search_student_button.grid(row=7, columnspan=2, pady=10)









def add_student():
    def add_data():
        currentdate = time.strftime('%d/%m/%Y')  # Get the current date
        currenttime = time.strftime('%H:%M:%S')  # Get the current time
        if idEntry.get() == '' or nameEntry.get() == '' or phoneEntry.get() == '' or \
                emailEntry.get() == '' or addressEntry.get() == '' or genderEntry.get() == '' or dobEntry.get() == '':
            messagebox.showerror('All fields are required', parent=add_window)
        else:
            try:
                query = 'insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                mycursor.execute(query, (idEntry.get(), nameEntry.get(),
                                     phoneEntry.get(), emailEntry.get(),
                                     addressEntry.get(), genderEntry.get(),
                                     dobEntry.get(), currentdate, currenttime))
                con.commit()
                result=messagebox.askyesno('confirm','data added . do you want to clean form?',parent=add_window)
                print(result)
                if result:
                    idEntry.delete(0,END)
                    nameEntry.delete(0, END)
                    phoneEntry.delete(0, END)
                    emailEntry.delete(0, END)
                    addressEntry.delete(0, END)
                    genderEntry.delete(0, END)
                    dobEntry.delete(0, END)
                else:
                    pass
            except:
                messagebox.showerror('duplicate id',parent=add_window)
                return
            query='select *from student'
            mycursor.execute(query)
            fetched_data=mycursor.fetchall()
            studentTable.delete(*studentTable.get_children())
            for data in fetched_data:

                studentTable.insert('',END,values=data)


    add_window=Toplevel()
    add_window.grab_set()
    add_window.resizable(0,0)
    idLabel = Label(add_window,text='Id',font=('times new roman',20,'bold'))
    idLabel.grid(row=0,column=0,padx=30,pady=15,sticky=W)
    idEntry=Entry(add_window,font=('roman',15,'bold'),width=24)
    idEntry.grid(row=0,column=1,pady=15,padx=10)

    nameLabel = Label(add_window, text='name', font=('times new roman', 20, 'bold'))
    nameLabel.grid(row=1, column=0, padx=30, pady=15,sticky=W)
    nameEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, pady=15, padx=10)

    phoneLabel = Label(add_window, text='phone', font=('times new roman', 20, 'bold'))
    phoneLabel.grid(row=2, column=0, padx=30, pady=15,sticky=W)
    phoneEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    phoneEntry.grid(row=2, column=1, pady=15, padx=10)

    emailLabel = Label(add_window, text='email', font=('times new roman', 20, 'bold'))
    emailLabel.grid(row=3, column=0, padx=30, pady=15,sticky=W)
    emailEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    emailEntry.grid(row=3, column=1, pady=15, padx=10)

    addressLabel = Label(add_window, text='address', font=('times new roman', 20, 'bold'))
    addressLabel.grid(row=4, column=0, padx=30, pady=15,sticky=W)
    addressEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    addressEntry.grid(row=4, column=1, pady=15, padx=10)

    genderLabel = Label(add_window, text='gender', font=('times new roman', 20, 'bold'))
    genderLabel.grid(row=5, column=0, padx=30, pady=15,sticky=W)
    genderEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    genderEntry.grid(row=5, column=1, pady=15, padx=10)

    dobLabel = Label(add_window, text='D.O.B', font=('times new roman', 20, 'bold'))
    dobLabel.grid(row=6, column=0, padx=30, pady=15,sticky=W)
    dobEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    dobEntry.grid(row=6, column=1, pady=15, padx=10)

    add_student_button=Button(add_window,text='ADD STUDENT',command=add_data)
    add_student_button.grid(row=7,columnspan=2,pady=10)






Count = 0
text = ''
s = 'Student Management System'


def connect_database():
    def connect():
        global  mycursor,con

        try:
            con = pymysql.connect(host=hostEntry.get(), user=userEntry.get(), password=passwordEntry.get())
            mycursor = con.cursor()
            messagebox.showinfo('Database connection successful', parent=connectWindow)

            try:
                query = 'CREATE DATABASE IF NOT EXISTS studentmanagementsystem'
                mycursor.execute(query)

                query = 'USE studentmanagementsystem'
                mycursor.execute(query)

                query = '''
                    CREATE TABLE IF NOT EXISTS student (
                    id INT NOT NULL PRIMARY KEY,
                    name VARCHAR(30),
                    mobile VARCHAR(10),
                    email VARCHAR(30),
                    address VARCHAR(100),
                    gender VARCHAR(20),
                    dob VARCHAR(20),
                    date VARCHAR(50),
                    time VARCHAR(50)
                    )
                '''
                mycursor.execute(query)

                con.commit()
                messagebox.showinfo('Database setup successful', parent=connectWindow)
                connectWindow.destroy()
                addstudentButton.config(state=NORMAL)
                SearchstudentButton.config(state=NORMAL)
                updatestudentButton.config(state=NORMAL)
                showstudentButton.config(state=NORMAL)
                exportstudentButton.config(state=NORMAL)
                DeletestudentButton.config(state=NORMAL)

            except Exception as e:
                messagebox.showerror('Error', f'Failed to create table: {str(e)}', parent=connectWindow)

        except Exception as e:
            messagebox.showerror('Error', f'Failed to connect: {str(e)}', parent=connectWindow)

    global hostEntry, userEntry, passwordEntry, connectWindow
    connectWindow = Toplevel()
    connectWindow.grab_set()
    connectWindow.geometry('470x250+730+230')
    connectWindow.title('Database Connection')
    connectWindow.resizable(0, 0)

    hostnamelabel = Label(connectWindow, text="Host Name", font=('arial', 20, 'bold'))
    hostnamelabel.grid(row=0, column=0, padx=20)

    hostEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
    hostEntry.grid(row=0, column=1, padx=40, pady=20)

    usernamelabel = Label(connectWindow, text="User Name", font=('arial', 20, 'bold'))
    usernamelabel.grid(row=1, column=0, padx=20)

    userEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
    userEntry.grid(row=1, column=1, padx=40, pady=20)

    passwordlabel = Label(connectWindow, text="Password", font=('arial', 20, 'bold'))
    passwordlabel.grid(row=2, column=0, padx=20)

    passwordEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2, show='*')
    passwordEntry.grid(row=2, column=1, padx=40, pady=20)

    connectButton = Button(connectWindow, text='CONNECT', command=connect)
    connectButton.grid(row=3, column=0, columnspan=2)

def slider():
    global Count
    global text
    if Count == len(s):
        Count=0
        text=''
    text = text + s[Count]
    sliderLabel.config(text=text)
    Count += 1
    sliderLabel.after(300, slider)

def clock():
    global date,currenttime
    date = time.strftime('%d/%m/%Y')
    currenttime = time.strftime('%H:%M:%S')
    datetimelabel.config(text=f'Date:{date}\nTime:{currenttime}')
    datetimelabel.after(1000, clock)

root = Tk()
root.geometry('1174x680+0+0')
root.title('Student management system')

datetimelabel = Label(root, text='hello', font=('times new roman', 18, 'bold'))
datetimelabel.place(x=5, y=5)
clock()

sliderLabel = Label(root, text=s, font=('arial', 28, 'italic bold'), width=30)
sliderLabel.place(x=200, y=0)
slider()

connectButton = Button(root, text='Connect database', command=connect_database)
connectButton.place(x=980, y=0)

leftFrame = Frame(root)
leftFrame.place(x=50, y=80, width=300, height=600)

addstudentButton = Button(leftFrame, text='ADD Student', command=add_student)
addstudentButton.grid(row=1, column=0, pady=20)

SearchstudentButton = Button(leftFrame, text='Search Student',command=search_student)
SearchstudentButton.grid(row=2, column=0, pady=20)

DeletestudentButton = Button(leftFrame, text='Delete Student',command=delete_student)
DeletestudentButton.grid(row=3, column=0, pady=20)

updatestudentButton = Button(leftFrame, text='update Student',command=update_student)
updatestudentButton.grid(row=4, column=0, pady=20)

showstudentButton = Button(leftFrame, text='Show Student',command=show_student)
showstudentButton.grid(row=5, column=0, pady=20)

exportstudentButton = Button(leftFrame, text='Export Student',command=export_data)
exportstudentButton.grid(row=6, column=0, pady=20)

exitstudentButton = Button(leftFrame, text='Exit Student',command=iexit)
exitstudentButton.grid(row=7, column=0, pady=20)

rightFrame = Frame(root)
rightFrame.place(x=350, y=80, width=820, height=600)

scrollBarX = Scrollbar(rightFrame, orient=HORIZONTAL)
scrollBarY = Scrollbar(rightFrame, orient=VERTICAL)

studentTable = ttk.Treeview(
    rightFrame,
    columns=('Id', 'Name', 'Mobile No', 'Email', 'Address', 'Gender', 'D.O.B', 'Added Date', 'Added Time'),
    xscrollcommand=scrollBarX.set,
    yscrollcommand=scrollBarY.set
)

scrollBarX.config(command=studentTable.xview)
scrollBarY.config(command=studentTable.yview)

scrollBarX.pack(side='bottom', fill='x')
scrollBarY.pack(side='right', fill='y')
studentTable.pack(fill='both', expand=1)

studentTable.heading('Id', text='Id')
studentTable.heading('Name', text='Name')
studentTable.heading('Mobile No', text='Mobile No')
studentTable.heading('Email', text='Email')
studentTable.heading('Address', text='Address')
studentTable.heading('Gender', text='Gender')
studentTable.heading('D.O.B', text='D.O.B')
studentTable.heading('Added Date', text='Added Date')
studentTable.heading('Added Time', text='Added Time')

studentTable.config(show='headings')

root.mainloop()
