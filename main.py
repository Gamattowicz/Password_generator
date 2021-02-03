#!/usr/bin/python3

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mBox
from itertools import chain
import random
import pyperclip

class BtnCreate():
   def __init__(self, parent, names = [], type = 'chck', commands = []):
      self.parent = parent
      self.vars = []
      rowIndex = 1
      self.commands = commands
      funIndex = 0
      if type == 'chck':
         for name in names:
            chVar = tk.IntVar()
            chckBox = tk.Checkbutton(self.parent, text = name, variable = chVar)
            chckBox.grid(column = 0, row = rowIndex, columnspan = 2, sticky = 'W', padx = (15, 10), pady = 5)
            self.vars.append(chVar)
            rowIndex += 1
      elif type == 'btn':
         for name in names:
            btn = tk.Button(parent, text = name, command = self.commands[funIndex])
            btn.grid(column = funIndex, row = 2, sticky = 'W', padx = (15, 10), pady = (5, 15))
            funIndex += 1
   def state(self):
      return map((lambda var: var.get()), self.vars)
            
#Special characters
spec_chr = [chr(i) for i in chain(range(33,48), range(58, 65), range(91, 97), range(123, 127))]

#Uppercase characters
upp_chr = [chr(i) for i in range(65, 91)]

#Lowercase characters
low_chr = [chr(i) for i in range(97, 123)]

#Numbers
num_chr = [chr(i) for i in range(48, 58)]

options = [spec_chr, upp_chr, low_chr, num_chr]         

if __name__ == '__main__':
   win = tk.Tk()
   win.title('Password Generator')
   values = [i for i in range(5, 21)]
   
   def show_option():
      pass_area.delete(0, tk.END)
    
      length_pass = int(pass_len.get())
      new_password = ''
      possibility = []
      optionsIndex = list(check_boxes.state())
    
      for i in range(4):
         if optionsIndex[i] == 1:
               possibility.extend(options[i])
            
      if len(possibility) < 1:
         return mBox.showwarning('Warning', 'You must select at least one of the options')
      
      for i in range(0, length_pass):
         new_password += random.choice(possibility)
         
      print(new_password)
      pass_area.insert(10, new_password)

   def copy_option():
      copy_password = pass_area.get()
      pyperclip.copy(copy_password)
    
   #Password options
   op_label = tk.LabelFrame(win, text = 'Options', fg = 'blue')
   op_label.grid(column = 0, row = 0, columnspan = 2, sticky = 'WE', padx = 15, pady = (15, 10))

   tk.Label(op_label, text = 'Password Length').grid(column = 0, row = 0, sticky = 'W', padx = (15, 10) , pady = (15, 5))

   number = tk.StringVar
   pass_len = ttk.Combobox(op_label, width = 3, textvariable = number, state = 'readonly')
   pass_len['values'] = values
   pass_len.grid(column = 1, row = 0, sticky = 'W', padx = 10, pady = (15, 5))
   pass_len.current(0)
   
   
   check_boxes = BtnCreate(op_label, ['Special Characters', 'Uppercase Characters', 'Lowercase Characters', 'Numbers'], 'chck')
   password = tk.LabelFrame(win, text = 'Password', fg = 'green' )
   password.grid(column = 0, row = 1, sticky = 'W', padx = 15, pady = (5, 15))
   pass_area = tk.Entry(password, justify = 'center')
   pass_area.grid(column = 0, row = 0, sticky = 'WE', columnspan = 3, padx = (15, 15), pady = 5)
   btns = BtnCreate(password, ['Copy', 'Generate', ' Quit'], 'btn', [copy_option, show_option, win.quit])

   win.mainloop()

