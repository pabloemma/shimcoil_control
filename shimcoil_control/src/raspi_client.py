'''
Created on May 3, 2018

@author: klein
'''

import data_push as dp
if __name__ == '__main__':
    #establish connection
    ip_server = '204.121.140.2' # change for apporpitae server
    #ip_server = '192.168.2.41' # change for apporpitae server
    server_port = 5478
    # serial connection device
    device_name = '/dev/ttyAMA0'

    
    MyPush = dp.Push(ip_server,server_port)
    MyPush.Connect2Server()
    MyPush.PushData(data)

    
    MyPush.CloseConnection()    
