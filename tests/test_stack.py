import unittest
from retos.reto1_stack import validate_expression

class TestChallenge1Stack(unittest.TestCase):
    def test_simple_balanced_expression(self):
        # Arrange
        expression = "({[]})"
        # Act
        resultado = validate_expression(expression)
        # Assert
        self.assertTrue(resultado)

    # - desbalance por cierre extra
    def test_unbalanced_extra_closure(self):
        expression = "([]])"
        resultado = validate_expression(expression)
        self.assertFalse(resultado)
    def test__incorrect_order(self):    
    # - orden incorrecto "{[}]"
        expression = "{[}]"
        resultado = validate_expression(expression)
        self.assertFalse(resultado)
    def test_empty_string(self):    
    # - cadena vacía -> True
        expression = ""
        resultado = validate_expression(expression)
        self.assertTrue(resultado)
    # - solo aperturas -> False
    def test_only_openings(self):
        expression = "[[[((({{"
        resultado = validate_expression(expression)
        self.assertFalse(resultado)

if __name__ == "__main__":
    unittest.main()
