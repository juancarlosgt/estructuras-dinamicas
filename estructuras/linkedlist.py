"""
Lista doblemente enlazada (DLL) para gestionar tareas.

TODO:
- Implementa DoubleNode (id, descripcion, prioridad, prev, next)
- Implementa DoublyLinkedList con: append, prepend, remove_by_id, find_by_id, find_by_prioridad, iter_forward, iter_backward, size
- Mantén head, tail y contador para O(1) en inserciones a extremos.

Nota:
- 'find' será O(n) lineal.
"""

class DoubleNode:
    # TODO: implementar nodo doble para tareas
    pass

class DoublyLinkedList:
    # TODO: implementar DLL
    def append(self, task):
        """Inserta al final. O(1)"""
        raise NotImplementedError

    def prepend(self, task):
        """Inserta al inicio. O(1)"""
        raise NotImplementedError

    def remove_by_id(self, task_id):
        """Elimina por id. O(n). Retorna True si elimina, False si no."""
        raise NotImplementedError

    def find_by_id(self, task_id):
        """Retorna la tarea o None. O(n)"""
        raise NotImplementedError

    def find_by_prioridad(self, prioridad):
        """Retorna lista de tareas con esa prioridad. O(n)"""
        raise NotImplementedError

    def iter_forward(self):
        """Generador hacia adelante."""
        raise NotImplementedError

    def iter_backward(self):
        """Generador hacia atrás."""
        raise NotImplementedError

    def size(self):
        """Cantidad de nodos. O(1)"""
        raise NotImplementedError
