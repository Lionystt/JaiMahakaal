# OM NAMAH SHIVAAY
# import tempfile
# import shutil
# import os
from tkinter import Tk
from tkinter import Toplevel, Listbox, Menu, Text, Label, Scrollbar, END, StringVar, VERTICAL
from functools import reduce
import pyttsx3
import os
# from tkinter import font
import webbrowser
from tkinter.filedialog import askopenfilename, asksaveasfilename
class NotePad(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("900x600")
        self.title("Untitled - Notepad")
    def NewFile(self):
        self.title("Untitled - Notepad")
        MyText.delete(1.0, END)
    def OpenFile(self):
        global File, MyText
        try:
            MyText.delete(1.0, END)
            File = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])
            f = open(File, "r")
            MyText.insert(1.0, f.read())
            f.close()
            self.title(f"{File}   -   Notepad")
        except:
            pass
    def SaveFile(self):
        global File, MyText
        try:
            File = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
            f = open(File, "a")
            f.write(MyText.get(1.0, END))
            f.close()
            self.title(f"{File}   -   Notepad")
        except:
            pass
    def ExitNotepad(self):
        self.destroy()
    def Copy(self):
        MyText.event_generate("<<Copy>>")
    def Paste(self):
        MyText.event_generate("<<Paste>>")
    def Cut(self):
        MyText.event_generate("<<Cut>>")
    def Search(self):
        url = f"https://www.google.com/search?q={MyText.get(1.0, END).replace(' ', '+')}&rlz=1C1RXQR_enIN1050IN1050&oq={MyText.get(1.0, END).replace(' ', '+')}&aqs=chrome.0.0i433i512l2j0i131i433i512j0i512l5j0i131i433i512j0i512.442426391j0j15&sourceid=chrome&ie=UTF-8"
        # MyText.get(1.0, END).replace(" ", "+")
        webbrowser.open_new_tab(url=url)
    def createMenuBar(self):
        MainMenu = Menu(self)
        FileMenu = Menu(MainMenu, tearoff= "0")
        FileMenu.add_command(label="New", command = self.NewFile)
        FileMenu.add_command(label="Open", command = self.OpenFile)
        FileMenu.add_command(label="Save", command = self.SaveFile)
        FileMenu.add_separator()
        FileMenu.add_command(label="Exit", command = self.ExitNotepad)
        EditMenu = Menu(MainMenu, tearoff="0")
        EditMenu.add_command(label="Copy", command=self.Copy)
        EditMenu.add_command(label="Paste", command=self.Paste)
        EditMenu.add_command(label="Cut", command=self.Cut)
        EditMenu.add_command(label="Search On Internet", command= self.Search)
        MainMenu.add_cascade(label="File", menu=FileMenu)
        MainMenu.add_cascade(label="Edit", menu=EditMenu)
        self.config(menu=MainMenu)
    def createTextwidget(self):
        global MyText, Apps
        MyText = Text(self, font = "lucida 18 italic bold", wrap="none")
        MyText.grid(row=0, column=0)
        Scroll = Scrollbar(self, orient=VERTICAL, command=MyText.yview)
        Scroll.grid(row=0, column=1, sticky="ns")
        self.grid_columnconfigure(0,weight=1)
        MyText.config(yscrollcommand=Scroll.set)
if __name__ == "__main__":
    Note = NotePad()
    File = None
    Note.createMenuBar()
    Note.createTextwidget()
    Note.mainloop()