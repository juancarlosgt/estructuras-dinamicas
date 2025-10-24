"""
Reto 3: Gestor de tareas con DoublyLinkedList.

Funciones a implementar (usa DoublyLinkedList de estructuras/linkedlist.py):
    - add_task(id:int, descripcion:str, prioridad:int) -> None
    - find_by_id(id:int) -> dict|None
    - find_by_priority(prioridad:int) -> list[dict]

Nota:
- La lista interna debe almacenar dicts con llaves: id, descripcion, prioridad.
"""

from estructuras.linkedlist import DoublyLinkedList

#_lista_tareas = DoublyLinkedList()
class TaskManager :

    def __init__(self):
        self.lista_tareas = DoublyLinkedList()

    def add_task(self,task_id: int, descripcion: str, prioridad: int) -> None:
        # crear dict y agregar al final (append) en O(1)

        tarea = {
            "id": task_id,
            "descripcion":descripcion,
            "prioridad":prioridad,
        }
        self.lista_tareas.append(tarea)

    def find_by_id(self,task_id: int):
        # delegar en DLL.find_by_id (O(n))

        return self.lista_tareas.find_by_id(task_id)

    def remove_task(self,task_id: int) -> bool:
        return self.lista_tareas.remove_by_id(task_id)

    def find_by_priority(self,prioridad: int):
        # TODO: delegar en DLL.find_by_prioridad (O(n))
        return self.lista_tareas.find_by_prioridad(prioridad)

    def get_size(self):
        return self.lista_tareas.get_size()

    def get_list(self):
        return self.lista_tareas.iter_forward()
    
    def get_reverse_list(self):
        return self.lista_tareas.iter_backward()
