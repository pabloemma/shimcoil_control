'''
Created on May 3, 2018

@author: klein
'''

import socket
import sys
import os
import subprocess
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
	print ' connected to server'
    def GetSwitch(self):
        '''
	       here we listen for any changes in the relay switch
	    if we have one we change its with USBRELAY
	    '''

            # now we are looping

        while True:
            data = self.mysocket.recv(1024) 
            if (len(data)>0): 
                #print "this is the receiver and I got",data, len(data)
                print data 
                
                if(data == 'X'):
		    print 'Got hangup from server '
		    
		    break # finish loop here
		
		elif(data == 'R'):
		    print ' we got read command '
		    #create a subprocess
		    pi = subprocess.Popen('usbrelay',stdout=subprocess.PIPE)
		    relay_output = pi.communicate()[0]
		    #
		    
		    # this will give us two lines
		    #let's send the back to the server
		    self.mysocket.send(relay_output)
		    
		    #os.system("usbrelay > relay.dat")
		    #break
		elif( 'U' in data):
		
                    print ' we got a relay of UP ', data
		    command = data.partition(',')
                    os.system(command[2])		    
		    #break
                elif('D' in data):
                    print ' we got a relay of DOWN '
		    command = data.partition(',')
                    os.system(command[2])		    

		    #break
                else:
                    print ' invalid setting'
		    #break
	return

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
    ip_server = '192.168.24.198' # change for apporpitae server
    server_port = 5478
    
    MyPush = Push(ip_server,server_port)
    MyPush.Connect2Server()
    MyPush.GetSwitch()
    MyPush.CloseConnection()        
