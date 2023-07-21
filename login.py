from tkinter import *
import mysql.connector



def login():
    try:
        staff_name = str(username_entry.get())
        staff_id = int(password_entry.get())
    
        mydb = mysql.connector.connect(host="localhost",user="root",password="balamurugan",database="library_management_system")

        mycur = mydb.cursor()

        mycur.execute("SELECT * FROM staff")

        records = mycur.fetchall()
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
            clear_label.config(text="Login Successfull",fg = "green",font=('calibre',8,'bold'))
            
        else :
            clear_label.config(text="Invalid Username and Password!",fg="red",font=('calibre',8,'bold'))

        mycur.close()
    
    except ValueError as e:
        clear_label.config(text="Password must be a NUMBER!",fg='red',font=('calibre',8,'bold'))



root = Tk()
root.title("Library management system")
root.geometry('650x350')

main_lb= Label(root, text="Library management system",font=('calibre',20,'bold'))

main_lb.pack()

frame = Frame(root, highlightbackground="grey", highlightthickness=2)
frame.pack(padx= 20 ,pady= 20)

frame.place(relx=0.5,rely=0.5,anchor="center")

username_label = Label(frame, text="Username" , font=('calibre',10,'bold'))
username_entry = Entry(frame, width= 25, font=('calibre',10,'normal'))
password_label = Label(frame, text="password" ,font=('calibre',10,'bold'))
password_entry = Entry(frame, width= 25, font=('calibre',10,'bold'), show='*')

username_label.grid(row=0,column=0,padx=10,pady=10)
username_entry.grid(row=0,column=1,padx=10,pady=10)
password_label.grid(row=1,column=0,padx=10,pady=10)
password_entry.grid(row=1,column=1,padx=10,pady=10)

clear_label = Label(frame, text=" ")
clear_label.grid(row=3,column=0,columnspan=2,ipadx=2)


login_bt = Button(frame, text="LOGIN" , font=('calibre',10,'bold'),command=login)

login_bt.grid(row=2,columnspan=2 ,padx=20,pady=20)

root.mainloop()
