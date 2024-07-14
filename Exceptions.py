class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class Car:
    def __init__(self, model, vin, numbers=None):
        self.model = model
        try:
            self.__is_valid_vin(vin)
            self.__vin = vin
        except IncorrectVinNumber as e:
            print(e)
            raise

        if numbers:
            try:
                self.__is_valid_numbers(numbers)
                self.__numbers = numbers
            except IncorrectCarNumbers as e:
                print(e)
                raise
        else:
            self.__numbers = str(vin)  # Предполагаем, что номера производятся из VIN

    def __is_valid_vin(self, vin_number):
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип VIN номера')
        if not 1000000 <= vin_number <= 9999999:
            raise IncorrectVinNumber('Неверный диапазон для VIN номера')
        return True

    def __is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        return True

    def set_vin(self, vin):
        try:
            self.__is_valid_vin(vin)
            self.__vin = vin
            self.__numbers = str(vin)
        except IncorrectVinNumber as e:
            print(e)

    def set_numbers(self, numbers):
        try:
            self.__is_valid_numbers(numbers)
            self.__numbers = numbers
        except IncorrectCarNumbers as e:
            print(e)

    def get_vin(self):
        return self.__vin

    def get_numbers(self):
        return self.__numbers


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
