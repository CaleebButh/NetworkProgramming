import socket
import threading

nickname = input("Choose a nickname before we begin: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((socket.gethostbyname(socket.gethostname()), 55555))

def receive():
    #write all code that needs to happen when the client receives anything from the server here.
    while True:
        try:
            message = client.recv(1024).decode("ascii")
            if message == "NICK":
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("An error occurred")
            client.close()
            break
        
def write():
    while True:
        command = f"{nickname}: {input("")}"
        client.send(command.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
        