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
        print "got connection form ",self.addr

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
                print data , " mm"
            self.conn.send('thanks from server')
            break
                #self.scope.emitter(int(data))
            #conn.close()
        return 'relay value sent'
        
        
    def Looping(self):
        '''
        Here we listen for the Client
        '''

        while True:
            # wait for data
            data = conn.recv(1024)
            #if not data: break
            if (len(data)>0): 
                #print "this is the receiver and I got",data, len(data)
                print data , " mm"
                if(len(data)==4):
                    fl_data = int(data)
                else:
                    fl_data = 1
            conn.send('thanks from server')
                #self.scope.emitter(int(data))
            #conn.close()
    def PushSwitchRelay(self,status='1'):
        '''
        this pushes the relay setting for the USB relay on the raspi
        when it is triggered it send the value 1 or 0, by default the switch heater is on
        '''
        conn,addr = self.mysock.accept() # connection address pair
        print "got connection form ",addr

        conn.send(status)
        return
        
        
    def CloseAll(self):
        self.mysock.close()
        print ' going away'
        sys.exit(0)
        
            
if __name__ == '__main__':
    ip_addr = '169.254.104.11'  #this is the address of the raspi
    tel =Exchange(ip_addr)
    tel.Establish()
    #tel.Looping()
    tel.PushSwitchRelay(status='1')
    tel.CloseAll()
 