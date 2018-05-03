'''
Created on May 3, 2018

@author: klein
'''

import socket
import sys
from multiprocessing.connection import Client
class Push(object):
    '''
    classdocs
    '''


    def __init__(self,ip_server,server_port):
        '''
        Constructor
        '''
        self.raspi_server = ip_server # connect with ip of server
        self.raspi_port = server_port
    
    def Connect2Server(self):
        '''
        this establisk the socket connection with the server
        '''
        self.mysocket = socket.socket()  #use default protocol and stream
        # now connect to the server
        self.mysocket.connect((self.raspi_server,self.raspi_port))
    def GetSwitch(self):
        '''
	       here we listen for any changes in the relay switch
	    if we have one we change its with USBRELAY
	    '''
        conn,addr = self.mysocket.accept()
        print "got connectrion from " , addr

            # now we are looping

        while True:
            data = conn.recv(2) 
            if (len(data)>0): 
                #print "this is the receiver and I got",data, len(data)
                print data , " mm"
                data_int = int(data)
                if(data_int == 1):
                    print ' we got a relay of 1 '
                elif(data_int == 0):
                    print ' we got a relay of 0 '
                else:
                    print ' invalid setting'
        conn.send('thanks from raspi')
	

    def PushData(self,databuffer): 
        '''
        pushes data to server
        '''
        # make sure we know that we transmitted all the bytes
 
        temp=len(databuffer.encode('utf-8')) # length in bytes of databuffer, whih needs to be a string
        bytes_sent =self.mysocket.send(databuffer) # returns number of bytes sent
        
        if(temp - bytes_sent != 0):
            print "got ",temp," bytes  but sent ",bytes_sent,"  bytes"
        # get ack back from server
        response = self.mysocket.recv(1024)
        print response 
        
        
           
    def CloseConnection(self):  
        '''
        closes all connections
        '''
        self.mysocket.close()
         
if __name__ == '__main__':
    ip_server = '169.254.104.3' # change for apporpitae server
    server_port = 5478
    
    MyPush = Push(ip_server,server_port)
    MyPush.Connect2Server()
    #MyPush.PushData('R0430')
    MyPush.GetSwitch()
    MyPush.CloseConnection()        
