class Calculator:
    def __init__(self):
        self.__result = 0

    def add(self, a):
        self.__result += a

    def subtract(self, a):
        self.__result -= a

    def multiply(self, a):
        self.__result *= a

    def divide(self, a):
        if a == 0:
            raise ValueError("Cannot divide by zero")
        self.__result /= a

    def modulo(self, a):
        if a == 0:
            raise ValueError("Cannot divide by zero")
        self.__result %= a

    def power(self, a):
        temp = self.__result
        for _ in range(a - 1):
            self.__result *= temp

    def square_root(self):
        self.__result = self.__result ** (1 / 2)

    def clear(self):
        self.__result = 0

    def get_result(self):
        return self.__result
