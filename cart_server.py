import socket
import _pickle as pickle
import _thread

coordinator = { 1: 'ip-1', 2: 'ip-2', 3: 'ip-3', 4: 'ip-4', 5: 'ip-5', 6: 'ip-6', 7: 'ip-7', 8: 'ip-8'}

def user_interaction(con, client_addr):
    print("Client connected: ", client_addr)
    user_name_serialized = con.recv(2048)
    user_name = pickle.loads(user_name_serialized)
    server = coordinator[(int(user_name[4])%8)+1]
    print('The coordinator node is: node_', (int(user_name[4])%8)+1)
    con.send(products_ser)
    client_cart_ser = con.recv(4096)
    client_cart = pickle.loads(client_cart_ser)
    print(client_cart)
    con.close()

socket = socket.socket()
print("Socket created")

port = 7771

socket.bind(('', port))
print("Socket bind to %s" %(port))

socket.listen(3)

products = {1: 'MSI Gaming GeForce RTX 2080 Ti 11GB GDRR6', 2: 'Intel Core i9 9900K Coffee Lake 8-Core', 3: 'Asus TUF Z370 Plus Gaming 8th Generation Motherboard', 4: 'G.Skill Trident Z RGB Series 32Gb 3000MhHz Mem' }
products_ser = pickle.dumps(products)

while True:
    con, client_addr = socket.accept()
    _thread.start_new_thread(user_interaction,(con,client_addr))
    
socket.close()
