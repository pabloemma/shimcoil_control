This is the simple file to control the shim heaters.
There are two relays on the USB board. To run the system, you need to install usbrelay on the raspi.
With debian this is simply
apt install usbrealy.
Then you need to get data_push.py onto the raspi.
On the server machine, you need to install wx python. for simple GUI and run the ControlShim.py
If you dont have wx python, you can also run Controller.py (chnage the parameters at the bottom)
You need to get the IP address of both the server and the RASPI since they are hardwired.

First start the controller program on the server, then start the program on the RASPI.