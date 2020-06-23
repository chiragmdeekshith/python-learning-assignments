import socket
import threading


class ClientListenThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        print("Listening to messages from server.")
        while True:
            server_message = server_socket.recv(1024).decode('ascii')
            print(server_message)
            if server_message == "Exiting":
                return


server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
host = socket.gethostname()
port = 9876

client = ClientListenThread()
server_socket.connect((host, port))
client.start()

while True:
    client_message = input()
    server_socket.send(client_message.encode('ascii'))
    if client_message == "exit":
        break

client.join()
