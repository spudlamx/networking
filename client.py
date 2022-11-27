import socket

import socket
HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = '127.0.0.1'
ADDR = (SERVER, PORT)
LIST_MSG = "RCV_LST"
client = socket. socket (socket.AF_INET, socket.SOCK_STREAM)
client.connect (ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    recieved = str(client.recv(2048))
    recieved = recieved[2:-1]
    recieved = recieved.split(".|.")
    for i in recieved:
        print(i)


running = True
while running:
    choice = -1
    # Prints menu
    print("0. QUIT")
    print("1. Add item")
    print("2. View items")
    # get choice
    choice = input("Enter choice: ")

    if choice == "0":
        # sends the disconnect message to end connection with server.
        send(DISCONNECT_MESSAGE)
        # end loop.
        running = False
    elif choice == "1":
        # prompt for the item and send it to server.
        item = input("Enter Item: ")
        send(item)
    elif choice == "2":
        # list_msg will prompt the server to send back the list.
        send(LIST_MSG)
    else:
        print("Invalid choice. Try Again.")