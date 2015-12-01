#! /usr/bin/env python
#coding=utf-8

from Tkinter import *


def donothing():
    filewin = Toplevel(top)
    button = Button(filewin, text="Do nothing button")
    button.pack()
    
def show_help():
    help_text = Text()
    
def create_menu(root):
    menubar = Menu(root)

    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="新建", command=donothing)
    filemenu.add_command(label="打开", command=donothing)
    filemenu.add_command(label="保存", command=donothing)
    filemenu.add_command(label="另存为", command=donothing)
    filemenu.add_separator()
    filemenu.add_command(label="退出", command=donothing)
    menubar.add_cascade(label="文件", menu=filemenu)
    
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="撤销")
    editmenu.add_command(label="恢复")
    
    editmenu.add_separator()
    editmenu.add_command(label="剪切")
    editmenu.add_command(label="复制")
    editmenu.add_command(label="粘贴")
    editmenu.add_command(label="删除")
    menubar.add_cascade(label="编辑", menu=editmenu)
    
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="关于", command=show_help)
    menubar.add_cascade(label="帮助", menu=helpmenu)

    return menubar


def main_window():
    root = Tk()
    root.wm_title("CodEditor demo")
    root.geometry('600x400+100+100')
    root.config(menu=create_menu(root))
    root.mainloop()
    
    
if __name__ == '__main__':
    main_window()