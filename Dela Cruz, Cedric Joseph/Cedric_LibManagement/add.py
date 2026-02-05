from tkinter import *
import mysql.connector
from tkinter import messagebox

def addBooks():
    def add_to_db():
        book_id = book_id_entry.get()
        book_title = title_entry.get()
        book_author = author_entry.get()

        db = mysql.connector.connect(
            host="localhost", 
            user="sqllibrary", 
            password="password", 
            database="library"
        )
        cursor = db.cursor()

        try:
            sql_query = """
                INSERT INTO books (bid, title, author, available) 
                VALUES (%s, %s, %s, %s)
            """
            values = (book_id, book_title, book_author, "YES")
            
            cursor.execute(sql_query, values)
            db.commit()

            messagebox.showinfo('Yay!', "Book has been added successfully")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error adding book: {err}")
        finally:
            cursor.close()
            db.close()
            window.destroy()

    window = Tk()
    window.title('Add Book to Library')

    Label(window, font=('helvetica', 20, 'bold'), text="Add Your Book").grid(row=0, columnspan=2, pady=10)

    Label(window, font=('helvetica', 15), text="Book ID:", fg="#41a6d9").grid(row=1, column=0, pady=5)
    book_id_entry = Entry(window, font=('helvetica', 15))
    book_id_entry.grid(row=1, column=1, pady=5)

    Label(window, font=('helvetica', 15), text="Book Title:", fg="#41a6d9").grid(row=2, column=0, pady=5)
    title_entry = Entry(window, font=('helvetica', 15))
    title_entry.grid(row=2, column=1, pady=5)

    Label(window, font=('helvetica', 15), text="Author:", fg="#41a6d9").grid(row=3, column=0, pady=5)
    author_entry = Entry(window, font=('helvetica', 15))
    author_entry.grid(row=3, column=1, pady=5)

    Button(window, text="Add Book", command=add_to_db, font=('helvetica', 15), bg="#1eaebd", fg="white").grid(row=4, columnspan=2, pady=10)

    window.mainloop()
