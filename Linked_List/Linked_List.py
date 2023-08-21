from Node import Node

class LinkedList(object): # CC* - Связный список
    def __init__(self):
        self.head = None


    def append(self,data): # добавление элемента в конец СС*
        new_node = Node(data)
        current_node = self.head
        if current_node == None: # проверка на пустую голову
            self.head = new_node
            return
        while current_node.getNext() != None: # проходимся по всему списку и останавливаемся на предпоследнем
            current_node = current_node.getNext()
        current_node.setNext(new_node)


    def showMeAll(self): # вывод элементов СС*
        current_node = self.head
        result = ''
        while current_node != None: # проходимся по всему списку
            result += str(current_node.getData())
            current_node = current_node.getNext()
        return " --> ".join(result)
    

    def length(self):
        current_node = self.head
        count = 0
        while current_node != None:
            current_node = current_node.getNext()
            count += 1
        return count
    

    def addFirst(self,data): # добавление элемента в начало СС*
        new_node = Node(data)
        current_node = self.head 
        new_node.setNext(current_node) # добавляем ссылку новому элементу на текущую голову
        self.head = new_node # меняем голову на новый элемент


    def remove_last(self): # удаление последнего элемента из СС*
        current_node = self.head
        while current_node.getNext().getNext() != None:
            current_node = current_node.getNext()
        current_node.setNext(None)
    
    
    def remove_first(self): # удаление первого элемента из СС*
        if self.head == None:
            return
        else:
            current_node = self.head
            self.head = current_node.getNext()


    def value(self, index): # возвращение элемента, через его индекс в СС*
        current_node = self.head
        count = 0
        if index < 0:# что-бы не переберало весь список
            return "Index out of range" 
        while current_node != None: # перебор всего списка
            if count == index: # если входной индекс равен count, вовзращаем искомое
                return current_node.getData()
            count += 1
            current_node = current_node.getNext()
        return "Index out of range" # если не нашло индекс
    
    def insert(self, index, data): # вставка в любое место СС*. index - на какое место, data - какой элемент
        current_node = self.head
        new_node = Node(data)
        count = 0
        while current_node != None:
            if index == 0: # вставка в начало списка
                self.addFirst(data)
                return
            if index == count + 1: # count + 1, потому что без этого плюса, он будет вставлять элемент после заданного индекса
                new_node.setNext(current_node.getNext()) # вставляем ссылку
                current_node.setNext(new_node)
            count += 1
            current_node = current_node.getNext()
        return "Index out of range" # если не нашло индекс

