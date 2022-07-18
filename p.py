import pyshorteners
from tkinter import *
root =Tk()
root.title("URL Shortner")
root.geometry("700x200")
root.config(bg="red")
def shorturl():
    u= entry1.get()
    s=pyshorteners.Shortener()
    a = s.tinyurl.short(u)
    entry2.insert(END, a)
    
Label(root,text="Enter url",font="impact").pack(fill="x")
entry1 =Entry(root,width="100")
entry1.pack(pady="20")
Button(root,text="Click",bg="yellow",command=shorturl).pack()
entry2 =Entry(root,width="100")
entry2.pack(pady="20")
root.mainloop()