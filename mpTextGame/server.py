import socket
import threading

host = socket.gethostbyname(socket.gethostname())
port = 55555

print(f"Opening server on: {host}")
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

menu_string = "\t\tWelcome To the game!\n" \
    "\t\t1. Start new game\n" \
    "\t\t2. Continue\n" \
    "\t\t3. Instructions\n" \
    "\t\t4. Quit"

instructions_string = "\t\tright: Take the right path\n" \
"\t\tleft: Take the left path\n" \
"\t\tforward: Take the forward path\n"\
"\t\tback: Takes the backwards path\n"\
"\t\tattack1: Primary attack\n" \
"\t\tattack2: Secondary attack\n" \
"\t\tcheckpaths: Shows all available directional moves"

def handle(client):
    while True:
        try:
            input = client.recv(1024).decode('ascii')
            #input_handler(input)
            if input.endswith("quit"):
                remove_client(client)
                break
        except:
            remove_client(client)
            print("What have you done?")
            break

def broadcast(command):
    try:
        for client in clients:
            client.send(command)
    except:
        print("Error when broadcasting message to all clients")
    
def receive():
    while True:
        client, address = server.accept()
        print(f"Someone New is approaching!")

        client.send("NICK".encode("ascii"))
        nickname = client.recv(1024).decode("ascii")
        nicknames.append(nickname)
        clients.append(client)

        print(f"{nickname} Approaches!")
        client.send(menu_string.encode('ascii'))

        thread = threading.Thread(target=handle(client,))
        thread.start()
    
def input_handler(input):
    if input == "QUIT GAME":
        pass

def remove_client(client):
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f"{nickname} left the journey!".encode("ascii"))
            nicknames.remove(nickname)

receive()