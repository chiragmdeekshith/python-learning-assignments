import socket
import threading
import pymysql
from datetime import datetime

clients_list = []


class ClientHandlerThread(threading.Thread):
    def __init__(self, client_socket, address):
        threading.Thread.__init__(self)
        self.email = ""
        self.client_socket = client_socket
        self.address = address

    def run(self):
        print("New client thread starting:- ", self.email, " , Address:- ", self.address)
        server_message = "Connection successful. Type 'exit' to exit. Enter your valid email ID"
        self.client_socket.send(server_message.encode('ascii'))
        self.email = self.client_socket.recv(1024).decode('ascii')

        if self.email == "exit":
            return

        while True:
            message = self.client_socket.recv(1024).decode('ascii')
            if message == "exit":
                exit_message = "Exiting"
                self.client_socket.send(exit_message.encode('ascii'))
                for client in clients_list:
                    if client.email == self.email:
                        clients_list.remove(client)
                        print(client.email, " left.")
                return
            else:
                time = datetime.now().strftime("%H:%M:%S")
                print_message = time+" -- "+self.email + ": " + message
                print(print_message)
                for client in clients_list:
                    if client.email != self.email:
                        client.client_socket.send(print_message.encode('ascii'))

                # log the message into db
                save_to_database(time, self.email, message)


def save_to_database(time, email, message):
    database = pymysql.connect("localhost", "root", "toor", "python")
    cursor = database.cursor()
    query = "INSERT INTO chat_log VALUES(\'" + time+"\',\'"+email+"\',\'"+message + "\')"
    cursor.execute(query)
    database.commit()
    database.close()
    return


def main():
    # Server for the chat application
    server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 9876

    server_socket.bind((host, port))
    server_socket.listen(50)

    while True:
        client_socket, address = server_socket.accept()
        client = ClientHandlerThread(client_socket, address)
        client.start()
        clients_list.append(client)


main()
