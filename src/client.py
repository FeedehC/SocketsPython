import socket
import threading

matrixB = 'postmult_B_stream_fixed.out'
matrixA = 'premult_A_stream_fixed.out'

HEADER = 64
PORT = 7
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "172.16.0.91" #IP del server al que me quiero conectar
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length)) #Se hace padding agregando caracteres blancos, cantidad: 64-len
    client.send(send_length) #Primero se envia la longitud de todo el mensaje, completado con espacios hasta 64 bytes
    client.send(message) #Se envia el mensaje completo
    print(client.recv(2048).decode(FORMAT))
    

send("Somos la fundacion fulgor".encode(FORMAT))


##################-Enviar Matrix A-################
#with open(matrixA) as f_obj:
    #send("  ######## Envio Matrix A ########  ")
    #for line in f_obj:
        #lineSplit = line.split()
        #for elemento in lineSplit:
            #send(elemento)

##################-Enviar Matrix B-################
#with open(matrixB) as f_obj:
    #send("  ######## Envio Matrix B ########  ")
    #for line in f_obj:
        #lineSplit = line.split()
        #for elemento in lineSplit:
            #send(elemento)


send(DISCONNECT_MESSAGE)






