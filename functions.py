import tkinter as tk
from tkinter import scrolledtext 
from tkinter import *

class Functions(Text):
    def __init__(self, master, **kw):
        Text.__init__(self, master, **kw)
        self.bind('<Control-a>', self.select_all)
        self.bind('<Control-A>', self.select_all)
        self.bind('<Control-Z>', '<<Undo>>')
        self.bind('<Control-z>', '<<Undo>>')
        self.bind('<Control-Y>', '<<Redo>>')
        self.bind('<Control-y>', '<<Redo>>')

    def select_all(self, event = None):
        self.tag_add(SEL, "1.0", "end-1c")
        self.mark_set(INSERT, "1.0")
        self.see(INSERT)
        return "break"

    def copy(self, event=None):
        self.clipboard_clear()
        text = self.get(SEL, "1.0", "end-1c")
        self.clipboard_append(text)  


if __name__ == '__main__':
    Functions()
