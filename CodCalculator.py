#! /usr/bin/env python
#coding=utf-8

import wx


class CalFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(300, 300))
        panel = wx.Panel(self, -1)
        
        self.button1 = wx.Button(panel, -1, "1", pos=(50, 40), size= (30, 30))
        self.button2 = wx.Button(panel, -1, "2", pos=(100, 40), size= (30, 30))
        self.button3 = wx.Button(panel, -1, "3", pos=(150, 40), size= (30, 30))
        self.buttonAdd = wx.Button(panel, -1, "+", pos=(200, 40), size= (30, 30))
        self.button4 = wx.Button(panel, -1, "4", pos=(50, 90), size= (30, 30))
        self.button5 = wx.Button(panel, -1, "5", pos=(100, 90), size= (30, 30))
        self.button6 = wx.Button(panel, -1, "6", pos=(150, 90), size= (30, 30))
        self.buttonMinus = wx.Button(panel, -1, "-", pos=(200, 90), size= (30, 30))
        self.button7 = wx.Button(panel, -1, "7", pos=(50, 140), size= (30, 30))
        self.button8 = wx.Button(panel, -1, "8", pos=(100, 140), size= (30, 30))
        self.button9 = wx.Button(panel, -1, "9", pos=(150, 140), size= (30, 30))
        self.buttonMul = wx.Button(panel, -1, "x", pos=(200, 140), size= (30, 30))
        self.button0 = wx.Button(panel, -1, "0", pos=(50, 190), size= (30, 30))
        self.buttonClear = wx.Button(panel, -1, "C", pos=(100, 190), size=(30, 30))
        self.buttonEqual = wx.Button(panel, -1, "=", pos=(150, 190), size=(30, 30))
        self.buttonDiv = wx.Button(panel, -1, "/", pos=(200, 190), size=(30, 30))
        
        self.Bind(wx.EVT_BUTTON, self.OnOne, self.button1)
        self.Bind(wx.EVT_BUTTON, self.OnTwo, self.button2)
        self.Bind(wx.EVT_BUTTON, self.OnThree, self.button3)
        self.Bind(wx.EVT_BUTTON, self.OnFour, self.button4)
        self.Bind(wx.EVT_BUTTON, self.OnFive, self.button5)
        self.Bind(wx.EVT_BUTTON, self.OnSix, self.button6)
        self.Bind(wx.EVT_BUTTON, self.OnSeven, self.button7)
        self.Bind(wx.EVT_BUTTON, self.OnEight, self.button8)
        self.Bind(wx.EVT_BUTTON, self.OnNine, self.button9)
        self.Bind(wx.EVT_BUTTON, self.OnZero, self.button0)
        self.Bind(wx.EVT_BUTTON, self.OnEqual, self.buttonEqual)
        self.Bind(wx.EVT_BUTTON, self.OnAdd, self.buttonAdd)
        self.Bind(wx.EVT_BUTTON, self.OnMinus, self.buttonMinus)
        self.Bind(wx.EVT_BUTTON, self.OnMul, self.buttonMul)
        self.Bind(wx.EVT_BUTTON, self.OnDiv, self.buttonDiv)
        self.Bind(wx.EVT_BUTTON, self.OnClear, self.buttonClear) 
        
        self.text_ctrl_1 = wx.TextCtrl(panel, -1, "", style=wx.TE_READONLY, pos=(50, 0),size=(180, 30))
        
    def OnClear(self, event):
        self.text_ctrl_1.SetValue("")
    
    def OnEqual(self, event):
        self.num2 = self.text_ctrl_1.GetValue()
        num1 = int(self.num1)
        num2 = int(self.num2)
        if self.op == "+":
            self.text_ctrl_1.SetValue(str(num1+num2))
        elif self.op == "-":
            self.text_ctrl_1.SetValue(str(num1-num2))
        elif self.op == "x":
            self.text_ctrl_1.SetValue(str(num1*num2))
        elif self.op == "/":
            if num2 == 0:
                self.text_ctrl_1.SetValue("Zero diver")
            else:
                self.text_ctrl_1.SetValue(str(num1/num2))
        
    
    def OnAdd(self, event):
        self.num1 = self.text_ctrl_1.GetValue()
        print self.num1
        self.op="+"
        #self.text_ctrl_1.Clear()
        
    def OnMinus(self, event):
        self.num1 = self.text_ctrl_1.GetValue()
        print self.num1
        self.op="-"
        #self.text_ctrl_1.Clear()
        
    def OnMul(self, event):
        self.num1 = self.text_ctrl_1.GetValue()
        print self.num1
        self.op="x"
        #self.text_ctrl_1.Clear()
        
    def OnDiv(self, event):
        self.num1 = self.text_ctrl_1.GetValue()
        print self.num1
        self.op="/"
        #self.text_ctrl_1.Clear()
    
    def OnOne(self, event):
        self.text_ctrl_1.SetValue("")
        print '1'
        self.text_ctrl_1.AppendText('1')
        
    def OnTwo(self, event):
        self.text_ctrl_1.SetValue("")
        print '2'
        self.text_ctrl_1.AppendText('2')
        
    def OnThree(self, event):
        self.text_ctrl_1.SetValue("")
        print '3'
        self.text_ctrl_1.AppendText('3')
        
    def OnFour(self, event):
        self.text_ctrl_1.SetValue("")
        print '4'
        self.text_ctrl_1.AppendText('4')
        
    def OnFive(self, event):
        self.text_ctrl_1.SetValue("")
        print '5'
        self.text_ctrl_1.AppendText('5')
        
    def OnSix(self, event):
        self.text_ctrl_1.SetValue("")
        print '6'
        self.text_ctrl_1.AppendText('6')
        
    def OnSeven(self, event):
        self.text_ctrl_1.SetValue("")
        print '7'
        self.text_ctrl_1.AppendText('7')
    
    def OnEight(self, event):
        self.text_ctrl_1.SetValue("")
        print '8'
        self.text_ctrl_1.AppendText('8')
        
    def OnNine(self, event):
        self.text_ctrl_1.SetValue("")
        print '9'
        self.text_ctrl_1.AppendText('9')
        
    def OnZero(self, event):
        self.text_ctrl_1.SetValue("")
        print '0'
        self.text_ctrl_1.AppendText('0')


class myApp(wx.App):
    def OnInit(self):
        self.frame = CalFrame(None, id=-1, title="Calculator")
        self.frame.Show()
        return True

def main():
    app = myApp()
    app.MainLoop()  

if __name__ == '__main__':
    main()