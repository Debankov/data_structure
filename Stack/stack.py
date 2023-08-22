from node import Node # импортируем класс элемента

class Stack(object):
    def __init__(self) -> None:
        self.head = None

    def __repr__(self) -> str: # магический метод, который отображает стек
        current_node = self.head
        result = ''
        while current_node != None: # проходимся по всему списку
            result += str(current_node.getData())
            current_node = current_node.getNext()
        return " --> ".join(result)

    def push(self,data): # добавление элемента в начало стека
        new_node = Node(data) # создаём новый элемент
        current_node = self.head
        new_node.setNext(current_node) # ставим новым элемент на первое место
        self.head = new_node

    def pop(self): # удаление элемента из начала стека
        if self.head == None:
            return
        current_node = self.head
        self.head = current_node.getNext() # меняем голову на следующий по списку элемент
        return current_node.getData() # возвращает элемент при удалении