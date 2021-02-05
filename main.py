#!/usr/bin/python3
import random, pyperclip, tkinter as tk
from tkinter import ttk, messagebox as mBox
from itertools import chain
import random, pyperclip


class BtnCreate:
    def __init__(self, parent, names = [], type = 'chck', commands = []):
        self.parent = parent
        self.vars = []
        self.rowIndex = 1
        self.commands = commands
        self.funIndex = 0
        if type == 'chck':
            for name in names:
                chVar = tk.IntVar()
                chckBox = tk.Checkbutton(self.parent, text = name, variable = chVar)
                chckBox.grid(column = 0, row = self.rowIndex, columnspan = 2, sticky = 'W', padx = (15, 10), pady = 5)
                self.vars.append(chVar)
                self.rowIndex += 1
        elif type == 'btn':
            for name in names:
                btn = tk.Button(parent, text = name, command = self.commands[self.funIndex])
                btn.grid(column = self.funIndex, row = 2, sticky = 'W', padx = (15, 10), pady = (5, 15))
                self.funIndex += 1

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


class CreateWindow:
    def __init__(self, title = 'Title', password_range = (5, 10)):
        self.win = tk.Tk()
        self.win.title(title)
        self.password_range = [i for i in range(password_range)]


class CreateLable:
    def __init__(self, type = 'Label', parent = 'root', text = '', font_color = 'black', col = 0, row = 0, colspan = 1, sticky = 'W', paddingX = 0, paddingY = 0):
        if type == 'Label_Frame':
            lbl_frame = tk.LabelFrame(parent, text = text, fg = font_color)
            lbl_frame.grid(column = col, row = row , columnspan = colspan, sticky = sticky , padx = paddingX, pady = paddingY)
        elif type == 'Label':
            lbl = tk.Label(parent, text = text)
            lbl.grid(column = col, row = row , columnspan = colspan, sticky = sticky , padx = paddingX, pady = paddingY)


class CreateComboBox:
    def __init__(self):
        pass


if __name__ == '__main__':

    win = tk.Tk()
    win.title('Password Generator')
    values = [i for i in range(5, 21)]

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


    # Align buttons
    random_password = PasswordCreate([spec_chr, upp_chr, low_chr, num_chr], pass_len, check_boxes, pass_area)
    btns = BtnCreate(password, ['Copy', 'Generate', ' Quit'], 'btn', [random_password.copy_password, random_password.gen_password, win.quit])

    win.mainloop()

