import socket
import _pickle as pickle
from uhashring import HashRing


hr = HashRing(nodes=['node_1', 'node_2', 'node_3', 'node_4', 'node_5', 'node_6', 'node_7', 'node_8'], vnodes = 1)

nodes = {'node_1': 'ip-1', 'node_2': 'ip-2', 'node_3': 'ip-3', 'node_4': 'ip-4', 'node_5': 'ip-5', 'node_6': 'ip-6', 'node_7': 'ip-7', 'node_8': 'ip-8'}

port = 7771 

user_name = input('Enter your username: ')
server_name = hr.get_node(user_name)

print('Your request will be handled by: ', server_name) 

socket = socket.socket()

socket.connect((nodes[server_name], port))

username_serialized = pickle.dumps(user_name)

socket.send(username_serialized)

products_list_ser = socket.recv(2048)

products_list = pickle.loads(products_list_ser)

for i in range(0,len(products_list)):
    print("Item ", i+1,': ', products_list[i+1])


flag = True

cart_object = {'username': user_name}

while flag == True:
    item = int(input("Enter the item number you want to buy: "))
    quantity = int(input("How many: "))
    cart_object[hashlib.md5(products_list[item].encode()).hexdigest()] = quantity
    quit = input("Do you want to buy more? y/n: ")
    if quit == 'n':
        flag = False

socket.send(pickle.dumps(cart_object))

socket.close()
