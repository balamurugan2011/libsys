import tkinter as tk
from Home.addbooks import addbook
from Home.deletebook import Deletebook
from Home.issuebook import Issuebook
from Home.returnbook import Returnbook
from Home.viewbook import Viewbook

class Home(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Library management system")
        self.width= self.winfo_screenwidth()
        self.height= self.winfo_screenheight()



        self.geometry("%dx%d" % (self.width,self.height))

        head_lab= tk.Label(self,text="Library Management System",
                           width=self.width,height=2,bg="#61b5fa",
                           font=('calibre',20,'bold'))
        head_lab.pack(side="top")


        button_container = tk.Frame(self,width=self.winfo_screenwidth(),height=50)
        button_container.pack()

        # on button click raise the selected window
        addbook_bn = tk.Button(button_container,text="ADD BOOK",
                               command=lambda:self.show_frame("addbook"),height=1)
        viewbook_bn =tk.Button(button_container,text="VIEW BOOK",
                               command=lambda:self.show_frame("Viewbook"),height=1)
        deletebook_bn =tk.Button(button_container,text="DELETE BOOK",
                                 command=lambda:self.show_frame("Deletebook"),height=1)
        issuebook_bn =tk.Button(button_container,text="ISSUE BOOK",
                                command=lambda:self.show_frame("Issuebook"),height=1)
        returnbook_bn =tk.Button(button_container,text="RETURN BOOK",
                                 command=lambda:self.show_frame("Returnbook"),height=1)
        
        addbook_bn.pack(side="left")
        viewbook_bn.pack(side="left")
        deletebook_bn.pack(side="left")
        issuebook_bn.pack(side="left")
        returnbook_bn.pack(side="left")




        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack()

        self.frames = {}
        for F in (addbook,Viewbook,Deletebook,Issuebook,Returnbook):
            page_name = F.__name__
            frame = F(parent=container)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0,column=0,sticky='nsew')

        self.show_frame("addbook")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

def run():
        app = Home()
        app.mainloop()