#!/usr/bin/python3
import random, pyperclip, tkinter as tk
from tkinter import ttk, messagebox as mBox
from itertools import chain
from PasswordCreator import BtnCreate

# Special characters
spec_chr = [chr(i) for i in chain(range(33,48), range(58, 65), range(91, 97), range(123, 127))]
# Uppercase characters
upp_chr = [chr(i) for i in range(65, 91)]
# Lowercase characters
low_chr = [chr(i) for i in range(97, 123)]
# Numbers
num_chr = [chr(i) for i in range(48, 58)]


class PasswordCreate:
    def __init__(self, options = [], password_length = '', btn = '', password_area = ''):
        self.options = options
        self.password_area = password_area
        self.password_length = password_length
        self.password_new = ''
        self.possibility = []
        self.btn = btn

    def gen_password(self):
        self.password_area.delete(0, tk.END)
        self.options_index = list(self.btn.state())
        for i in range(len(self.options)):
            if self.options_index[i] == 1:
                self.possibility.extend(self.options[i])
        if len(self.possibility) < 1:
            return mBox.showwarning('Warning', 'You must select at least one of the options')
        for i in range(0, int(self.password_length.get())):
            self.password_new += random.choice(self.possibility)
        print(self.password_new)
        self.password_area.insert(10, self.password_new)
        self.password_new = ''

    def copy_password(self):
        pyperclip.copy(self.password_area.get())


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

