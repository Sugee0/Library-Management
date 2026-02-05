from tkinter import *
import mysql.connector
from tkinter import messagebox

def deleteBooks():
    def delete_from_db():
        book_id = book_id_entry.get()

        db = mysql.connector.connect(
            host="localhost", 
            user="sqllibrary", 
            password="password", 
            database="library"
        )
        cursor = db.cursor()

        try:
            sql_query = "DELETE FROM books WHERE bid = %s"
            cursor.execute(sql_query, (book_id,))
            db.commit()

            if cursor.rowcount == 0:
                messagebox.showinfo("Not Found", "Book ID not found")
            else:
                messagebox.showinfo('Success', "Book has been deleted!")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error deleting book: {err}")
        finally:
            cursor.close()
            db.close()
            window.destroy()

    window = Tk()
    window.title('Delete Book from Library')

    Label(window, font=('helvetica', 20, 'bold'), text="Delete Book").grid(row=0, columnspan=2, pady=10)

    Label(window, font=('helvetica', 15), text="Book ID:", fg="#41a6d9").grid(row=1, column=0, pady=5)
    book_id_entry = Entry(window, font=('helvetica', 15))
    book_id_entry.grid(row=1, column=1, pady=5)

    Button(window, text="Delete Book", command=delete_from_db, font=('helvetica', 15), bg="#1eaebd", fg="white").grid(row=2, columnspan=2, pady=10)

    window.mainloop()
