import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title('Password Generator')

values = [i for i in range(1, 20)]
#Password options
number = tk.StringVar
pass_len = ttk.Combobox(win, width = 3, textvariable = number)

pass_len['values'] = values
pass_len.grid(column = 1, row = 0, sticky = 'W')
pass_len.current(0)
ttk.Label(win, text = 'Password Length').grid(column = 0, row = 0, sticky = 'W')


chVar1 = tk.IntVar()
check_spec_chr = tk.Checkbutton(win, text = "Special Characters (e.g. &!@`}", variable = chVar1)
check_spec_chr.deselect()
check_spec_chr.grid(column = 0, row = 1, sticky = 'W')

chVar2 = tk.IntVar()
check_upp_chr = tk.Checkbutton(win, text = "Uppercase Characters (e.g. ABCDE)", variable = chVar2)
check_upp_chr.deselect()
check_upp_chr.grid(column = 0, row = 2, sticky = 'W')

chVar3 = tk.IntVar()
check_low_chr = tk.Checkbutton(win, text = "Lowercase Characters (e.g. abcde)", variable = chVar3)
check_low_chr.deselect()
check_low_chr.grid(column = 0, row = 3, sticky = 'W')

chVar4 = tk.IntVar()
check_num_chr = tk.Checkbutton(win, text = "Numbers (e.g. 12345)", variable = chVar4)
check_num_chr.deselect()
check_num_chr.grid(column = 0, row = 4, sticky = 'W')


#Password 

password = ttk.Label(win, text = 'Password')
password.grid(column = 0, row = 5, sticky = 'W')
pass_area = ttk.Entry(win)
pass_area.grid(column = 1, row = 5, sticky = 'W')


#Buttons 
copy_btn = ttk.Button(win, text = 'Copy')
copy_btn.grid(column = 0, row = 6, sticky = 'W')

gen_btn = ttk.Button(win, text = 'Generate password')
gen_btn.grid(column = 1, row = 6, sticky = 'W')

win.mainloop()