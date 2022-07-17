from tkinter import *
import pyttsx3
import PyPDF2
from tkinter.filedialog import *

win =Tk()
win.title("AudioBOOK")
win.config(bg="#1e7898")
win.geometry("700x200")


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def play():
    book = askopenfile("rb")
    pdfreader = PyPDF2.PdfFileReader(book)
    pages = pdfreader.numPages
    for num in range(0, pages+1):
     page = pdfreader.getPage(num)
     text = page.extractText()
     player=pyttsx3.init()
     player.say(text)
     player.runAndWait()

   
   


Label(win,text="No need To read Pdf files Just Listen it by Audiobook").pack(fill="x")
Button(win,text="Choose File",command=play).pack(pady="10")
Button(win,text="Stop",command=exitp).pack(pady="10")
win.mainloop()