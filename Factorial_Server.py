#Factorial program on socket programming
## Code for the server ##
import socket

def fact(a):  #Function to find out factorial of a number using recursion
	if a==0:
		return 1
	else:
		return a*fact(a-1)

def server_program(): #Function to define server code
	host = socket.gethostname()  #As Both Client and server are running on the same machine
	port = 5000   #Port address, keep the same value in client code.

	Serv_socket= socket.socket()  #Socket object
	Serv_socket.bind((host,port))
	Serv_socket.listen(2)  
	conn, address = Serv_socket.accept()
	print("Connection from: " + str(address))	 
	
	while True:
		data = conn.recv(1024).decode()
		if not data:
			break
		print("Number entered by User :~ " + str(data))
		a = int(data)
		output = fact(a)
		#data = input('Factorial of this number is :~ ')
		data = str(output)
		data = "Factorial is :: "+data
		conn.send(data.encode())

	conn.close()

if __name__ == '__main__':
	server_program()			


