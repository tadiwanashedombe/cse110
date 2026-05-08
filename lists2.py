clients = []

new_client = ""

while new_client != "quit":
    
    new_client = input("New client name : ")
    if new_client != "quit":
        clients.append(new_client)

for client in clients:
    print(client)