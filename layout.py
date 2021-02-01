#!/usr/bin/python3

import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title('Password Generator')

values = [i for i in range(1, 20)]
    
def show_option():
    print(f'Special char: {chVar1.get()}, uppercase: {chVar2.get()}, lowercase: {chVar3.get()}, numbers: {chVar4.get()}')
    
#Password options
op_label = tk.LabelFrame(win, text = 'Options', fg = 'blue')
op_label.grid(column = 0, row = 0, columnspan = 2, sticky = 'WE', padx = 15, pady = (15, 10))

tk.Label(op_label, text = 'Password Length').grid(column = 0, row = 0, sticky = 'W', padx = (15, 10) , pady = (15, 5))

number = tk.StringVar
pass_len = ttk.Combobox(op_label, width = 3, textvariable = number)
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
pass_area = tk.Entry(password)
pass_area.grid(column = 0, row = 0, sticky = 'WE', padx = (10, 15), pady = 5)


#Buttons 
copy_btn = tk.Button(password, text = 'Copy')
copy_btn.grid(column = 0, row = 2, sticky = 'W', padx = (15, 10), pady = (5, 5))

gen_btn = tk.Button(password, text = 'Generate password')
gen_btn.grid(column = 1, row = 2, sticky = 'W', padx = (10, 15), pady = (5, 4))

checkbtn = tk.Button(password, text = 'Show', command = show_option)
checkbtn.grid(column = 0, row = 3, sticky = 'W', padx = (15, 10), pady = (5, 15))

quitbtn = tk.Button(password, text = ' Quit', command = win.quit)
quitbtn.grid(column = 1, row = 3, sticky = 'W', padx = (10, 15), pady = (5, 15))

win.mainloop()