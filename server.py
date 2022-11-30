import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
LIST_MSG = "RCV_LST"
item_list = []
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client (conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        # get message header
        msg_length = conn.recv(HEADER).decode(FORMAT)
        # check if the message has length. (when it connects it will send a message with no length.)
        if msg_length:
            # convert message length to int.
            msg_length = int(msg_length)
            # decode message
            msg = conn.recv(msg_length).decode(FORMAT)
        
            if msg == DISCONNECT_MESSAGE:
                # disconnect if message is the disconnect message  
                connected = False
                conn.send("Goodbye".encode(FORMAT))
            elif msg == LIST_MSG:
                # if list message is recieved, send list to user.
                count = 0
                for i in item_list:
                    count += 1
                    conn.send(f"{i} .|.".encode(FORMAT))
            else:
                # add message to list
                item_list.append(msg)
                conn.send("added".encode(FORMAT))
            
            # prints user and messsage sent.
            print(f"[{addr}] {msg}")

    conn.close()



def start() :
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        # recieves new connnection
        conn, addr = server.accept()
        # starts a new thread
        thread = threading.Thread(target=handle_client, args= (conn, addr))
        thread.start()
        # print the number of active connections.
        print (f" [ACTIVE CONNECTIONS] {threading.active_count() - 1}")

    
print(" (STARTING] server is starting...")
start()