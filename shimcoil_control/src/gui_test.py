'''
Created on May 11, 2018

@author: klein
'''


import wx
import os
import Controller as CO
import wxmplot as PL # this will allow to creat plots
import numpy as np
import datetime as dt
from matplotlib.lines import drawStyles


class WXexample(wx.Frame):

    def __init__(self, parent, title):
        super(WXexample, self).__init__(parent, title=title,
            size=(800, 400))
        
    #initialize sockets
        self.MakeUI()
        self.SetupPlot()



        
    def MakeUI(self):
        pnl = wx.Panel(self)
        

          




        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        ExitItem = fileMenu.Append(wx.NewId(), 'Quit', 'Quit application')
        FileDialog = fileMenu.Append(wx.NewId(), 'File ', 'File Open')
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)
        
        # add simple radio button
        
        #just a simple radio button
        
        self.rb1 = wx.RadioButton(pnl,11, label = 'Shim heater relay1', pos = (10,10), style = wx.RB_GROUP)
        # get the current value fro the relay

        
          
        #bind the two radio buttons
        self.Bind(wx.EVT_RADIOBUTTON,self.OnRB1,self.rb1)
     
        # now we call the event method
        
# Bind the actions from the file menu
        self.Bind(wx.EVT_MENU, self.OnQuit,ExitItem)
        self.Bind(wx.EVT_MENU,self.OnOpenFile,FileDialog)
        


    def OnRB1(self,event):
        print 'We are doing the radio button'
        rbvalue = self.rb1.GetValue
        print "value of radio button is", rbvalue
        
    def OnOpenFile(self,event):
        '''
        here we open a file dialog

        
        '''
        wildcard = "*.par|*.*"

        dialog = wx.FileDialog(None, "Choose a file", os.getcwd(), "", wildcard, style = wx.FD_MULTIPLE)
        if dialog.ShowModal() == wx.ID_OK:
            print dialog.GetPaths() 
            self.FileName = dialog.GetPaths() # this opens several files
        dialog.Destroy()
        

        
    def OnQuit(self,event):
        print 'program exit'
        exit()
        
        
        
        
    def SetupPlot(self):
        '''
        this sets up the plots
        using the xmplot described on
        https://newville.github.io/wxmplot/plotpanel.html
        '''
        self.PL_FRAME=PL.PlotFrame(parent=None)
        self.PL_FRAME.set_title('tank level ')
        
        # here I play with a datetime array which will be the x
        start = dt.datetime(2000, 1, 1)
        starty=10.
        startx=2.
        
        
        #dt_array = np.array([start + dt.timedelta(hours=i) for i in range(24)])
        #Create emtpy numpy arrays
        x_array = np.array([]) 
        y_array =  np.array([])
        dt_array =  np.array([])
        # now append elements
        for k in range (10000):
            
            x_array = np.append(x_array,startx+k)
            dt_array = np.append(dt_array, start+ dt.timedelta(hours=k))
            #y_array = np.append(y_array,starty+k)
            y= np.random.random()
            y_array = np.append(y_array,np.sin(k)*y)
        print 
        
        self.PL_FRAME.plot(x_array,y_array,marker='*',
                    markersize=4,
                    drawstyles = 'steps-mid' )
        
        
        self.PL_FRAME.Show()

def main():

    app = wx.App()
    ex = WXexample(None, title='Shim Relay Control')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()

