#! /usr/bin/env python
#coding=utf-8

import Tkinter

top = Tkinter.Tk()
top.geometry('600x400+100+100')

File_Button = Tkinter.Button(top, text="File",justify='left')
Edit_Button = Tkinter.Button(top, text="Edit")

File_Button.pack()
Edit_Button.pack(after=File_Button)

top.mainloop()