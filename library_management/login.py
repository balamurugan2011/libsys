import tkinter as tk
import sqlite3
import Home.home as new_window


class Login(tk.Tk):
    def __init__(self):
        # initializing self Tk()
        tk.Tk.__init__(self)
        self.title("Library management system")

        width = 650
        height = 350

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x_coordinate = (screen_width - width) // 2
        y_coordinate = (screen_height - height) // 2 - 50

        self.geometry(f"{width}x{height}+{x_coordinate}+{y_coordinate}")

        main_lb= tk.Label(self, text="Library management system",font=('calibre',20,'bold'))

        main_lb.pack()

        self.frame = tk.Frame(self, highlightbackground="grey", highlightthickness=2)
        self.frame.pack(padx= 20 ,pady= 20)

        self.frame.place(relx=0.5,rely=0.5,anchor="center")

        self.username_label = tk.Label(self.frame, text="Username" , font=('calibre',10,'bold'))
        self.username_entry = tk.Entry(self.frame, width= 25, font=('calibre',10,'normal'))
        self.password_label = tk.Label(self.frame, text="password" ,font=('calibre',10,'bold'))
        self.password_entry = tk.Entry(self.frame, width= 25, font=('calibre',10,'bold'), show='*')

        self.username_label.grid(row=0,column=0,padx=10,pady=10)
        self.username_entry.grid(row=0,column=1,padx=10,pady=10)
        self.password_label.grid(row=1,column=0,padx=10,pady=10)
        self.password_entry.grid(row=1,column=1,padx=10,pady=10)

        self.clear_label = tk.Label(self.frame, text=" ")
        self.clear_label.grid(row=3,column=0,columnspan=2,ipadx=2)


        login_bt = tk.Button(self.frame, text="LOGIN" , font=('calibre',10,'bold'),command=self.login_fn)

        login_bt.grid(row=2,columnspan=2 ,padx=20,pady=20)

    def login_fn(self):
        # login func authenticates the user
        try:
            staff_name = str(self.username_entry.get())
            staff_id = int(self.password_entry.get())


            # connecting to the sqlite3 database
            mydb = sqlite3.connect("LIBRARY_MANAGEMENT_SYSTEM.db")
            mycur = mydb.cursor()

            mycur.execute("SELECT * FROM STAFFS")

            records = mycur.fetchall()
            
            # converting the records tuple to rows
            records_list = [list(row) for row in records]

            flag = 0

            for i in range(0,len(records_list)):
                if flag == 2:
                    break
                else:
                    flag = 0
                for j in range(0,len(records_list[0])):
                    if staff_id == records_list[i][j] : 
                        flag = flag + 1
                    elif staff_name == records_list[i][j] :
                        flag = flag + 1
                    else :
                        pass

            if flag==2:

                self.clear_label.config(text="Login Successfull",fg = "green",font=('calibre',8,'bold'))
                self.frame.after(2000,self.new_window_open)
            else :
                self.clear_label.config(text="Invalid Username and Password!",fg="red",font=('calibre',8,'bold'))

            mycur.close()

        except ValueError as e:
            self.clear_label.config(text="Password must be a NUMBER!",fg='red',font=('calibre',8,'bold'))

    def new_window_open(self):
        self.destroy()
        new_window.run()

app = Login()
app.mainloop()