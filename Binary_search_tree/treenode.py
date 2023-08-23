class TreeNode():
    def __init__(self, key = None) : 
        self.key = key # ключ
        self.left = None # левый элемент
        self.right = None # правый элемент


    def __str__(self) -> str: # нормальный вывод 
        return f"TreeNode = {self.key}"    


    def insert(self,key): # вставка элементов в дерево
        if self.key is None: # проверка на пустую голову
            self.key = key
            return

        current = self 
        while True: # бесконечный цикл, который проходит во всему дереву
            if key < current.key: # проход в левую часть дерева
                if current.left is None: # вставка элемента
                    current.left = TreeNode(key)
                    break # выход из цикла
                current = current.left # меняем текущий элемент для того, что-бы пройти дальше 
            elif key > current.key: # проход в правую часть дерева
                if current.right is None: # вставка элемента
                    current.right = TreeNode(key)
                    break
                current = current.right
            else:
                raise ValueError(f"key {key} already exist") # вывод ошибки, нельзя добавить два одинаковых элемента

    
    def print_hierarhy(self,dir = "root", level = 0): # рекурсивный вывод дерева
        print(f"{[dir]}, level:{level} = {self.key}, TreeLeft = {self.left}, TreeRight = {self.right}")
        if self.left is not None:self.left.print_hierarhy("left", level+1) # проход по левой части, с каждым проходом уровень будет повышаться
        if self.right is not None:self.right.print_hierarhy("right", level+1) # проход по правой части
        
            


    