"""
Reto 2: Simulador de atención usando Queue (FIFO).

Clase a implementar:
    class QueueManager:
        - add_person(nombre: str, tiempo: int) -> None
        - serve_person() -> tuple[str, int]   # (nombre, tiempo)
        - state() -> list[str]                # nombres en orden FIFO

Reglas:
- 'agregar_persona' encola al final.
- 'atender_persona' desencola y retorna la tupla; si está vacía, lanza IndexError.
- 'estado' retorna los nombres en el orden actual sin mutar la cola.

Tips:
- Usa Queue de estructuras/queue.py
"""

from estructuras.queue import Queue

class QueueManager:
    # TODO: implementar usando Queue internamente.
    def __init__(self):
        raise NotImplementedError

    def add_person(self, nombre: str, tiempo: int) -> None:
        raise NotImplementedError

    def serve_person(self) -> tuple[str, int]:
        raise NotImplementedError

    def state(self) -> list[str]:
        raise NotImplementedError