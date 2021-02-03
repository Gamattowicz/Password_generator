#!/usr/bin/python3

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mBox
from itertools import chain
import random
import pyperclip

class ChckBtnCreate():
   def __init__(self, parent, names = []):
      self.parent = parent
      rowIndex = 1
      for name in names:
         chVar = tk.IntVar()
         chckBtn = tk.Checkbutton(self.parent, text = name, variable = chVar)
         chckBtn.grid(column = 0, row = rowIndex, columnspan = 2, sticky = 'W', padx = (15, 10), pady = 5)
         rowIndex += 1


if __name__ == '__main__':
   win = tk.Tk()
   win.title('Password Generator')
   lng = ChckBtnCreate(win, ['Special Characters', 'Uppercase Characters', 'Lowercase Characters', 'Numbers'])


   win.mainloop()

