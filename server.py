import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 3000)) #create server at socket.gethostname() port 3000
s.listen(5)

while True:
	clt, adr = s.accept()
	print(f"Connection to {adr} established!")
	clt.send(bytes("Sample Text", "utf-8"))