import socket
import time


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(bytes("-100;-100", "utf-8"), ("192.168.255.95", 3000))
time.sleep(1)
sock.sendto(bytes("0;0", "utf-8"), ("192.168.255.95", 3000))

""" 
Left: 
    
sock.sendto(bytes("50,-50", "utf-8"), ("192.168.255.95", 3000))
time.sleep(1)
sock.sendto(bytes("0;0", "utf-8"), ("192.168.255.95", 3000))

Right:
    
    
sock.sendto(bytes("-50,50", "utf-8"), ("192.168.255.95", 3000))
time.sleep(1)
sock.sendto(bytes("0;0", "utf-8"), ("192.168.255.95", 3000)) """