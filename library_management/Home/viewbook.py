import tkinter as tk
from tkinter import ttk
import sqlite3


class Viewbook(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        # creating a frame for combobox selection
        frame_input = tk.Frame(self)
        frame_input.pack(pady=10)

        # creating a frame for showing table
        self.frame_table = tk.Frame(self,highlightbackground="grey",highlightthickness=1)
        self.fetch_input_from_combo(frame_input)
        
    
    def fetch_input_from_combo(self,frame_input):
        style = ttk.Style()
        # other themes
        # winnative,clam,alt,default,classic,vista,xpnative
        style.theme_use("clam")
        style.configure("TCombobox.Listbox",postoffset = (0, 50))

        mydb = sqlite3.connect("LIBRARY_MANAGEMENT_SYSTEM.db")
        my_cursor = mydb.cursor()

        my_cursor.execute("SELECT BOOK_NO FROM BOOKS")
        bookno_rec = my_cursor.fetchall()
        bookno_rec_list = ["ALL"] + list(bookno_rec)

        # combobox for book no with label
        combo1_label = tk.Label(frame_input,text="BOOK NO:",font = ('calibre',10,'bold'))
        combo1_label.grid(row=0,column=0,padx=5,pady=5)

        self.combo1 = ttk.Combobox(frame_input, values=bookno_rec_list,
                              width=30)
        self.combo1.set("ALL")  # Set the initial text for the entry
        self.combo1.grid(row=1,column=0,padx=5,pady=5)

        # Bind the combobox event to the func display_table_data
        self.combo1.bind("<<ComboboxSelected>>",self.display_table_data)

        my_cursor.execute("SELECT BOOK_NAME FROM BOOKS")
        bookname_rec = my_cursor.fetchall()
        # typecasting each element in the bookname_rec 
        # to string and adding ALL to resulting
        # list for the combobox selection
        bookname_rec_list =["ALL"] +  [str(item[0]) for item in bookname_rec]

        combo2_label = tk.Label(frame_input,text="BOOK NAME:",font = ('calibre',10,'bold'))
        combo2_label.grid(row=0,column=1,padx=5,pady=5)

        self.combo2 = ttk.Combobox(frame_input, values=bookname_rec_list,width=30)
        self.combo2.set("ALL")  # Set the initial text for the entry
        self.combo2.grid(row=1,column=1,padx=5,pady=5)

        # Bind the combobox event to the func display_table_data
        self.combo2.bind("<<ComboboxSelected>>",self.display_table_data)

        my_cursor.execute("SELECT BOOK_PRICE FROM BOOKS")
        book_price = my_cursor.fetchall()
        # converting the book_price tuple to set 
        # to remove duplicate elements
        book_price = set(book_price)

        # typecasting each element in the bookname_rec 
        # to string and adding ALL to resulting
        # list for the combobox selection
        book_price_list = ["ALL"] + [str(item[0]) for item in book_price]

        combo3_label = tk.Label(frame_input,text="BOOK PRICE:",font = ('calibre',10,'bold'))
        combo3_label.grid(row=0,column=2,padx=5,pady=5)

        self.combo3 = ttk.Combobox(frame_input, values=book_price_list,width=30)
        self.combo3.set("ALL")  # Set the initial text for the entry
        self.combo3.grid(row=1,column=2,padx=5,pady=5)

        # Bind the combobox event to the func display_table_data
        self.combo3.bind("<<ComboboxSelected>>",self.display_table_data)


        my_cursor.execute("SELECT BOOK_CATEGORY FROM BOOKS")
        book_category = my_cursor.fetchall()
        # converting the book_price tuple to set 
        # to remove duplicate elements
        book_category = set(book_category)
        # typecasting each element in the bookname_rec 
        # to string and adding ALL to resulting
        # list for the combobox selection
        book_category_list = ["ALL"] + list(book_category)

        combo4_label = tk.Label(frame_input,text="BOOK CATEGORY:",font = ('calibre',10,'bold'))
        combo4_label.grid(row=0,column=3,padx=5,pady=5)
        self.combo4 = ttk.Combobox(frame_input, values=book_category_list,width=30)
        self.combo4.set("ALL")  # Set the initial text for the entry
        self.combo4.grid(row=1,column=3,padx=5,pady=5)

        # Bind the combobox event to the func display_table_data
        self.combo4.bind("<<ComboboxSelected>>",self.display_table_data)


        book_status = ["ALL","AVAIL","ISSUED"]

        combo5_label = tk.Label(frame_input,text="BOOK NO:",font = ('calibre',10,'bold'))
        combo5_label.grid(row=0,column=4,padx=5,pady=5)

        self.combo5 = ttk.Combobox(frame_input, values=book_status,width=30)
        self.combo5.set("ALL")  # Set the initial text for the entry
        self.combo5.grid(row=1,column=4,padx=5,pady=5)

        # Bind the combobox event to the func display_table_data
        self.combo5.bind("<<ComboboxSelected>>",self.display_table_data)

    
    def fetch_bookno(self,combo1_var,combo2_var="ALL",combo3_var="ALL",combo4_var="ALL",combo5_var="ALL"):
            conn = sqlite3.connect("LIBRARY_MANAGEMENT_SYSTEM.db")
            cursor = conn.cursor()

            # if all combobox selection is "ALL"
            # then show all the contents in 
            # the books table 
            if combo1_var == "ALL" and combo2_var == "ALL" and combo3_var == "ALL" and combo4_var == "ALL" and combo5_var == "ALL":
                cursor.execute("SELECT * FROM BOOKS")
                data = cursor.fetchall()
                # get the column name of the books table
                columns = [description[0] for description in cursor.description]
                conn.close()
                return columns,data
                  
            # if book_no not equals ALL 
            # and all other equals ALL 
            # then show the selected book_no row in the books table
            elif combo1_var != "ALL" and combo2_var == "ALL" and combo3_var == "ALL" and combo4_var == "ALL" and combo5_var == "ALL":
                # use formatted string to give
                # combobox value to the 'where' query
                query = f"SELECT * FROM BOOKS WHERE BOOK_NO = {combo1_var}"
    
                cursor.execute(query)
                records = cursor.fetchall()
    
                cursor.execute("SELECT * FROM BOOKS")
                data = cursor.fetchall()
                # get the column name of the books table
                columns = [description[0] for description in cursor.description]
                conn.close()
                return columns,records

            # if book_name not equals ALL 
            # and all other equals ALL 
            # then show the selected book_name row in the books table
            elif combo1_var == "ALL" and combo2_var != "ALL" and combo3_var == "ALL" and combo4_var == "ALL" and combo5_var == "ALL":
                # use formatted string to give
                # combobox value to the 'where' query
                query = f"SELECT * FROM BOOKS WHERE BOOK_NAME = '{combo2_var}'"
    
                cursor.execute(query)
                records = cursor.fetchall()
    
                cursor.execute("SELECT * FROM BOOKS")
                data = cursor.fetchall()
                # get the column name of the books table
                columns = [description[0] for description in cursor.description]
                conn.close()
                return columns,records
            
            # if book_price not equals ALL 
            # and all other equals ALL 
            # then show the selected book_price row in the books table
            elif combo1_var == "ALL" and combo2_var =="ALL" and combo3_var != "ALL" and combo4_var =="ALL" and combo5_var == "ALL":
                # use formatted string to give
                # combobox value to the 'where' query
                query = f"SELECT * FROM BOOKS WHERE BOOK_PRICE = '{combo3_var}'"
    
                cursor.execute(query)
                records = cursor.fetchall()
    
                cursor.execute("SELECT * FROM BOOKS")
                data = cursor.fetchall()
                # get the column name of the books table
                columns = [description[0] for description in cursor.description]
                conn.close()
                return columns,records
            
            # if book_category not equals ALL 
            # and all other equals ALL 
            # then show the selected book_category row in the books table
            elif combo1_var == "ALL" and combo2_var =="ALL" and combo3_var == "ALL" and combo4_var !="ALL" and combo5_var == "ALL":
                # use formatted string to give
                # combobox value to the 'where' query
                query = f"SELECT * FROM BOOKS WHERE BOOK_CATEGORY = '{combo4_var}'"
    
                cursor.execute(query)
                records = cursor.fetchall()
    
                cursor.execute("SELECT * FROM BOOKS")
                data = cursor.fetchall()
                # get the column name of the books table
                columns = [description[0] for description in cursor.description]
                conn.close()
                return columns,records
            
            # if book_status not equals ALL 
            # and all other equals ALL 
            # then show the selected book_status row in the books table
            elif combo1_var == "ALL" and combo2_var =="ALL" and combo3_var == "ALL" and combo4_var =="ALL" and combo5_var != "ALL":
                # use formatted string to give
                # combobox value to the 'where' query
                query = f"SELECT * FROM BOOKS WHERE BOOK_STATUS = '{combo5_var}'"
    
                cursor.execute(query)
                records = cursor.fetchall()
    
                cursor.execute("SELECT * FROM BOOKS")
                data = cursor.fetchall()
                # get the column name of the books table
                columns = [description[0] for description in cursor.description]
                conn.close()
                return columns,records
            
            # if not the above mentioned cases work
            # print warning message to select 'ALL'
            # in the other combobox to get the data table
            else :
                # give the guidance message to the user to get the output
                error_label = tk.Label(self.frame_table,text="Please select 'ALL' for all other options to retrieve the required BOOKS!",
                                        fg="red",font =('calibre',10,'bold'),
                                        highlightbackground="grey",highlightthickness=1)
                error_label.grid(row=1,column=0,columnspan=5,sticky='ew')
                cursor.execute("SELECT * FROM BOOKS")
                data = cursor.fetchall()
                # get the column name of the books table
                columns = [description[0] for description in cursor.description]
                conn.close()
                # empty record to show there is no table 
                # for this selection
                records = []
                return columns,records
                 
            
    def display_table_data(self,event):
        # getting the input selected from the combobox
        combo1_var = self.combo1.get()
        combo2_var = self.combo2.get()
        combo3_var = self.combo3.get()
        combo4_var = self.combo4.get()
        combo5_var = self.combo5.get()

        # destroying each widgets in the frame table
        # for refreshing each time the selection made
        for widget in self.frame_table.winfo_children():
            widget.destroy()

        # to get table records 'data' and its column name 'columns'
        columns, data = self.fetch_bookno(combo1_var,combo2_var,combo3_var,combo4_var,combo5_var)

            # Display column names
        for j, column_name in enumerate(columns):
                label = tk.Label(self.frame_table, text=column_name, font=("bold", 12),
                                 width=25,highlightbackground="grey",
                                 highlightthickness=1,bg="#61b5fa")
                label.grid(row=0, column=j)

            # Display table data
        for i, row in enumerate(data):
                for j, value in enumerate(row):
                    label = tk.Label(self.frame_table, text=value,font=('calibre',12),
                                     width=25,highlightbackground="grey", 
                                     highlightthickness=1)
                    label.grid(row=i + 1, column=j)
        self.frame_table.pack()
