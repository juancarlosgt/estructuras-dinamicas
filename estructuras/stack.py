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
    # TODO: implementar nodo simple
    pass

class Stack:
    # TODO: implementar pila enlazada
    def push(self, value):
        """Inserta en el tope. O(1)"""
        raise NotImplementedError

    def pop(self):
        """Extrae y retorna el tope. O(1). Debe lanzar IndexError si está vacía."""
        raise NotImplementedError

    def peek(self):
        """Retorna el tope sin extraer. O(1). IndexError si vacía."""
        raise NotImplementedError

    def is_empty(self):
        """True si no hay elementos. O(1)"""
        raise NotImplementedError

    def size(self):
        """Cantidad de elementos. O(1)"""
        raise NotImplementedError
