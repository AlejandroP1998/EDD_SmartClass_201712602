from nodo import node

class lista:
    def __init__(self):
        self.header = None
        self.last = None
    def empty(self):
        if self.header == None:
            return True
        else:
            return False
    
    def insert_header(self,dato):
        if self.empty():
            self.header = self.last = node(dato)
        else:
            aux = node(dato)
            aux.next = self.header
            self.header.prev = aux
            self.header = aux
    def insert_last(self,dato):
        if self.empty():
            self.header = self.last = node(dato)
        aux = self.last
        self.last = aux.next = node(dato)
        self.last.prev = aux
    
    def link_nodes(self):
        if self.header != None:
            self.header.prev = self.last
            self.last.next = self.header
        
    def travel_header_to_last(self):
        aux = self.header
        while aux:
            print(aux.dato)
            aux = aux.next
            if aux == self.header:
                break
    def travel_last_to_header(self):
        aux = self.ultimo
        while aux:
            print(aux.dato)
            aux = aux.prev
            if aux == self.last:
                break
    def delete_header(self):
        if self.empty:
            print('No hay elementos en la lista')
        elif self.header == self.last:
            self.header = self.last = None
        else:
            self.header = self.header.next
        self.link_nodes()
    
    def delete_last(self):
        if self.empty:
            print('No hay elementos en la lista')
        elif self.header == self.last:
            self.header = self.last = None
        else:
            self.last = self.last.prev
        self.link_nodes()
    
    def search(self,dato):
        aux = self.header
        while aux:
            if aux.dato == dato:
                return True
            else:
                aux = aux.next
                if aux == self.header:
                    return False