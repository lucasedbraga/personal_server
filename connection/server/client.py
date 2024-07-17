import socket

# Defina o endereço do servidor (host) e a porta
HOST = '192.168.100.10'  # Substitua pelo endereço IP do servidor (host)
PORT = 65432             # Mesma porta usada pelo servidor

# Cria um socket TCP/IP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(f"Conectado ao servidor em {HOST}:{PORT}")
    
    while True:
        message = input("Digite a mensagem para enviar ao servidor (ou 'exit' para sair): ")
        if message.lower() == 'exit':
            break
        s.sendall(message.encode())
        data = s.recv(1024)
        print(f"Recebido do servidor: {data.decode()}")
