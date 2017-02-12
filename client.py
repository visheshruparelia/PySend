import socket               
import sys
from Tkinter import *
import tkMessageBox
import time

try:
	script,ip,port=sys.argv			#Taking HOST IP and PORT as Command lne arguments 
except:								#Handling the exception if user doesnt write IP and PORT while calling the program.
	print("Incorrect parameters")
	print("Usage: python cfinal.py HOST PORT")
	print("Ex. python cfinal.py localhost 8000")
	print("Ex. python cfinal.py 172.16.82.169 8000")
	sys.exit(1)

s = socket.socket()		#Creating a Socket Object which will be used to recieve information from the server
try:        
	s.connect((sys.argv[1],int(sys.argv[2])))  #Using Connect function to connect to the HOST using IP  and PORT.
except:
	print 'PLEASE press OKAY in server pop-up before connecting.'
	print 'If the problem persists check the HOST IP and PORT'
	print 'Try again\nExitting.'
	sys.exit(1)    #This will exit the program using sys module if error occurred

#This will pop-up saying its Connected if it connected successfully 

app1=Tk()
def exit1():
	print 'Exited abruptly!'
	sys.exit(1)
app1.protocol('WM_DELETE_WINDOW',exit1)
app1.wm_title("Connected")
label_connected=Label(app1,text='Connected to ' + sys.argv[1]+' and Port:' + sys.argv[2])  
def destroyapp1():
	app1.destroy()
b_connected=Button(app1,text='Ok',command=destroyapp1)
label_connected.pack()
b_connected.pack()
app1.mainloop()

app2=Tk()
app2.wm_title("PySend")
def exit1():
	print 'Exited abruptly!'
	sys.exit(1)
app2.protocol('WM_DELETE_WINDOW',exit1)
b=s.recv(13)
label_recieve=Label(app2,text=b)
def destroyapp2():
	app2.destroy()
b_get=Button(app2,text='Start recieving!',command=destroyapp2) #This button will initiate the loop of recieving file.
label_recieve.pack()
b_get.pack()
app2.mainloop()

name=s.recv(1024)   							#Will recieve the name of File from HOST and storing it in variable.
print name
i=s.recv(10) 									#Will recieve the size of file in bytes as 10 charactered string.
try:  										    
	len1=int(float(i))							#Converting again the string to integer.
except:
	print 'The size is not properly recieved\nPlease try again.'
	sys.exit(1)
print i
prev=0
with open(name,'w') as fo:						#Opening the file in WRITE MODE with same name as recieved from HOST.
	print 'Started Recieveng...'
	start=time.time()							#Initialising time object.
	end=0  					
	for j in range(len1+1):
		l=s.recv(1)   							#Recieving Data BYTE BY BYTE and storing in variable.
		fo.write(l)   							#Writing that data in that file using WRITE function.
		curr= j*100/len1
		if curr!=prev:
			prev=curr
			if(curr==99):
				end=time.time()
				print curr
			else:
				print curr						#Printing the currently recieved precentage of file.

	print 'Finished.'
	print 'Time Elapsed='+str(end-start)+'s'	#Total time elapsed

fo.close()
app4=Tk()
app4.wm_title("Done")
def exit1():
	print 'Exited abruptly!'
	sys.exit(1)
app4.protocol('WM_DELETE_WINDOW',exit1)
app4.wm_title('Done!')
label_done=Label(app4,text='File('+name+') recieved successfully!').pack()
def close():
	app4.destroy()
	sys.exit(0)   #Successfully exitting the Code.
b_close=Button(app4,text='Close safely!',command=close).pack()
app4.mainloop()