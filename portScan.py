import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(0.2)
code = client.connect_ex(("bancocn.com", 443))
if code == 0:
    print("porta aberta")
else:
    print("porta fechada")

