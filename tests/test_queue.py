import unittest
from retos.reto2_queue import QueueManager

class TestChallenge2Queue(unittest.TestCase):
    def test_serve_in_fifo_order(self):
        gestor = QueueManager()
        gestor.add_person("Ana", 5)
        gestor.add_person("Luis", 3)

        nombre, tiempo = gestor.serve_person()
        self.assertEqual(nombre, "Ana")
        self.assertEqual(tiempo, 5)

    # agrega más casos:

    def test_serve_empty_queue(self):
    # - atender_persona en cola vacía -> IndexError
        gestor = QueueManager()
        with self.assertRaises(IndexError):
            gestor.serve_person()
    # - estado() refleja el orden actual
    def test_state_reflects_current_order(self):
        gestor = QueueManager()
        gestor.add_person("Luis", 3)
        gestor.add_person("Juan",3)
        gestor.add_person("Marcos",4)
        self.assertEqual([("Luis", 3),("Juan",3),("Marcos",4)],gestor.state())

    # - mezcla de agregar/atender repetidas veces
    def test_mixed_operations(self):
        gestor = QueueManager()  
        gestor.add_person("Luis", 3)  
        gestor.add_person("Marcos",4)
        gestor.serve_person()
        gestor.add_person("Ruth",6)
        gestor.serve_person()
        gestor.add_person("Carlos",5)
        gestor.add_person("Shirley",5)
        self.assertEqual([("Ruth",6),("Carlos",5),("Shirley",5)],gestor.state())

if __name__ == "__main__":
    unittest.main()