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

    def __init__(self, id, descripcion,prioridad,prev,next):
        self.id =id
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    # TODO: implementar DLL
    def __init__(self):
        self.head = DoubleNode(None,None,None,None,None)
        self.tail = DoubleNode(None,None,None,self.head,None)
        self.head.next = self.tail
        self.size = 0

    def append(self, task):
        """Inserta al final. O(1)"""
        tarea = DoubleNode(task["id"], task["descripcion"], task["prioridad"], None, None)
        tarea.prev = self.tail.prev
        tarea.next = self.tail
        self.tail.prev.next = tarea
        self.tail.prev = tarea
        self.size +=1

    def prepend(self, task):
        """Inserta al inicio. O(1)"""
        raise NotImplementedError

    def remove_by_id(self, task_id):
        """Elimina por id. O(n). Retorna True si elimina, False si no."""
        nodo = self.head
        while nodo is not self.tail:
            
            if nodo.id == task_id:
                nodo.prev.next = nodo.next
                nodo.next.prev = nodo.prev
                self.size -=1
                return True
            nodo = nodo.next    
        return False    

    def find_by_id(self, task_id):
        """Retorna la tarea o None. O(n)"""
        
        nodo = self.head
        while nodo is not self.tail:
            if nodo.id == task_id :
                tarea = {
                    "id":nodo.id,
                    "descripcion" : nodo.descripcion,
                    "prioridad":nodo.prioridad
                }
                return tarea
            nodo = nodo.next
        return None        
                
        

    def find_by_prioridad(self, prioridad):
        """Retorna lista de tareas con esa prioridad. O(n)"""
        lista = []
        nodo = self.head
        while nodo is not self.tail:
            if nodo.prioridad == prioridad :
                tarea = {
                    "id":nodo.id,
                    "descripcion" : nodo.descripcion,
                    "prioridad":nodo.prioridad
                }
                lista.append(tarea)
            nodo = nodo.next
        return lista  

    def iter_forward(self):
        """Generador hacia adelante."""
        lista = []
        nodo = self.head
        while nodo is not self.tail:
            if nodo is not self.head:
                tarea = {
                    "id":nodo.id,
                    "descripcion" : nodo.descripcion,
                    "prioridad":nodo.prioridad
                }
                lista.append(tarea)
            nodo = nodo.next
        return lista  

    def iter_backward(self):
        """Generador hacia atrás."""
        lista = []
        nodo = self.tail

        while nodo is not self.head:
            if nodo is not self.tail:
                tarea = {
                    "id":nodo.id,
                    "descripcion" : nodo.descripcion,
                    "prioridad":nodo.prioridad
                }
                lista.append(tarea)
            nodo = nodo.prev
        return lista  


    def get_size(self):
        """Cantidad de nodos. O(1)"""
        return self.size
    

