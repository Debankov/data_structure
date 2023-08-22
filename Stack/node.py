class Node(object):
    def __init__(self,data = None ,next = None) -> None:
        self.data = data
        self.next = None
        
    # гетеры
    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next

    # сетеры
    def setData(self,data):
        self.data = data

    def setNext(self,next):
        self.next = next