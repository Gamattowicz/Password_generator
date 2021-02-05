#!/usr/bin/python3
import random, pyperclip, tkinter as tk
from tkinter import ttk, messagebox as mBox


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