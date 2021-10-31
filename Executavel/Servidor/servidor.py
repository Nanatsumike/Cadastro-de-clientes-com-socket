import pandas as pd
import socket


def consultar(nome):
    df = pd.read_csv('database.csv')
    try:
        x = df.loc[df['Nome'] == nome]
        nome, cpf, endereco = x.iloc[0]
        resultado = 'Nome: ' + str(nome) + '\nCPF: ' + \
            str(cpf) + '\nEndereço: ' + str(endereco)
        return resultado
    except:
        return 'Nome não encontrado'


def cadastar(nome, cpf, endereco):
    try:
        df = pd.read_csv('database.csv')
        df = df.append({'Nome': nome, 'CPF': cpf,
                        'Endereco': endereco}, ignore_index=True)
        df.to_csv('database.csv', index=False)
        return 'Cadastro feito com sucesso!'
    except:
        return 'Erro ao cadastrar cliente'


def remover(nome):
    df = pd.read_csv('database.csv')
    try:
        df = df.set_index('Nome')
        df = df.drop(nome)
        df.to_csv('database.csv')
        return 'Removido com sucesso!'
    except:
        return 'Erro ao remover ' + nome


def operator(values: str):
    values = values.split(sep=';')
    if values[0] == '1':
        result = cadastar(values[1], values[2], values[3])
    elif values[0] == '2':
        result = remover(values[1])
    elif values[0] == '3':
        result = consultar(values[1])
    else:
        result = 'Invalid operation!'
    result = str(result)
    return result


try:
    df = pd.read_csv('database.csv')
except:
    df = pd.DataFrame(columns=['Nome', 'CPF', 'Endereco'])
    df.to_csv('database.csv', index=False)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 50000)
print('Starting up on %s port %s' % server_address)
sock.bind(server_address)

sock.listen(1)
while True:
    # Wait for a connection
    print('Waiting for a connection')
    connection, client_address = sock.accept()
    print('Connected in ip: %s, port: %s ' % client_address)
    try:
        # Receiving the values
        data = connection.recv(512)
        values = data.decode()
        data = operator(values)

        # Returning the result
        connection.sendall(data.encode())
        print("Information returned")
    finally:
        # Clean up the connection
        print('Closing connection')
        connection.close()
