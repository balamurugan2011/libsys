import tkinter as tk
import mysql.connector
import sqlite3

class Deletebook(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        width = self.winfo_screenwidth()

        frame_in = tk.Frame(self,highlightbackground="grey", highlightthickness=2)
        frame_in.pack(pady=100)

        self.book_no = tk.Label(frame_in,text="BOOK NO:",font=('calibre',10,'bold'))
        self.book_no_en = tk.Entry(frame_in, width= 25,font=('calibre',10,'bold'))
        self.book_name = tk.Label(frame_in, text="BOOK NAME" , font=('calibre',10,'bold'))
        self.book_name_en = tk.Entry(frame_in, width= 25, font=('calibre',10,'bold'))
        self.delete_book = tk.Button(frame_in,text="DELETE BOOK",command=lambda: self.delete_book_bn())




        self.book_no.grid(row=0,column=0,padx=10,pady=10,sticky="ew")
        self.book_no_en.grid(row=0,column=1,padx=10,pady=10)
        self.book_name.grid(row=1,column=0,padx=10,pady=10,sticky="ew")
        self.book_name_en.grid(row=1,column=1,padx=10,pady=10)
        self.delete_book.grid(row=4,column=0,columnspan=2,pady=20)

        self.status_label = tk.Label(self, text="", font=('calibre', 12, 'bold'), fg="green")
        self.status_label.pack()

    def delete_book_bn(self):
        try:
            book_no = int(self.book_no_en.get())
            book_name = str(self.book_name_en.get())
            
            mydb = sqlite3.connect("LIBRARY_MANAGEMENT_SYSTEM.db")

            mycur = mydb.cursor()
            
            mycur.execute("SELECT BOOK_NO FROM BOOKS")
            record = mycur.fetchall()
            mycur.execute("SELECT BOOK_NAME FROM BOOKS")
            name_record = mycur.fetchall()

            # converting the record values to integers
            int_record = [int(item[0]) for item in record]

            # converting the name_record values to string
            str_name_rec = [str(item[0]) for item in name_record]

            # making the string in str_name_rec values to lowercase
            str_name_rec = [item[0].lower() for item in name_record]
            
            # checking that both the book no and book name matches 
            # with the data in the database
            if book_no in int_record and book_name.lower() in str_name_rec:
                sql = "DELETE FROM BOOKS WHERE BOOK_NO = ?"
                values = [book_no]
                mycur.execute(sql, values)
                mydb.commit()
                mycur.close()
                self.status_label.config(text=f"The Book:{book_name} was deleted successfully!", fg="green")  # Set success message
                self.after(5000, self.clear_status)  # Clear status after 5 seconds
                self.book_no_en.delete(0, tk.END)
                self.book_name_en.delete(0, tk.END)
            else:
                 self.status_label.config(text=f"The book_no:{book_no} is not available! or Invalid Book Name",fg="red")

        except Exception as e:
            self.status_label.config(text="Error: " + str(e), fg="red")  # Set error message

    def clear_status(self):
        self.status_label.config(text="")

