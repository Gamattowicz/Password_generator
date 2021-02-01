import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title('Password Generator')

values = [i for i in range(1, 20)]
#Password options
ttk.Label(win, text = 'Password Length').grid(column = 0, row = 0, sticky = 'W', padx = (15, 10), pady = (15, 5))

number = tk.StringVar
pass_len = ttk.Combobox(win, width = 3, textvariable = number)
pass_len['values'] = values
pass_len.grid(column = 1, row = 0, sticky = 'W', padx = 10, pady = (15, 5))
pass_len.current(0)



chVar1 = tk.IntVar()
check_spec_chr = tk.Checkbutton(win, text = "Special Characters", variable = chVar1)
check_spec_chr.deselect()
check_spec_chr.grid(column = 0, row = 1, columnspan = 2, sticky = 'W', padx = (15, 10), pady = 5)

chVar2 = tk.IntVar()
check_upp_chr = tk.Checkbutton(win, text = "Uppercase Characters", variable = chVar2)
check_upp_chr.deselect()
check_upp_chr.grid(column = 0, row = 2, columnspan = 2, sticky = 'W', padx = (15, 10), pady = 5)

chVar3 = tk.IntVar()
check_low_chr = tk.Checkbutton(win, text = "Lowercase Characters", variable = chVar3)
check_low_chr.deselect()
check_low_chr.grid(column = 0, row = 3, columnspan = 2, sticky = 'W', padx = (15, 10), pady = 5)

chVar4 = tk.IntVar()
check_num_chr = tk.Checkbutton(win, text = "Numbers", variable = chVar4)
check_num_chr.deselect()
check_num_chr.grid(column = 0, row = 4, columnspan = 2, sticky = 'W', padx = (15, 10), pady = 5)


#Password 

password = ttk.Label(win, text = 'Password')
password.grid(column = 0, row = 5, sticky = 'W', padx = (15, 10), pady = 5)
pass_area = ttk.Entry(win)
pass_area.grid(column = 1, row = 5, sticky = 'W', padx = (10, 15), pady = 5)


#Buttons 
copy_btn = ttk.Button(win, text = 'Copy')
copy_btn.grid(column = 0, row = 6, sticky = 'W', padx = (15, 10), pady = (5, 15))

gen_btn = ttk.Button(win, text = 'Generate password')
gen_btn.grid(column = 1, row = 6, sticky = 'W', padx = (15, 10), pady = (5, 15))

win.mainloop()