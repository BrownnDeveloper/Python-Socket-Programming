#Factorial Socket programming code
#Code for the Client 
import socket


def client_program():
    host = socket.gethostname()  #As Both Client and server are running on same machine
    port = 5000  # Port number same as Server port address

    client_socket = socket.socket()  # Instantiating the socket
    client_socket.connect((host, port))  # Connecting to the server
    print("+--------------+")
    print("|Factorial bot |")
    print("+--------------+")
    try:
        message = int(input("\nNumber To Find Factorial ~:  "))  #Takes First Input
        message = str(message)
        while message.lower().strip() != 'bye':
            client_socket.send(message.encode())  # Sending message to the server
            data = client_socket.recv(1024).decode()  # Receiving response from the server

            print(data,"\n")  # show in terminal
            print("+-----------------------+")
            print("|Do you want to continue|")
            print("+-----------------------+")
            print("Type [Yes] to find out factorial of more numbers")
            print("Type [BYE] to exit.")
            
            user_input = input("\n[YES] :: [Bye]\n")

            if user_input == 'yes' or user_input =='YES':
                print("\n------------------------------------------------------")
                message = int(input("\nNumber To Find Factorial ~:  "))  # More inputs !!
                message = str(message)
            else:
                message = 'bye'   
        client_socket.close()  # close the connection
    except ValueError:
        print("Invalid Input By The User\n", )
        client_socket.close()
            
if __name__ == '__main__':
    client_program()
