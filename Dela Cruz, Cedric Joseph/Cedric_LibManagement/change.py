from tkinter import *
from tkinter import messagebox
import mysql.connector

def updateBooks():
    def search_book():
        book_id = id_entry.get()  
        db = mysql.connector.connect(host="localhost", user="sqllibrary", password="password", database="library")
        cursor = db.cursor()

        try:
            sql_query = "SELECT * FROM books WHERE bid = %s"
            cursor.execute(sql_query, (book_id,))
            record = cursor.fetchone()
            
            if record:
                title_entry.delete(0, END)
                author_entry.delete(0, END)

                title_entry.insert(0, record[1])
                author_entry.insert(0, record[2])
                
                update_button.config(state=NORMAL)
            else:
                messagebox.showinfo("Not Found", "No book found with the given ID")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error fetching book details: {err}")
        finally:
            cursor.close()
            db.close()

    def update_db():
        book_id = id_entry.get()
        book_title = title_entry.get()
        book_author = author_entry.get()

        db = mysql.connector.connect(host="localhost", user="sqllibrary", password="password", database="library")
        cursor = db.cursor()

    window = Tk()
    window.title('Update Book Details')

    Label(window, font=('helvetica', 20, 'bold'), text="Update Book Details").grid(row=0, columnspan=2, pady=20)

    Label(window, font=('helvetica', 15), text="Book ID:", fg="#41a6d9").grid(row=1, column=0, pady=5)
    id_entry = Entry(window, font=('helvetica', 15))
    id_entry.grid(row=1, column=1, pady=5)

    search_button = Button(window, text="Search", command=search_book, font=('helvetica', 15), bg="#1eaebd", fg="white")
    search_button.grid(row=2, columnspan=2, pady=10)

    Label(window, font=('helvetica', 15), text="Title:", fg="#41a6d9").grid(row=3, column=0, pady=5)
    title_entry = Entry(window, font=('helvetica', 15))
    title_entry.grid(row=3, column=1, pady=5)

    Label(window, font=('helvetica', 15), text="Author:", fg="#41a6d9").grid(row=4, column=0, pady=5)
    author_entry = Entry(window, font=('helvetica', 15))
    author_entry.grid(row=4, column=1, pady=5)

    update_button = Button(window, text="Update", command=update_db, font=('helvetica', 15), bg="#1eaebd", fg="white")
    update_button.grid(row=6, columnspan=2, pady=10)

    window.mainloop()
