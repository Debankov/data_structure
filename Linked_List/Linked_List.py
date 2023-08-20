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
        while current_node.getNext() != None: # пока следущий элемент после текущего не равен None
            current_node = current_node.getNext()
        current_node.setNext(new_node)


    def showMeAll(self): # вывод элементов СС*
        current_node = self.head
        result = ''
        while current_node != None: # пока текущий элемент не равен None
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
        current_node = self.head
        self.head = current_node.getNext()
