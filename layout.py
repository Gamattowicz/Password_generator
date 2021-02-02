#!/usr/bin/python3

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mBox
from itertools import chain
import random
import pyperclip

#Special characters
spec_chr = [chr(i) for i in chain(range(33,48), range(58, 65), range(91, 97), range(123, 127))]

#Uppercase characters
upp_chr = [chr(i) for i in range(65, 91)]

#Lowercase characters
low_chr = [chr(i) for i in range(97, 123)]

#Numbers
num_chr = [chr(i) for i in range(48, 58)]

options = [spec_chr, upp_chr, low_chr, num_chr]

win = tk.Tk()
win.title('Password Generator')

values = [i for i in range(5, 21)]

def show_option():
    pass_area.delete(0, tk.END)
    
    length_pass = int(pass_len.get())
    new_password = ''
    possibility = []
    optionsIndex = [chVar1.get(), chVar2.get(), chVar3.get(), chVar4.get()]
    
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


chVar1 = tk.IntVar()
check_spec_chr = tk.Checkbutton(op_label, text = "Special Characters", variable = chVar1)
check_spec_chr.deselect()
check_spec_chr.grid(column = 0, row = 1, columnspan = 2, sticky = 'W', padx = (15, 10), pady = 5)

chVar2 = tk.IntVar()
check_upp_chr = tk.Checkbutton(op_label, text = "Uppercase Characters", variable = chVar2)
check_upp_chr.deselect()
check_upp_chr.grid(column = 0, row = 2, columnspan = 2, sticky = 'W', padx = (15, 10), pady = 5)

chVar3 = tk.IntVar()
check_low_chr = tk.Checkbutton(op_label, text = "Lowercase Characters", variable = chVar3)
check_low_chr.deselect()
check_low_chr.grid(column = 0, row = 3, columnspan = 2, sticky = 'W', padx = (15, 10), pady = 5)

chVar4 = tk.IntVar()
check_num_chr = tk.Checkbutton(op_label, text = "Numbers", variable = chVar4)
check_num_chr.deselect()
check_num_chr.grid(column = 0, row = 4, columnspan = 2, sticky = 'W', padx = (15, 10), pady = 5)


#Password 
password = tk.LabelFrame(win, text = 'Password', fg = 'green' )
password.grid(column = 0, row = 1, sticky = 'W', padx = 15, pady = (5, 15))
pass_area = tk.Entry(password, justify = 'center')
pass_area.grid(column = 0, row = 0, sticky = 'WE', columnspan = 3, padx = (15, 15), pady = 5)


#Buttons 
copy_btn = tk.Button(password, text = 'Copy', command = copy_option)
copy_btn.grid(column = 0, row = 2, sticky = 'W', padx = (15, 10), pady = (5, 15))

gen_btn = tk.Button(password, text = 'Generate', command = show_option)
gen_btn.grid(column = 1, row = 2, sticky = 'W', padx = (10, 10), pady = (5, 15))

quitbtn = tk.Button(password, text = ' Quit', command = win.quit)
quitbtn.grid(column = 2, row = 2, sticky = 'W', padx = (10, 15), pady = (5, 15))

win.mainloop()