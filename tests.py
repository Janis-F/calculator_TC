import unittest
from calculator.calculator import Calculator


class MyTestCase(unittest.TestCase):

    def setUp(self, memory: float = 100) -> None:
        self.calculator = Calculator()
        self.memory = Calculator(memory)

    def test_addition(self) -> None:
        self.assertEqual(self.memory.addition(10), 110.0)

    def test_subtraction(self) -> None:
        self.assertEqual(self.memory.subtraction(10), 90)

    def test_multiplication(self) -> None:
        self.assertEqual(self.memory.multiply(10), 1000)

    def test_division(self) -> None:
        self.assertEqual(self.memory.division(10), 10)

    def test_memory(self) -> None:
        self.assertEqual(self.memory.memory, 100.0)

    def test_memory_reset(self) -> None:
        self.assertEqual(self.memory.reset_memory(), None)


if __name__ == '__main__':
    unittest.main()
