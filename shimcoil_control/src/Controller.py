'''
Created on May 1, 2018

@author: klein

This is the server
we communicate to the relay with the follwing commands:
R: give state of relay
U: Up turn relay on
D: Down turn relay off

'''

import socket
import sys

import numpy as np



from multiprocessing.connection import Client


class Exchange(object):
    '''
    classdocs
    '''


    def __init__(self,ip_addr):
        '''
        Constructor
        '''
        self.ip_addr = ip_addr
        
    
    def Establish(self):
        '''
        establish connection with Client
        on address ip_addr. We are using port 5478
        '''
        self.mysock = socket.socket() # create socket
        myip = self.ip_addr
        myport = 5478
        self.mysock.bind(('',myport))
        self.mysock.listen(5) # start listening
        self.conn,self.addr = self.mysock.accept() # connection address pair
        print "got connection form in establish ",self.addr

    def ReadStateRelay(self):
        '''
        Get the USB real state
        we send a read character to the client and get the answer back
        '''
        self.conn.send('R')
        
        # get repsonse
        while True:
            # wait for data
            data = self.conn.recv(1024)
            #if not data: break
            if (len(data)>0): 
                #print "this is the receiver and I got",data, len(data)
                #print data 
                # lets find the name of the relays
                relay = data.splitlines() # this gives us a list with name xxx=0
                # next step is to strip the =0 or =1
                help1 = relay[0].partition('=')
                help2 = relay[1].partition('=')
                self.relay1 = help1[0]
                self.relay2 = help2[0]
                self.relay1_state = help1[2]
                self.relay2_state = help2[2]
#                print 'the relay names are',self.relay1, self.relay2
                
            #self.conn.send('thanks from server')
            break
                #self.scope.emitter(int(data))
            #conn.close()
        #print'relay value sent'
        return 
        
        
    def Looping(self):
        '''
        Here we listen for the Client
        '''

        while True:
            # wait for data
            data =  self.conn.recv(1024)
            #if not data: break
            if (len(data)>0): 
                #print "this is the receiver and I got",data, len(data)
                print data , " mm"
                if(len(data)==4):
                    fl_data = int(data)
                else:
                    fl_data = 1
            self.conn.send('thanks from server')
                #self.scope.emitter(int(data))
            #conn.close()
    def SetRelay(self,status=None, relay=None):
        '''
        this pushes the relay setting for the USB relay on the raspi
        when it is triggered it send the value 1 or 0, by default the switch heater is on
        status is either U or D
        relay = 1 or 2
        '''
        data=''
        if(relay==1):
            data=self.relay1
        elif(relay==2):
            data=self.relay2
        # form the command
        if(status == 'U'):
            command = 'U,usbrelay '+data+'=1'
        elif(status == 'D'):
            command = 'D,usbrelay '+data+'=0'
        else:
            print 'invalid signal'
            self.CloseAll()

        self.conn.send(command)
  

        return
    def ExitTransfer(self): 
        self.conn.send('X')
        self.CloseAll()
        return
 
          
        
    def CloseAll(self):
        #self.mysock.shutdown(socket.SHUT_RDWR)
        self.mysock.close()
        print ' going away'
        sys.exit(0)
        
            
if __name__ == '__main__':
    ip_addr = '192.168.24.199'  #this is the address of the raspi
    tel =Exchange(ip_addr)
    tel.Establish()
    #tel.Looping()
   # tel.PushSwitchRelay(status='1')
    tel.ReadStateRelay()
    tel.SetRelay('U',1)
    #tel.PushSwitchRelay('D') # turn relay off
    tel.ExitTransfer()
    tel.CloseAll()
 