#!/usr/bin/python3
import random, pyperclip, tkinter as tk
from tkinter import ttk, messagebox as mBox


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
                btn.grid(column = self.funIndex, row = 2, sticky = 'W', padx = (15, 15), pady = (5, 15))
                self.funIndex += 1

    def state(self):
        return map((lambda var: var.get()), self.vars)