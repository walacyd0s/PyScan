# biblioteca usada para escanear as portas
import socket

# host de destino
ip_host = '192.168.0.1'

# dicionário contendo o nome e numero das portas
port_list = {21: 'ftp', 22: 'ssh', 80: 'http', 443: 'https', 110: 'pop'}

# loop aonde é executado o comando para teste nas portas, iterando os itens do dicionário
for x, y in port_list.items():
    conexao = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # condição que verifica se a porta está aberta ou fechada
    if conexao.connect_ex((ip_host, int(x))) == 0:
        print(f'Porta {x}({y}) aberta!')
    else:
        print(f'Porta {x}({y}) fechada!')
