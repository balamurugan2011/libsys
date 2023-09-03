import tkinter as tk
import sqlite3
class addbook(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        frame_in = tk.Frame(self,highlightbackground="grey", highlightthickness=2)
        frame_in.pack(pady=100)

        self.book_no = tk.Label(frame_in,text="BOOK NO:",font=('calibre',10,'bold'))
        self.book_no_en = tk.Entry(frame_in, width= 25,font=('calibre',10,'bold'))
        self.book_name = tk.Label(frame_in, text="BOOK NAME" , font=('calibre',10,'bold'))
        self.book_name_en = tk.Entry(frame_in, width= 25, font=('calibre',10,'bold'))
        self.book_price = tk.Label(frame_in, text="BOOK PRICE" ,font=('calibre',10,'bold'))
        self.book_price_en = tk.Entry(frame_in, width= 25, font=('calibre',10,'bold'))
        self.book_category = tk.Label(frame_in, text="BOOK CATEGORY" ,font=('calibre',10,'bold'))
        self.book_category_en = tk.Entry(frame_in, width= 25, font=('calibre',10,'bold'))
        self.add_book = tk.Button(frame_in,text="ADD BOOK",command=lambda: self.Add_book_bn())




        self.book_no.grid(row=0,column=0,padx=10,pady=10,sticky="ew")
        self.book_no_en.grid(row=0,column=1,padx=10,pady=10)
        self.book_name.grid(row=1,column=0,padx=10,pady=10,sticky="ew")
        self.book_name_en.grid(row=1,column=1,padx=10,pady=10)
        self.book_price.grid(row=2,column=0,padx=10,pady=10,sticky="ew")
        self.book_price_en.grid(row=2,column=1,padx=10,pady=10)
        self.book_category.grid(row=3,column=0,padx=10,pady=10,sticky="ew")
        self.book_category_en.grid(row=3,column=1,padx=10,pady=10)
        self.add_book.grid(row=4,column=0,columnspan=2,pady=20)

        self.status_label = tk.Label(self, text="", font=('calibre', 12, 'bold'), fg="green")
        self.status_label.pack()

    def Add_book_bn(self):
        try:
            book_no = int(self.book_no_en.get())
            book_name = str(self.book_name_en.get())
            book_price = str(self.book_price_en.get())
            book_category = str(self.book_category_en.get())
            book_status = "AVAIL"
            
            

            mydb = sqlite3.connect("LIBRARY_MANAGEMENT_SYSTEM.db")

            mycur = mydb.cursor()


            sql = "INSERT INTO BOOKS (BOOK_NO, BOOK_NAME, BOOK_PRICE, BOOK_CATEGORY, BOOK_STATUS) VALUES (?,?,?,?,?)"
            values = (book_no, book_name, book_price, book_category, book_status)

            mycur.execute(sql, values)
        
            mydb.commit()
            mycur.close()

            self.status_label.config(text="Query worked successfully!", fg="green")  # Set success message
            self.after(5000, self.clear_status)  # Clear status after 5 seconds

            # clear the entry widget after the insertion completes
            self.book_no_en.delete(0, tk.END)
            self.book_name_en.delete(0, tk.END)
            self.book_price_en.delete(0, tk.END)
            self.book_category_en.delete(0, tk.END)

        except Exception as e:
            self.status_label.config(text="Error: " + str(e), fg="red")  # Set error message

    def clear_status(self):
        # creating a empty label which can be configured later
        self.status_label.config(text="")

