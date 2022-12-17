import time, socket, sys

print("\nWelcome to Chat Room\n")
print("Initialising....\n")
time.sleep(1)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
shost = socket.gethostname()
ip = socket.gethostbyname(socket.gethostname())
print(shost, "(", ip, ")\n")
host = input(str("Enter server address: "))
host= host.strip()
name = input(str("\nEnter your name: "))
port = 1234 
print("\nTrying to connect to ", ip, "(", port, ")\n")
time.sleep(1)
s.connect((host, port))
print("Connected...\n")

s.send(name.encode())
s_name = s.recv(1024)
s_name = s_name.decode()
print(s_name, "has joined the chat room\nEnter [e] to exit chat room\n")

while True:
    message = s.recv(1024)
    message = message.decode()
    print(s_name, ":", message)
    message = input(str("Me : "))
    if message == "[e]":
        message = "Left chat room!"
        s.send(message.encode())
        print("\n")
        break
    s.send(message.encode())