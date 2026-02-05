from tkinter import *
import mysql.connector
from tkinter import messagebox

def listBooks():
    window = Tk()
    window.title('View Books')

    Label(window, font=('helvetica', 20, 'bold'), text="View Books",fg="#d6283b").grid(row=0, columnspan=4, pady=10)

    db = mysql.connector.connect(host="localhost", user="sqllibrary", password="password", database="library")
    cursor = db.cursor()

    try:
        sql_query = "SELECT * FROM books"
        cursor.execute(sql_query)

        headers = ["ID", "Title", "Author", "Available"]

        for col, header in enumerate(headers):
            Label(
                window, 
                font=('helvetica', 15, 'bold'), 
                text=header,fg="#51b5e7"
            ).grid(row=1, column=col, padx=10, pady=5)

        current_row = 2
        for record in cursor.fetchall():
            Label(window, font=('helvetica', 15), text=record[0], fg="#0e435e").grid(row=current_row, column=0, padx=10, pady=5)
            Label(window, font=('helvetica', 15), text=record[1], fg="#0e435e").grid(row=current_row, column=1, padx=10, pady=5)
            Label(window, font=('helvetica', 15), text=record[2], fg="#0e435e").grid(row=current_row, column=2, padx=10, pady=5)
            Label(window, font=('helvetica', 15), text=record[3], fg="#0e435e").grid(row=current_row, column=3, padx=10, pady=5)
            current_row += 1
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error fetching data: {err}")
    finally:
        cursor.close()
        db.close()

    window.mainloop()
