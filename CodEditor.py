#! /usr/bin/env python
#coding=utf-8

from Tkinter import *
import tkMessageBox
from FileDialog import *


WIDTH=600
HEIGHT=400
filename = ""

def open_file():
    global text_Window
    fd = LoadFileDialog(root)
    filename=fd.go()
    f  = open(""+filename,'r')
    content = f.read()
    length = len(content)
    text_Window.delete('1.0', '99999999.0')
    text_Window.insert(END, content)

def save_file():
    pass

def donothing():
    pass
    '''filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button")
    button.pack()'''
    
def show_help():
    tkMessageBox.showinfo("about", "Cod Editor demo")
    
def create_menu(root):
    menubar = Menu(root)

    right_menu = Menu(root)

    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label='新建', command=donothing)
    filemenu.add_command(label='打开', command=open_file)
    filemenu.add_command(label='保存', command=donothing)
    filemenu.add_command(label='另存为', command=donothing)    
    filemenu.add_separator()
    filemenu.add_command(label="退出", command=donothing)
    
    
    editmenu = Menu(menubar, tearoff=0)
    for item in ['撤销','恢复']:
        editmenu.add_command(label=item)
    editmenu.add_separator()
    for item in ['剪切','复制','粘贴','删除']:
        editmenu.add_command(label=item)
   
    
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="关于", command=show_help)

    
    menubar.add_cascade(label="文件", menu=filemenu)
    menubar.add_cascade(label="编辑", menu=editmenu)
    menubar.add_cascade(label="帮助", menu=helpmenu)


    for x in ['复制', '剪切', '粘贴']:
        right_menu.add_command(label=x, command=show_help)
    def pop(event):
        right_menu.post(event.x_root, event.y_root)
    root.bind("<Button-3>", pop)
        
    return menubar



root = Tk()
root.wm_title("CodEditor demo")
root.geometry('600x400+100+100')
    
text_Window=Text(root)
text_Window.pack(expand=YES, fill=BOTH)
scroll = Scrollbar(text_Window)
text_Window.config(yscrollcommand=scroll.set)
scroll.config(command=text_Window.yview)
scroll.pack(side=RIGHT, fill=Y)
root.config(menu=create_menu(root))
root.mainloop()
