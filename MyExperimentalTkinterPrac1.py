# OM NAMAH SHIVAAY
# Importing the requirements
from tkinter import Tk, ttk
from tkinter import *
from tkinter import filedialog
from tkinter import colorchooser
from tkinter import messagebox
from PIL import ImageTk, Image
# from tkinter import Combobox
# Creating a class for the GUi
class MyExperimentalTkinterPrac(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x600")
        self.title("My experimental GUI")
    def createFrame(self):
        global frame
        frame = Frame(root, width=500, height=500, colormap="new")
        frame.grid(row=0, column=0)
    def createLabel(self, a):
        label = Label(a, text="Hi", font="lucida 45")
        label.grid(row=0, column=1)
    def createLabel2(self, a):
        label2 = Label(a, text = "Hi", font="lucida 45")
        label2.grid()
    def createButton(self, a):
        button = Button(a, text="Click", command=self.createLabel2)
        button.grid(row=0, column=3)
    def createRadioButton(self, a):
        radio1 = Radiobutton(a, text="MyRadio", variable=StringVar(), value="MyRadio1")
        radio1.grid(row=0, column=1)
        radio2 = Radiobutton(a, text="MyRadio", variable=StringVar(), value="MyRadio2")
        radio2.grid(row=1, column=3)
        radio3 = Radiobutton(a, text="MyRadio", variable=StringVar(), value="MyRadio3")
        radio3.grid(row=2, column=3)
        radio4 = Radiobutton(a, text="MyRadio", variable=StringVar(), value="MyRadio4")
        radio4.grid(row=3, column=3)
    def createCheckBox(self, a):
        check = Checkbutton(a, text="How are you?", variable=IntVar())
        check.grid(row=0, column=7)
    def createListBox(self, a):
        listitems = ["car", "bike", "cycle", "bus", "truck", "jcb"]
        myvar = StringVar(value=listitems)
        list = Listbox(a, listvariable=myvar)
        list.grid(row=0, column=8)
    def createComboBox(self, a):
        comboitems = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        combovar = StringVar(value=comboitems)
        combo = ttk.Combobox(a, textvariable = combovar)
        combo.bind("<<ComboboxSelected>>", self.createLabel2)
        combo.grid()
    def createEntry(self, a):
        entry = Entry(a, textvariable=StringVar())
        entry.grid()
        # Creating Password Field
        password = StringVar()
        pswd = Entry(a, textvariable=password, show="*")
        pswd.grid()
    def createTextWidget(self, a):
        global text
        text = Text(a, font="lucida 18")
        text.grid(row=3, column=0)
        self.createScrollBar(frame)
    def createMenu(self):
        global menu, menu2
        menu = Menu(root)
        menu2 = Menu(menu, tearoff=0)
        menu2.add_command(label="item1", command=self.createWindowDialog1)
        menu2.add_command(label = "item2", command=self.createWindowDialog2)
        menu2.add_command(label = "My Event", command=self.createEvent)
        menu2.add_checkbutton(label="how are you?", variable=IntVar())
        menu2.add_separator()
        menu2.add_radiobutton(label="mobile", variable=StringVar(), value="mobile")
        menu.add_cascade(label="menu2", menu=menu2)
        root.config(menu=menu)
    def createScrollBar(self, a):
        # scroll = Scrollbar(root, orient=VERTICAL, command=text.yview)
        # scroll.grid(row=0, column=4, sticky=NW,)
        # # scroll.config(command=text.yview)
        # text.config(yscrollcommand=scroll.set)
        s = ttk.Scrollbar(text, orient=VERTICAL, command=text.yview)
        s.grid()
        text.config(yscrollcommand=s.set)
    def createRangeScale(self, a):
        range = Scale(a, from_= 1, to=20, orient=HORIZONTAL)
        range.grid(row=0, column=0)
    def createTopLevelWidget(self):
        global top
        top = Toplevel(root, takefocus=False)
        label3 = Label(root, text="This is a top level widget")
        label3.grid()
        top.grid()
    def createSpinBox(self, a):
        spinvar = StringVar()
        spin = Spinbox(a, from_=0,to=27, textvariable=spinvar)
        spin.grid()
    def createProgressbar(self, a):
        progress = ttk.Progressbar(a, orient=HORIZONTAL, length=90, mode="determinate")
        progress.grid()
    def createEvent(self):
        root.event_generate("<<MyEvent>>")
    def bindEvent(self):
        # root.bind("<<MyEvent>>", self.createFrame)
        # top.bind("<Enter>", self.createFrame)
        pass
        # print("Event Bound")
    def createContextualMenu(self, a):
        a.bind("<2>", self.createMenu)
    def createWindowDialog1(self):
        filedialog.askopenfilename()
    def createWindowDialog2(self):
        filedialog.asksaveasfilename()
    def importColorChooser(self):
        colorchooser.askcolor("red")
    def createAlertMessage(self):
        messagebox.showinfo("MessageBox", "This is a messagebox.")
    def createPaneWindow(self, a):
        global pane 
        pane = PanedWindow(a, orient=HORIZONTAL)
        pane.grid()
    def createLabelFrame(self):
        labelframe = LabelFrame(pane, text="My Label Frame", width=100, height=100)
        pane.add(labelframe)
    def createNoteBook(self, a):
        notebook = ttk.Notebook(a)
        f1 = Frame(root)
        f2 = Frame(root)
        # notebook.add(frame, text="My Frame")
        notebook.add(f1, text="F1")
        notebook.add(f2, text="f2")
        notebook.grid()
    def createImage(self):
        img = ImageTk.PhotoImage(Image.open(b"C:\Users\hp\Documents\Harman (Python Practice)\Tkinter\\boat2.png"))
    def createTreeView(self, a):
        tree = ttk.Treeview(a)
        tree.insert('', 'end', 'widgets', text='Widget Tour')
 
        # Same thing, but inserted as first child:
        tree.insert('', 0, 'gallery', text='Applications')

        # Treeview chooses the id:
        id = tree.insert('', 'end', text='Tutorial')

        # Inserted underneath an existing node:
        tree.insert('widgets', 'end', text='Canvas')
        tree.insert(id, 'end', text='Tree')
        tree.grid()
if __name__ == "__main__":
    root = MyExperimentalTkinterPrac()
    # root.createNoteBook(root)
    root.createFrame()
    # root.createNoteBook(root)
    root.createLabel(frame)
    root.createButton(frame)
    # root.createLabel(frame)
    # root.createLabel(frame)
    # root.createLabel(frame)
    # root.createLabel(frame)
    # root.createLabel(frame)
    # root.createLabel(frame)
    root.createRadioButton(frame)
    # root.createRadioButton(frame)
    root.createCheckBox(frame)
    root.createListBox(frame)
    root.createComboBox(frame)
    root.createEntry(frame)
    root.createTextWidget(frame)
    root.createMenu()
    root.createScrollBar(frame)
    root.createRangeScale(frame)
    # root.createTopLevelWidget()
    root.createSpinBox(frame)
    root.createProgressbar(frame)
    # root.createProgressbar()
    root.bindEvent()
    root.createContextualMenu(frame)
    if (root.tk.call('tk', 'windowingsystem')=='aqua'):
        root.bind('<2>', lambda e: menu2.post(e.x_root, e.y_root))
        root.bind('<Control-1>', lambda e: menu2.post(e.x_root, e.y_root))
    else:
        root.bind('<3>', lambda e: menu2.post(e.x_root, e.y_root))
    # root.protocol("WM_delete_window", )
    # root.attributes("-alpha", 1)
    # root.importColorChooser()
    # root.createAlertMessage()
    root.createPaneWindow(frame)
    root.createLabelFrame()
    root.createNoteBook(root)
    root.createImage()
    # root.createTreeView(frame)
    s = ttk.Style()
    # print(s.theme_names())
    # print(s.theme_use())
    s.theme_use("xpnative")
    # print(s.theme_use())
    root.mainloop()
    # print(dir(filedialog))
    