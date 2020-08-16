import Main

class ClientClass:

    clients_list = Main.array_list()

    def __init__(self, name, password):
        self.username = name
        self.password = password
        self.downloaded_apps = Main.array_list()


def signing_checker(username, password):
    for each_contact in ClientClass.clients_list.display():
        if each_contact.username == username and each_contact.password == password:
            return True
    return False

def client_getter(username, password):
    for each_contact in ClientClass.clients_list.display():
        if each_contact.username == username and each_contact.password == password:
            return each_contact