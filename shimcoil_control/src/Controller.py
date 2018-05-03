'''
Created on May 1, 2018

@author: klein
'''

import socket
import sys

import numpy as np



from multiprocessing.connection import Client


class Exchange(object):
    '''
    classdocs
    '''


    def __init__(self,ip_addr=ip_addr):
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
        
    def Looping(self):
        '''
        Here we listen for the Client
        '''
        conn,addr = self.mysock.accept() # connection address pair
        print "got connection form ",addr

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
    def CloseAll(self):
        self.mysock.close()
        print ' going away'
        sys.exit(0)
        
            
if __name__ == '__main__':
    ip_addr = '204.121.146.110'
    tel =Exchange()
    tel.Establish()
    tel.Looping()
    tel.CloseAll()
 