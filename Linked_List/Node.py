class Node(object):
    def __init__(self, data = None, next = None): # обьявление элемента
        self.data = data
        self.next = None


    # Get методы
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    
    # Set методы
    def setData(self,data):
        self.data = data
    def setNext(self,next):
        self.next = next