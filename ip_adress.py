import socket
if os.path.isfile('C:/Python/Project/tg_bot/files/received/my_ip.txt'):
 ip = open('C:/Python/Project/tg_bot/files/received/my_ip.txt', 'r')
 ip_adress = ip.read()
HOST = ip_adress  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            if data == b'say hello':
                print("hello")
#   Thanks Victor VosMottor from stackoverflow!
