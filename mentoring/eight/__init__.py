class AdultAgeException(Exception):
    """Exception raised for invalid age values.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message="Age must be more then", age=18):
        self.message = message
        self.age = age
        super().__init__(f'{self.message} {self.age}')


def is_adult(customer_list):
    for elem in customer_list:
        try:
            if elem["customer"]["age"] < 18:
                raise AdultAgeException()
        except AdultAgeException as e:
            print(f'Customer age is {elem["customer"]["age"]}. {e}')
        except Exception:
            print("Something go wrong")
        else:
            print('Nice I can take a beer!!')
        finally:
            print('Meh, I will always RUN')
