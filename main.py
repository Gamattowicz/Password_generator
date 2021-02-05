#!/usr/bin/python3
import tkinter as tk
from itertools import chain
from ButtonCreator import BtnCreate
from PasswordCreator import PasswordCreate
from tkinter import ttk

# Special characters
spec_chr = [chr(i) for i in chain(range(33,48), range(58, 65), range(91, 97), range(123, 127))]
# Uppercase characters
upp_chr = [chr(i) for i in range(65, 91)]
# Lowercase characters
low_chr = [chr(i) for i in range(97, 123)]
# Numbers
num_chr = [chr(i) for i in range(48, 58)]


if __name__ == '__main__':
    win = tk.Tk()
    win.title('Password Generator')
    values = [i for i in range(5, 21)]
    # Create password options label frame and label
    options_label_frame = tk.LabelFrame(win, text = 'Options', fg = 'blue')
    options_label_frame.grid(column = 0, row = 0, columnspan = 2, sticky = 'WE', padx = 15, pady = (15, 10))
    options_label = tk.Label(options_label_frame, text = 'Password Length')
    options_label.grid(column = 0, row = 0, sticky = 'W', padx = (15, 10) , pady = (15, 5))
    # Create combobox with password length selection
    number = tk.StringVar
    pass_len = ttk.Combobox(options_label_frame, width = 3, textvariable = number, state = 'readonly')
    pass_len['values'] = values
    pass_len.grid(column = 1, row = 0, sticky = 'W', padx = 10, pady = (15, 5))
    pass_len.current(0)
    # Create buttons with password options selection
    check_boxes = BtnCreate(options_label_frame, ['Special Characters', 'Uppercase Characters', 'Lowercase Characters', 'Numbers'], 'chck')
    # Create password label frame and label
    password = tk.LabelFrame(win, text = 'Password', fg = 'green' )
    password.grid(column = 0, row = 1, sticky = 'W', padx = 15, pady = (5, 15))
    pass_area = tk.Entry(password, justify = 'center')
    pass_area.grid(column = 0, row = 0, sticky = 'WE', columnspan = 3, padx = (15, 15), pady = 5)
    # Create password
    random_password = PasswordCreate([spec_chr, upp_chr, low_chr, num_chr], pass_len, check_boxes, pass_area)
    # Create buttons with copy, generate and quit function
    btns = BtnCreate(password, ['Copy', 'Generate', ' Quit'], 'btn', [random_password.copy_password, random_password.gen_password, win.quit])
    win.mainloop()

