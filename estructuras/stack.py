"""
Stack (Pila) implementado con lista enlazada simple.

TODO:
- Implementa Node (valor, next)
- Implementa Stack con operaciones: push, pop, peek, is_empty, size
- Garantiza que push y pop sean O(1)

Sugerencia:
- Mantén referencia a la "cabeza" (top) y un contador de tamaño.
"""

class Node:
    def __init__(self,value,next):
        self.value = value
        self.next = next

class Stack:
    def __init__(self):
        self.top = Node(None,None)
        self.size = 0
    def push(self, value):
        """Inserta en el tope. O(1)"""
        if self.size == 0 :
            self.top.value = value
        else :
            newTop = Node(value,self.top) 
            self.top = newTop   
        self.size +=1    

    def pop(self):
        """Extrae y retorna el tope. O(1). Debe lanzar IndexError si está vacía."""
        if self.size == 0:
            raise IndexError
        value = self.top.value
        self.top = self.top.next
        self.size -=1
        if self.size == 0:
            self.__init__()
        return value

    def peek(self):
        """Retorna el tope sin extraer. O(1). IndexError si vacía."""
        return self.top.value

    def is_empty(self):
        """True si no hay elementos. O(1)"""
        empty = self.size == 0
        return empty

    def get_size(self):
        """Cantidad de elementos. O(1)"""
        return self.size
    
    
