#! /usr/bin/env python
#coding=utf-8
'''
a wxPython Editor
'''

import wx

class Frame(wx.Frame):
    pass

class App(wx.App):
    def OnInit(self):
        self.frame = Frame(None, title="hehe")
        self.frame.Show()        
        return True
    
def main():
    app = App()
    app.MainLoop()
        
if __name__ == "__main__":
    main()