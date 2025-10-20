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
    # TODO: implementar nodo doble
    pass

class Queue:
    # TODO: implementar cola enlazada doble
    def enqueue(self, value):
        """Inserta al final. O(1)"""
        raise NotImplementedError

    def dequeue(self):
        """Extrae el primero. O(1). Debe lanzar IndexError si está vacía."""
        raise NotImplementedError

    def peek(self):
        """Retorna el primero sin extraer. O(1). IndexError si vacía."""
        raise NotImplementedError

    def is_empty(self):
        """True si la cola está vacía. O(1)"""
        raise NotImplementedError

    def size(self):
        """Cantidad de elementos. O(1)"""
        raise NotImplementedError
