import tkinter as tk
import socket

HEIGHT = 620
WIDTH = 800
global sock


def socket_connection(data):
    # Create a tcp/ip socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect the socket to the port where the server is listening
    server_address = ('localhost', 50000)
    print('Connecting to %s port %s' % server_address)
    sock.connect(server_address)

    try:
        # Send data
        sock.sendall(data)
        # Wait the result from the server
        data = sock.recv(512)
        resultado_label['text'] = data.decode()
    finally:
        sock.close()


def main():
    frame = tk.Frame(root, bg='#80c1ff')
    frame.place(relheight=1, relwidth=1)

    cadastrar_botao = tk.Button(
        frame, text='Cadastrar um novo cliente', command=cadastrar)
    cadastrar_botao.place(rely=0.1, relwidth=0.5, relx=0.25, relheight=0.1)

    remover_botao = tk.Button(
        frame, text='Remover um cliente', command=remover)
    remover_botao.place(rely=0.4, relwidth=0.5, relx=0.25, relheight=0.1)

    consultar_botao = tk.Button(
        frame, text='Consultar dados de um cliente', command=consultar)
    consultar_botao.place(rely=0.7, relwidth=0.5, relx=0.25, relheight=0.1)


def cadastrar():
    global resultado_label
    frame = tk.Frame(root, bg='#80c1ff')
    frame.place(relheight=1, relwidth=1)
    label = tk.Label(frame, text='Preencha os campos abaixo',
                     font=('Century', 14), bg='#80c1ff')
    label.place(rely=0.1, relx=0.25, relheight=0.1, relwidth=0.5)
    name_label = tk.Label(frame, text='Nome:', font=('Century', 12))
    name_label.place(rely=0.3, relx=0.2, relwidth=0.1, relheight=0.05)
    name_entry = tk.Entry(frame)
    name_entry.place(rely=0.3, relx=0.31, relwidth=0.5, relheight=0.05)
    cpf_label = tk.Label(frame, text='CPF:', font=('Century', 12))
    cpf_label.place(rely=0.4, relx=0.2, relwidth=0.1, relheight=0.05)
    cpf_entry = tk.Entry(frame)
    cpf_entry.place(rely=0.4, relx=0.31, relwidth=0.5, relheight=0.05)
    adress_label = tk.Label(frame, text='Endereço:', font=('Century', 12))
    adress_label.place(rely=0.5, relx=0.2, relwidth=0.1, relheight=0.05)
    adress_entry = tk.Entry(frame)
    adress_entry.place(rely=0.5, relx=0.31, relwidth=0.5, relheight=0.05)
    back_button = tk.Button(frame, text='Voltar', command=main)
    back_button.place(rely=0.7, relx=0.2, relwidth=0.25, relheight=0.06)
    cadastrar_button = tk.Button(frame, text='Cadastrar', command=lambda: socket_connection(
        str.encode('1;' + name_entry.get() + ';' + cpf_entry.get() + ';' + adress_entry.get())))
    cadastrar_button.place(rely=0.7, relx=0.56, relwidth=0.25, relheight=0.06)
    resultado_label = tk.Label(
        frame, text='', font=('Century', 14), bg='#80c1ff')
    resultado_label.place(rely=0.9, relx=0.2, relwidth=0.6, relheight=0.06)


def remover():
    global resultado_label
    frame = tk.Frame(root, bg='#80c1ff')
    frame.place(relheight=1, relwidth=1)
    label = tk.Label(frame, text='Preencha os campos abaixo',
                     font=('Century', 14), bg='#80c1ff')
    label.place(rely=0.1, relx=0.25, relheight=0.1, relwidth=0.5)
    name_label = tk.Label(frame, text='Nome:', font=('Century', 12))
    name_label.place(rely=0.3, relx=0.2, relwidth=0.1, relheight=0.05)
    name_entry = tk.Entry(frame)
    name_entry.place(rely=0.3, relx=0.31, relwidth=0.5, relheight=0.05)
    back_button = tk.Button(frame, text='Voltar', command=main)
    back_button.place(rely=0.4, relx=0.2, relwidth=0.25, relheight=0.06)
    remover_button = tk.Button(frame, text='Remover', command=lambda: socket_connection(
        str.encode('2;' + name_entry.get())))
    remover_button.place(rely=0.4, relx=0.56, relwidth=0.25, relheight=0.06)
    resultado_label = tk.Label(
        frame, text='', font=('Century', 14), bg='#80c1ff')
    resultado_label.place(rely=0.55, relx=0.2, relwidth=0.6, relheight=0.06)


def consultar():
    global resultado_label
    frame = tk.Frame(root, bg='#80c1ff')
    frame.place(relheight=1, relwidth=1)
    label = tk.Label(frame, text='Preencha os campos abaixo',
                     font=('Century', 14), bg='#80c1ff')
    label.place(rely=0.1, relx=0.25, relheight=0.1, relwidth=0.5)
    name_label = tk.Label(frame, text='Nome:', font=('Century', 12))
    name_label.place(rely=0.3, relx=0.2, relwidth=0.1, relheight=0.05)
    name_entry = tk.Entry(frame)
    name_entry.place(rely=0.3, relx=0.31, relwidth=0.5, relheight=0.05)
    back_button = tk.Button(frame, text='Voltar', command=main)
    back_button.place(rely=0.4, relx=0.2, relwidth=0.25, relheight=0.06)
    consultar_button = tk.Button(frame, text='Consultar', command=lambda: socket_connection(
        str.encode('3;' + name_entry.get())))
    consultar_button.place(rely=0.4, relx=0.56, relwidth=0.25, relheight=0.06)
    resultado_label = tk.Label(
        frame, text='', font=('Century', 14), bg='#80c1ff')
    resultado_label.place(rely=0.55, relx=0.2, relwidth=0.6, relheight=0.25)

# ----------------------------------------------------------------------------------------


root = tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.place(relheight=1, relwidth=1)
canvas.pack()

main()

root.mainloop()
