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

    def appendleft(self,data): # добавление элемента в начало стека (если учитывать что начала стека находится на 0-ом элементе)
        new_node = Node(data) # создаём новый элемент
        current_node = self.head
        new_node.setNext(current_node) # ставим новым элемент на первое место
        self.head = new_node

    def popleft(self): # удаление элемента из начала стека (если учитывать что начала стека находится на 0-ом элементе)
        if self.head == None:
            return
        current_node = self.head
        self.head = current_node.getNext() # меняем голову на следующий по списку элемент
        return current_node.getData() # возвращает элемент при удалении
    

    def append(self,data): # добавление элемента в начало стека (если учитывать что начало стека начинается на -1-ом элементе)
        new_node = Node(data)
        current_node = self.head
        if current_node == None:
            self.head = new_node
            return
        while current_node.getNext() != None: # проход по всему стеку
            current_node = current_node.getNext()
        current_node.setNext(new_node) # добавляем ссылку на новый элемент


    def pop(self): # # удаление элемента из начала стека (если учитывать что начала стека находится на -1-ом элементе)
        current_node = self.head
        if self.head == None: # проверка на пустую голову
            return
        while current_node.getNext().getNext() != None: # доходим до предпоследнего элемента
            current_node = current_node.getNext()
        temp = current_node.getNext().getData() # сохраняем удаляемый элемент в памяти
        current_node.setNext(None) # удаляем ссылку на последний элемент списка
        return temp # возвращаем удаляемый элемент
