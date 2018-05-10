'''
Created on May 10, 2018

@author: klein
'''


# centering.py

import wx
import Controller as CO


class ControlShim(wx.Frame):

    def __init__(self, parent, title):
        super(ControlShim, self).__init__(parent, title=title,
            size=(300, 200))
        
    #initialize sockets
        ip_addr = '192.168.24.199'  #this is the address of the raspi
        self.tel =CO.Exchange(ip_addr)
        self.tel.Establish()


        self.MakeUI()
        
    def MakeUI(self):
        pnl = wx.Panel(self)

        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        fileItem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)
        
        # add simple radio button
        
        
        
        self.rb1 = wx.RadioButton(pnl,11, label = 'Shim heater relay1', pos = (10,10), style = wx.RB_GROUP)
        self.rb2 = wx.RadioButton(pnl,22, label = 'Shim heater relay2', pos = (10,60), style = wx.RB_GROUP)
        # get the current value fro the relay
        self.tel.ReadStateRelay()
        
        if self.tel.relay1_state=='1':
            self.rb1.SetValue(True)
        else:
            self.rb1.SetValue(False)
 
        if self.tel.relay2_state=='1':
            self.rb2.SetValue(True)
        else:
            self.rb2.SetValue(False)
            
        #bind the two radio buttons
        self.Bind(wx.EVT_RADIOBUTTON,self.OnRB1,self.rb1)
        self.Bind(wx.EVT_RADIOBUTTON,self.OnRB2,self.rb2)
      
        # now we call the event method
        

        self.Bind(wx.EVT_MENU, self.OnQuit, fileItem)

    def OnQuit(self, e):
        self.tel.ExitTransfer()
        self.tel.CloseAll()
        self.Close()
    
    def OnRB1(self,e):
        #print 'clicked relay button 1'
        self.tel.ReadStateRelay()
        if self.tel.relay1_state=='1':  # right now it is on, so we turn it off
            self.tel.SetRelay('D',1)
        else:
            self.tel.SetRelay('U',1)

        self.tel.ReadStateRelay()
        if self.tel.relay1_state=='1':
            self.rb1.SetValue(True)
        else:
            self.rb1.SetValue(False)

        return
           

      
        
    def OnRB2(self,e):
        #print 'clicked relay button 2'
        self.tel.ReadStateRelay()
        if self.tel.relay2_state=='1':  # right now it is on, so we turn it off
            self.tel.SetRelay('D',2)
        else:
            self.tel.SetRelay('U',2)

        self.tel.ReadStateRelay()

        if self.tel.relay2_state=='1':
            self.rb2.SetValue(True)
        else:
            self.rb2.SetValue(False)
        return
        
        
        
 





def main():

    app = wx.App()
    ex = ControlShim(None, title='Shim Relay Control')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()




