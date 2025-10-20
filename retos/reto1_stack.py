"""
Reto 1: Validador de expresión usando Stack.
Paréntesis válidos: (), {}, []

Función a implementar:
    validate_expression(expression: str) -> bool

Reglas:
- Recorre la cadena; apila aperturas; ante un cierre, desapila y compara.
- Si al final la pila queda vacía y nunca hubo desajuste -> True.

Tips:
- Usa Stack de estructuras/stack.py
"""

from estructuras.stack import Stack

PARES = {')': '(', '}': '{', ']': '['}
OPEN = {'(','[','{'}

def validate_expression(expression: str) -> bool:
    # TODO: Implementar con Stack siguiendo las reglas de arriba.
    # Debe ser O(n) en tiempo; O(n) espacio peor caso.

    pila = Stack()
    lista = list(expression)
    print(lista)
    for item in lista:

        print(item)
        if item in OPEN:
            pila.push(item)
            
        else :
            if PARES.get(item) == pila.pop():
                
                return True
            else :
                return False  
