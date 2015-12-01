#! /usr/bin/env python
#coding=utf-8

from Tkinter import *

WIDTH=600
HEIGHT=400


def donothing():
    pass
    '''filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button")
    button.pack()'''
    
def show_help():
    pass
    
def create_menu(root):
    menubar = Menu(root)

    filemenu = Menu(menubar, tearoff=0)
    for item in ['新建','打开','保存','另存为']:
        filemenu.add_command(label=item, command=donothing)
    filemenu.add_separator()
    filemenu.add_command(label="退出", command=donothing)
    menubar.add_cascade(label="文件", menu=filemenu)
    
    editmenu = Menu(menubar, tearoff=0)
    for item in ['撤销','恢复']:
        editmenu.add_command(label=item)
    
    editmenu.add_separator()
    for item in ['剪切','复制','粘贴','删除']:
        editmenu.add_command(label=item)
    menubar.add_cascade(label="编辑", menu=editmenu)
    
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="关于", command=show_help)
    menubar.add_cascade(label="帮助", menu=helpmenu)

    return menubar


def main_window():
    root = Tk()
    root.wm_title("CodEditor demo")
    root.geometry('600x400+100+100')
    
    e=Entry(root, width=WIDTH)
    e.pack()
    root.config(menu=create_menu(root))
    root.mainloop()
    
    
if __name__ == '__main__':
    main_window()