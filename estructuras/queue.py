"""
Queue (Cola) implementada con lista doblemente enlazada.

TODO:
- Implementa DoubleNode (value, prev, next)
- Implementa Queue con operaciones: enqueue, dequeue, peek, is_empty, size
- Enqueue al final (tail) y dequeue al inicio (head) para O(1)

Sugerencia:
- Mantén punteros a head y tail, más un contador.
"""

class DoubleNode:
    def __init__(self,value,prev,next):
        self.value = value
        self.prev = prev
        self.next = next

class Queue:
    def __init__(self):
        self.head = DoubleNode(None,None,None)
        self.tail = DoubleNode(None,self.head,None)
        self.head.next = self.tail
        self.size = 0

    def enqueue(self, value):
        """Inserta al final. O(1)"""
        nodo = DoubleNode(value,self.tail.prev,self.tail)
        self.tail.prev.next = nodo
        self.tail.prev = nodo
        self.size += 1

    def dequeue(self):
        """Extrae el primero. O(1). Debe lanzar IndexError si está vacía."""
        if self.size == 0 :
            raise IndexError
        nodo = self.head.next
        valor = nodo.value

        self.head.next = nodo.next
        nodo.next.prev = self.head
        self.size -=1
        return valor

    def peek(self):
        """Retorna el primero sin extraer. O(1). IndexError si vacía."""
        if self.size == 0 :
            raise IndexError
        return self.head.next.value
        

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

    def list(self):
        nodo = self.head.next
        list = []
        while nodo is not self.tail:
            list.append(nodo.value)
            nodo = nodo.next
        return list    
                
