#=============================================================================|
#  Python Program for a simple robust text editor                             |
#  Made by - Harun, contact: harunbajric@protonmail.com                       |
#=============================================================================|

###############
### Imports ###
###############
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from tkinter import ttk 
from tkinter import messagebox as mBox
from tkinter import scrolledtext
from functions import Functions
import subprocess
from subprocess import call


class gui():
################################
### Initialising instanaces  ###
################################
        def __init__(self):
                self.parent = tk.Tk()
                self.parent.title('Text Editor')
                self.create_widgets()
                self.create_menu()
        def create_widgets(self):
                child = LabelFrame(self.parent, text="Text Box", padx=5, pady=5)
                child.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky=E+W+N+S)
                self.parent.columnconfigure(0, weight=1)
                self.parent.rowconfigure(1, weight=1)
                child.rowconfigure(0, weight=1)
                child.columnconfigure(0, weight=1)
                
                self.textBox = scrolledtext.ScrolledText(child, width = 50, height = 20)
                self.textBox.grid(column = 0, row = 0, sticky = E+W+N+S)
                self.t = Functions(self.textBox)
                self.t.pack(fill='both', expand = 1)
                self.textBox.config(background='black', foreground = 'green')
                self.t.config(background='black', foreground='green')

        ############
        ### MENU ###
        ############
        def warning_Box(self):
                if mBox.askokcancel('Quit', 'Do you really want to quit?'):
                        self.parent.destroy()
        # Message box info
        def _messageBox(self):
                mBox.showinfo('About',  'A simple text editor made by ~Harun~. \n Contact: bajra1729@yandex.com')
        # Quit 
        def _quit(self):
                self.parent.quit()
                self.parent.destroy()
                exit()  
        # Save 
        def save(self):
                t = self.textBox.get("1.0", "end-1c")
                f = filedialog.asksaveasfile(mode='w', defaultextension=".py")
                if f is None: 
                        return
                t = str(self.textBox.get(1.0, END)) 
                f.write(t)
                f.close()
        def run(self):
                file = filedialog.askopenfile(mode = 'r')
                call(["python", str(file)])

         # Open file
        def copy(self):
                self.event_generate('<<Copy>>')
        def open_command(self):
                file = filedialog.askopenfile(mode = 'rb',title = 'Select a file')
                if file != None:
                        contents = file.read()
                        self.textBox.insert('1.0', contents)
                        file.close()

        # Fonts
        def FontHelvetica(self):
                self.textBox.config(font = 'Helvetica')
        def FontCourier(self):
                self.textBox.config(font = 'Courier')
        # Initialising menu
        def create_menu(self):
                menuBar = Menu(self.parent)
                self.parent.config(menu = menuBar)
                fileMenu = Menu(menuBar, tearoff = 0)
                helpMenu = Menu(menuBar, tearoff = 0)
                editMenu = Menu(menuBar, tearoff = 0)
                viewMenu = Menu(menuBar, tearoff = 0)
                # adding commands
                # fileMenu
                fileMenu.add_command(label = 'Open', command = self.open_command)
                fileMenu.add_command(label = 'Save', command = self.save)
                fileMenu.add_command(label = "Exit", command = self._quit)
                fileMenu.add_command(label = "Run", command  = self.run)
                menuBar.add_cascade(label = "File", menu = fileMenu)
                # edit menu
                editMenu.add_command(label="Copy",  command=self.copy)        
                # viewMenu
                viewMenu.add_command(label = 'Helvetica', command = self.FontHelvetica)
                viewMenu.add_command(label = 'Courier', command = self.FontCourier)
                menuBar.add_cascade(label = 'View', menu = viewMenu)
                menuBar.add_cascade(label = 'Edit', menu = editMenu)
                helpMenu.add_command(label = "About", command = self._messageBox)
                menuBar.add_cascade(label = "Help", menu = helpMenu)

        #################################
        ### Mainloop and other things ###
        #################################

oop = gui()
oop.parent.protocol("WM_DELETE_WINDOW", oop.warning_Box)     
oop.parent.mainloop()

