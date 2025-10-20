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
    # - atender_persona en cola vacía -> IndexError
        gestor2 = QueueManager()
        with self.assertRaises(IndexError):
            gestor2.serve_person()
    # - estado() refleja el orden actual
        gestor.add_person("Juan",3)
        gestor.add_person("Marcos",4)
        self.assertEqual("Luis - Juan - Marcos",gestor.state())
    # - mezcla de agregar/atender repetidas veces
        gestor.serve_person()
        gestor.add_person("Ruth",6)
        gestor.serve_person()
        gestor.add_person("Carlos",5)
        self.assertEqual("Marcos - Ruth - Carlos",gestor.state())

if __name__ == "__main__":
    unittest.main()
