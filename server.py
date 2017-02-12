import socket
import os
import sys
from Tkinter import *
import tkMessageBox

def getip():    						#Function to retrieve server's Local IP using an active innternet connection.
	p = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	p.connect(("gmail.com",80)) 		#Pinging any random site--->Here gmail.com
	ip=(p.getsockname()[0])
	return ip
	p.close()
	raise Exception() 					#Handling the exception if there is no active internet connection.
global port
port=0000
try:
	script,port=sys.argv  				#Taking port as Command Line Argument and Handling the error in case the user doesn't enter the port
except:
	root = Tk()    						#Pops up an error message
	root.wm_title("Error")
	label_error = Label(root, text = "Incorrect parameters\nUsage: python server.py PORT\nEx. python server.py 8000")
	b = Button(root, text = "Okay", command = root.destroy)
	label_error.pack()
	b.pack()
	root.mainloop()
	sys.exit(1)

s = socket.socket()		#Creating a Socket Object which will be used to recieve information from the server
try:
	global ip
	ip=getip()
except Exception:
	#Will take ip address manually as the server is not connected to internet.
	'''
	GUI for taking input
	'''
	app = Tk()
	app.wm_title("PySend") 
	global entry_ip
	ip = 0
	label_ip=Label(app, text = 'You are not connected to internet so we are not able to fetch your ip address\nPlease Enter ip manually:')
	entry_ip=Entry(app, bd = 10)
	def get_ip():
		global ip
		ip = entry_ip.get()    
		app.destroy()
	b_ip = Button(app, text = "Create Server", command = get_ip)
	label_ip.pack()
	entry_ip.pack()
	b_ip.pack()
	app.mainloop()

try:
	s.bind((ip,int(port)))  #Hosting server using inbuilt bind function and handling the exception of already used socket as follows.
except:
	sock=Tk()
	sock.wm_title("Socket Error")
	def exit1():
		print 'Exited abruptly!'
		sys.exit(1)
	sock.protocol('WM_DELETE_WINDOW',exit1) 
	label_socket=Label(sock,text='Socket already in use\nPlease Enter another port to create server:')
	entry_port=Entry(sock,bd=10)
	port=8000 					#Default is 8000
	def createport():
		global port
		port=entry_port.get()
		s.bind((ip,int(port)))
		sock.destroy()
	b_socket=Button(sock,text='Create Server!',command=createport) #Taking new Port to host server on.
	label_socket.pack()
	entry_port.pack()
	b_socket.pack()
	sock.mainloop()

root1 = Tk()
root1.wm_title("Server")
def exit1():
		print 'Exited abruptly!'
		sys.exit(1)
root1.protocol('WM_DELETE_WINDOW',exit1) 
label_error = Label(root1, text = 'Server created successfully\nConnect to ip:'+ip+' and Port:'+str(port)+'\nWaiting for Connection!!')
b = Button(root1, text = "Okay", command = root1.destroy)
label_error.pack()
b.pack()
root1.mainloop()

s.listen(5) 	#This Functions waits for connection for 5 tries from client.
c, addr = s.accept()
root2 = Tk()
root2.wm_title("Connected")
def exit1():
		print 'Exited abruptly!'
		sys.exit(1)
root2.protocol('WM_DELETE_WINDOW',exit1) 
label_error = Label(root2, text = 'Got connection from' + str(addr))
def destroyb():
	root2.destroy()
b = Button(root2, text = "Okay", command = destroyb) #Destroys the Window
label_error.pack()
b.pack()
root2.mainloop()

c.send("Incoming File")  #Send Function is used to send strings to  the client.
app1=Tk()
def exit1():
		print 'Exited abruptly!'
		sys.exit(1)
app1.protocol('WM_DELETE_WINDOW',exit1) 
app1.wm_title("Name")
global entry_name
name='abcd' #Default

#Asking User to enter the name of file located in the same folder as on which the code is saved.
label_name=Label(app1,text='Enter name of the file:')     
entry_name=Entry(app1,bd=10)
   
def get_name():   #Selects and Stores the name.
	global name, app1
	name=entry_name.get()
	app1.destroy()

b_name=Button(app1,text='Select this file!',command=get_name)	#Calls the get_name function
label_name.pack()
entry_name.pack()
b_name.pack()
app1.mainloop()
print name

global byte
byte=0
def send_file():
	global app2
	app2.destroy()
	c.send(name)  #Sends the name of the file to the Client
	i=0 

	def computeSize():  #Computes the size of file in bytes using the OS module
		size=os.stat(name) 
		return size.st_size

	try:
		#global byte
		byte=computeSize()
	except:
		print 'Not able to compute the size of file.Check if the file exits and try again.'
		sys.exit(1)

	#Converting size into 10 digit decimal number and converting into string and then sending the size to the client.
	c.send(str(byte)+'.'+'0'*(9-len(str(byte))))  
	with open(name,'r') as fo:     		#Opening file as READ MODE and naming object as fo.
		for j in range(byte+1):    
			line=fo.read(1) 			#Running loop and reading the file byte by byte and storing data in a variable.   
			try:						#Handling Error of wrongly sent file size
				c.send(line)			#Now sending this variable to the client.
			except:
				print 'Some Error occurred.\nPlease try again.'
				sys.exit(1)				
							
	fo.close()
	app4=Tk()
	def exit1():
		print 'Exited abruptly!'
		sys.exit(1)
	app4.protocol('WM_DELETE_WINDOW',exit1) 
	def destroyb1():
		app4.destroy()
	b_sent=Button(app4,text='File('+name+') Sent Successfully!',command=destroyb1)
	b_sent.pack()
	app4.mainloop()

app2=Tk()
def exit1():
		print 'Exited abruptly!'
		sys.exit(1)
app2.protocol('WM_DELETE_WINDOW',exit1) 
app2.wm_title("Send")
b_send=Button(app2,text='Send File!',command=send_file) #Will call send_file function
b_send.pack()
app2.mainloop()