class Calculator:
    """
        Calculator is a Python library for making simple mathematical computations.

        Calculator can perform the following operations:
        Addition;
        Subtraction;
        Multiplication;
        Division;
        Take root of memory;
        Keep track of internal memory and reset it.

        Methods:
        addition(self, input_number: float) -> float:
        subtraction(self, input_number: float) -> float:
        multiply(self, input_number: float) -> float:
        division(self, input_number: float) -> float:
        root(self, input_number: float) -> float:
        reset_memory(self) -> None:

    """

    def __init__(self, memory: float = 0.0) -> None:
        self._memory = memory

    def addition(self, input_number: float) -> float:
        """Add input number to the memory"""
        try:
            self._memory += float(input_number)
        except ValueError:
            print("Must be a number, not a string")
        except TypeError:
            print("Calculator doesn't support operations with complex numbers")
        return self._memory

    def subtraction(self, input_number: float) -> float:
        """Subtract input number from the memory"""
        try:
            self._memory -= float(input_number)
        except ValueError:
            print("Must enter a number, not a string")
        except TypeError:
            print("Calculator doesn't support operations with complex numbers")
        return self._memory

    def multiply(self, input_number: float) -> float:
        """Multiply memory by the input number"""
        try:
            self._memory *= float(input_number)
        except ValueError:
            print("Must enter a number, not a string")
        except TypeError:
            print("Calculator doesn't support operations with complex numbers")
        return self._memory

    def division(self, input_number: float) -> float:
        """Divide memory by the input number"""
        try:
            self._memory /= float(input_number)
        except ValueError:
            print("Must enter a number, not a string")
        except ZeroDivisionError:
            return 0.0
        except TypeError:
            print("Calculator doesn't support operations with complex numbers")
        return self._memory

    def root(self, input_number: float) -> float:
        """Take an input number level root from the memory """
        try:
            if input_number == 0:
                print("Can't take a zero-level root")
            else:
                self._memory **= 1. / float(input_number)
        except ValueError:
            print("Must enter a number, not a string")
        except TypeError:
            print("Calculator doesn't support operations with complex numbers")
        return self._memory

    @property
    def memory(self) -> float:
        return self._memory

    @memory.setter
    def memory(self) -> None:
        print("Memory can't be changed")

    def reset_memory(self) -> None:
        self._memory = 0
