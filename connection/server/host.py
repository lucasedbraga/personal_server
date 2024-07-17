import socket

# Defina o endereço do host e a porta
HOST = '0.0.0.0'  # Aceitar conexões de qualquer endereço IP
PORT = 65432      # Porta para escutar as conexões

# Cria um socket TCP/IP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Servidor escutando em {HOST}:{PORT}")
    
    conn, addr = s.accept()
    with conn:
        print(f"Conectado por {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Recebido: {data.decode()}")
            conn.sendall(data)
