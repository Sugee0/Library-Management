from tkinter import *
from add import addBooks
from delete import deleteBooks
from change import updateBooks
from list import listBooks
from tkinter import messagebox


def login():
    def loginSuccess():
        username = user_entry.get()
        password = pass_entry.get()

        if username == "sqllibrary" and password == "password":
            messagebox.showinfo("Login Success", "Welcome to the Library Management System!")
            login_window.destroy()
            open_main_window()
        else:
            messagebox.showerror("Login Failed", "Invalid Password or Username.\n         Please Try Again!")

    login_window = Tk()
    login_window.title("Login")

    Label(login_window, text="Username:", font=('helvetica', 15)).grid(row=0, column=0, pady=5)
    user_entry = Entry(login_window, font=('helvetica', 15))
    user_entry.grid(row=0, column=1, pady=5)

    Label(login_window, text="Password:", font=('helvetica', 15)).grid(row=1, column=0, pady=5)
    pass_entry = Entry(login_window, show="*", font=('helvetica', 15))
    pass_entry.grid(row=1, column=1, pady=5)

    Button(login_window, text="Login", command=loginSuccess, font=('helvetica', 15), bg="#358cd5", fg="white").grid(row=2, columnspan=10, pady=10)

    login_window.mainloop()

def open_main_window():
    window = Tk()
    window.title("Library Management System")
    window.geometry("450x600")

    Label(window, font=('helvetica', 25, 'bold'), text="Library Management System", fg="#51b5e7").grid(row=0, column=0, pady=20)

    Button(window, text="Add Books", command=addBooks, font=('helvetica', 15), bg="#328bd5", fg="white").grid(row=1, column=0, padx=20, pady=10, sticky="ew")
    Button(window, text="Delete Books", command=deleteBooks, font=('helvetica', 15), bg="#328bd5", fg="white").grid(row=2, column=0, padx=20, pady=10, sticky="ew")
    Button(window, text="List Books", command=listBooks, font=('helvetica', 15), bg="#328bd5", fg="white").grid(row=3, column=0, padx=20, pady=10, sticky="ew")
    Button(window, text="Update Books", command=updateBooks, font=('helvetica', 15), bg="#328bd5", fg="white").grid(row=4, column=0, padx=20, pady=10, sticky="ew")
    Button(window, text="Exit", command=lambda: exit_to_login(window), font=('helvetica', 15), bg="#d6283b", fg="white").grid(row=5, column=0, padx=20, pady=20, sticky="ew")

    window.mainloop()   

def exit_to_login(current_window):
    current_window.destroy()
    login()

if __name__ == "__main__":
    login()
