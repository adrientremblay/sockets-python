import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect ((socket.gethostname(), 3000)) #connect to server
msg = s.recv(3000)
print(msg.decode("utf-8"))