#! /usr/bin/env python
#coding=utf-8
'''
a wxPython Editor
'''

import wx

class Frame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title)
        panel = wx.Panel(self)
        statusBar = self.CreateStatusBar()
        menuBar = wx.MenuBar()
        menu_File = wx.Menu()
        menu_File.Append(wx.NewId(), "&New")
        menu_File.Append(wx.NewId(), "&Open")
        menu_File.Append(wx.NewId(), "&Save")
        menu_File.AppendSeparator()
        menu_File.Append(wx.NewId(), "&Close")        
        menu_File.AppendSeparator()
        menu_File.Append(wx.NewId(), "Quit")
        
        menuBar.Append(menu_File, "&File")
        
        
        menu_Edit = wx.Menu()
        menu_Edit.Append(wx.NewId(), "&Cut")
        menu_Edit.Append(wx.NewId(), "&Copy")
        menu_Edit.Append(wx.NewId(), "&Paste")
        menuBar.Append(menu_Edit, "&Edit")
        self.SetMenuBar(menuBar)
        

class App(wx.App):
    def OnInit(self):
        self.frame = Frame(None, id=-1, title="CodEditor2 Demo")
        self.frame.Show()        
        return True
    
def main():
    app = App()
    app.MainLoop()
        
if __name__ == "__main__":
    main()