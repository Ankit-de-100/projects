from PIL import ImageTk
from tkinter import Tk, Frame, Label, Entry, Button, messagebox, PhotoImage

def login():
    if usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror('Error', 'Fields cannot be empty')
    elif usernameEntry.get() == 'Ankit' and passwordEntry.get() == '12345':
        messagebox.showinfo('Welcome loser')
        window.destroy()
        import sms
    else:
        messagebox.showerror('Error', 'Please enter correct credentials')

window = Tk()

window.geometry('1280x700+0+0')
window.title('System administrator')
window.resizable(False, False)

backgroundImage = ImageTk.PhotoImage(file='bg.jpg')

bgLabel = Label(window, image=backgroundImage)
bgLabel.place(x=0, y=0)

loginframe = Frame(window, bg='white')
loginframe.place(x=400, y=150)

logoImage = PhotoImage(file='logo.png')

logoLabel = Label(loginframe, image=logoImage)
logoLabel.grid(row=0, column=0, columnspan=2, pady=10)

usernameImage = PhotoImage(file='user.png')
from tkinter import LEFT

usernameLabel = Label(loginframe, image=usernameImage, text='username', compound=LEFT,
                      font=('times new roman', 20, 'bold'), bg='white')
usernameLabel.grid(row=1, column=0, pady=10, padx=20)

usernameEntry = Entry(loginframe, font=('times new roman', 20, 'bold'), bd=5, fg='Blue')
usernameEntry.grid(row=1, column=1, pady=10, padx=20)

# password
passwordImage = PhotoImage(file='password.png')
passwordLabel = Label(loginframe, image=passwordImage, text='password', compound=LEFT,
                      font=('times new roman', 20, 'bold'), bg='white')
passwordLabel.grid(row=2, column=0, pady=10, padx=20)

passwordEntry = Entry(loginframe, font=('times new roman', 20, 'bold'), bd=5, fg='Blue')
passwordEntry.grid(row=2, column=1, pady=10, padx=20)

# login

loginButton = Button(loginframe, text='login', font=('times new roman', 14, 'bold'), bg='white', pady=10
                     , width=15, fg='white', background='cornflowerblue', activebackground='cornflowerblue'
                     , cursor='hand2', command=login)
loginButton.grid(row=3, column=1, columnspan=2)

window.mainloop()
