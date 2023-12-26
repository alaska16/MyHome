# MyHome Server v0.1
import logging
import socket
from tkinter import *

# To figure out later: is it better to send all the data in one single "cycle" or should it close the socket every time?

# -- Variables --
SERVER_HOST = "0.0.0.0"
logging.info("Server is configured to listen to all IP adresses of this system.")
SERVER_PORT = 5555
BUFFER_SIZE = 4096
logging.info("Buffer size : 4096")
SEPARATOR = "<SEPARATOR>"

# -- Interface --
serverdebugwindow = Tk()
t_livingroom = IntVar()
t_room1 = IntVar()
t_room2 = IntVar()
# - Living room -
slider_livingroom = Scale(serverdebugwindow, label = "Living room", variable= t_livingroom)
slider_livingroom.pack(anchor = CENTER)
# - Room 1 -
slider_room1 = Scale(serverdebugwindow, label = "Room1", variable= t_room1)
slider_room1.pack(anchor = CENTER)
# - Room 2 -
slider_room2 = Scale(serverdebugwindow, label = "Room2", variable= t_room2)
slider_room2.pack(anchor = CENTER)
# - Loop -
serverdebugwindow.mainloop()
