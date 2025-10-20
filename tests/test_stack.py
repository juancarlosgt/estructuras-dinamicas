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
        expression = "([]])"
        resultado = validate_expression(expression)
        self.assertFalse(resultado)
    # - orden incorrecto "{[}]"
        expression = "{[}]"
        resultado = validate_expression(expression)
        self.assertFalse(resultado)
    # - cadena vacía -> True
        expression = ""
        resultado = validate_expression(expression)
        self.assertTrue(resultado)
    # - solo aperturas -> False
        expression = "[[[((({{"
        resultado = validate_expression(expression)
        self.assertFale(resultado)

if __name__ == "__main__":
    unittest.main()
