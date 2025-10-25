# Estructuras Dinámicas — Mini Biblioteca + Retos

Este repo contiene una **mini-biblioteca de estructuras** (Stack, Queue, LinkedList) y **3 retos** aplicados. La intención es practicar TDD: primero verás **pruebas unitarias iniciales** que fallan (fase *Red*), luego implementarás el mínimo código para hacerlas pasar (*Green*), y finalmente mejorarás (*Refactor*).

## Estructuras
- `Stack` sobre lista enlazada simple.
- `Queue` sobre lista doblemente enlazada.
- `LinkedList` (doblemente enlazada) con operaciones básicas.

## Retos
- **Reto 1 (Stack):** Validador de paréntesis/llaves/corchetes.
- **Reto 2 (Queue):** Simulador de cola de atención (FIFO).
- **Reto 3 (LinkedList):** Gestor de tareas (insertar, eliminar, buscar, recorrer).

## Cómo ejecutar pruebas
```bash
python -m unittest -v
```

## Sugerencias

* Sigue el patrón AAA (Arrange, Act, Assert) en las pruebas.
* Agrega más casos (bordes, errores esperados).
* Documenta complejidades Big-O en los READMEs de cada carpeta.


# Descripcion

- **Stack** : Almacena elementos mediante patron *LIFO* ; operaciones -> push, pop, peek , etc
- **Queue** : Almacena elementos mediante patron *FIFO* , se tienen nodos centinalas en head y tail ; operaciones -> enqueue, dequeue, etc
- **Linked List** : Lista en la que cada nodo tiene referencias al siguiente y al anterior mediante `head` y `prev` respectivamente.

## Retos

- **Reto 1** : Validar el balance y orden de parentesis `()` , llaves `{}` y corchetes `[]` , utilizando el *Stack*
- **Reto 2** : Cola de Atencion utilizando *Queue*
- **Reto 3** : Gestor de tareas: usa LinkedList para el manejo de tareas (insertar, eliminar, buscar).

## Complejidad Big O


Stack :
- push : `O(1)`
- pop : `O(1)`
- peek : `O(1)`

Queue :
- Enqueue : `O(1)`
- Dequeue : `O(1)`
- peek : `O(1)`

LinkedList :
- append : `O(1)`
- preppend : `O(1)`
- find : `O(n)`
- remove : `O(n)`
- list : `O(n)`
---
### Evidencia
![Evidencia de Pruebas](https://ibb.co/JhmgFns)

