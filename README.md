# PySend
PySend

FILE SHARING TOOL

PROJECT AIM:
To easily share any type of file between one client and a server over WiFi
with the primary condition that both should be connected to the same WiFi
network.

PROJECT DESCRIPTION:
In the software there are two programs. One is the Server which hosts the
sharing and sends the file and the other is Client , which accepts files
from server. This whole thing will be executed with GUI using Tkinter.
We will use Command Line Arguments to mention IP and PORT on
which the server is hosted. Errors will be Exception Handled to have a
better experience. The user has to enter the name of file along with the
extension and the same file will recieved by the client. SOCKET
Programming will be used extensively to establish connection and
send/recieve files. File Handling will be used to read ,write and save files.

CONCEPTS USED:
- Socket Programming
-File Handling
-Command Line Arguments
-Tkinter GUI
-Exception Handling

MODULES USED:
-Socket
-Os
-Sys
-Tkinter
-Tkinter MessageBox

BASIC FEATURES:
-A Function called getip() determines local IP address by pinging (requires
active internet connection) so that user doesn’t have to worry about finding
it and to avoid confusion between Local IP and Public IP. Here there will
be an exception that if user is not connected to internet i.e if the user is on
Hotspot type of network which doesn’t have connection but still has an IP
address so that an exception will be raised asking for user to enter IP
address manually.
-Server.py file will take port as a command line argument and Client.py
will take Host’s IP and PORT as command line arguments.
-Can Send any type of file.
-User Friendly.
-Upto 1.5MBps transfer speed.
