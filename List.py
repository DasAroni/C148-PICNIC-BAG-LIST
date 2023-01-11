from tkinter import*
import random

root=Tk()
root.title(" PICNIC BAG LIST")
root.geometry("400x400")
root.configure(background="Light Green")

listed_items=Label(root)
items_number=Label(root)

def list():
    listed_items["text"]="listed_items=['bottle','Tiffin','ID Card','Chocolates','chips','Tickets','Hanky'"
    listed_items.place(relx=0.5,rely=0.4,anchor=CENTER)

























root.mainloop()