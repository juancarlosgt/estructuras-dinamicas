import unittest
from retos.reto3_linkedlist import TaskManager

class TestChallenge3LinkedList(unittest.TestCase):
    def test_add_and_find_by_id(self):
        t = TaskManager()
        t.add_task(1, "Probar DLL", 2)
        tarea = t.find_by_id(1)
        self.assertIsNotNone(tarea)
        self.assertEqual(tarea["id"], 1)
        self.assertEqual(tarea["descripcion"], "Probar DLL")
        self.assertEqual(tarea["prioridad"], 2)

    # - eliminar por id (cuando implementes remove)
    def test_remove_task(self):
        t = TaskManager()
        t.add_task(1, "Probar DLL", 2)
        t.add_task(3, "Probar DLL2", 2)
        t.remove_task(1)
        self.assertEqual(1,t.get_size())  
        self.assertTrue(t.remove_task(3))
        self.assertEqual(0,t.get_size())
        self.assertFalse(t.remove_task(1))     



    # - find_by_priority devuelve múltiples tareas
    def test_find_by_priority(self):
        t = TaskManager()
        t.add_task(1, "Probar DLL 1", 1)
        t.add_task(2, "Probar DLL 2", 2)
        t.add_task(3, "Probar DLL 3", 1)
        t.add_task(4, "Probar DLL 4", 2)
        t.add_task(5, "Probar DLL 5", 1)
        list1 = t.find_by_priority(1)
        list2 = t.find_by_priority(2)
        self.assertEqual([
            {'id': 1, 'descripcion': 'Probar DLL 1', 'prioridad': 1},
            {'id': 3, 'descripcion': 'Probar DLL 3', 'prioridad': 1},
            {'id': 5, 'descripcion': 'Probar DLL 5', 'prioridad': 1}
            ],list1)
        self.assertEqual([
            {'id': 2, 'descripcion': 'Probar DLL 2', 'prioridad': 2},
            {'id': 4, 'descripcion': 'Probar DLL 4', 'prioridad': 2}
            ],list2)
    def test_find_by_priority_empty(self):
        t = TaskManager()
        self.assertEqual([],t.find_by_priority(1))    

    # - find_by_id inexistente -> None
    def test_non_existent_id(self):
        t = TaskManager()
        self.assertIsNone(t.find_by_id(999))

    def test_current_state(self):
        t = TaskManager()
        t.add_task(1, "Probar DLL 1", 1)
        t.add_task(2, "Probar DLL 2", 2)
        t.add_task(3, "Probar DLL 3", 3)
        t.add_task(4, "Probar DLL 4", 4)
        t.add_task(5, "Probar DLL 5", 5)
        lista = [
            {'id': 1, 'descripcion': 'Probar DLL 1', 'prioridad': 1},
            {'id': 2, 'descripcion': 'Probar DLL 2', 'prioridad': 2},
            {'id': 3, 'descripcion': 'Probar DLL 3', 'prioridad': 3},
            {'id': 4, 'descripcion': 'Probar DLL 4', 'prioridad': 4},
            {'id': 5, 'descripcion': 'Probar DLL 5', 'prioridad': 5}
        ]
        self.assertEqual(lista, t.get_list())

    def test_reverse_current_state(self):
        t = TaskManager()
        t.add_task(1, "Probar DLL 1", 1)
        t.add_task(2, "Probar DLL 2", 2)
        t.add_task(3, "Probar DLL 3", 3)
        t.add_task(4, "Probar DLL 4", 4)
        t.add_task(5, "Probar DLL 5", 5)
        lista = [
            {'id': 5, 'descripcion': 'Probar DLL 5', 'prioridad': 5},
            {'id': 4, 'descripcion': 'Probar DLL 4', 'prioridad': 4},
            {'id': 3, 'descripcion': 'Probar DLL 3', 'prioridad': 3},
            {'id': 2, 'descripcion': 'Probar DLL 2', 'prioridad': 2},
            {'id': 1, 'descripcion': 'Probar DLL 1', 'prioridad': 1}
        ]
        self.assertEqual(lista, t.get_reverse_list())  

if __name__ == "__main__":
    unittest.main()
