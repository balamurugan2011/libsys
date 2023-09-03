import tkinter as tk

class Returnbook(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="This is return book page", font=('Helvetica', 18,"italic"))
        label.pack(side="top", fill="x", pady=10)
        
        