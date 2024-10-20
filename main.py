class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        self.__vin = vin
        self.__numbers = numbers
        self.__is_valid_vin(self.__vin)
        self.__is_valid_numbers(self.__numbers)

    def __is_valid_vin(self, vin):
        if not isinstance(vin, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if not 1000000 <= vin <= 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return True

    def __is_valid_numbers(self, numbers):
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        return True
class IncorrectVinNumber(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


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




# # example a raise mistake
# # def greet_person(person_name):
# #     if person_name == 'VolDeMort':
# #         raise Exception('We dont love you, VolDeMort')
# #     print(f'Hello, {person_name}')
# #
# #
# # greet_person('Dear student')
# # greet_person('VolDeMort')
#
# #example 2
# # try:
# #     raise NameError('Hello there')
# # except NameError as exc:
# #     print(f'Exeption type {type(exc)} miss {exc.args}')
# #     raise
#
# # class ProZero(Exception):
# #     pass
# #
# #
# # def f(a, b):
# #     if b == 0:
# #         raise ProZero('Деление на нуль невозможно')
# #     return a / b
# #
# # print(f(4, 0))
#
# class ProZero(Exception):
#     def __init__(self,message, extra_info):
#         self.message = message
#         self.extra_info = extra_info
#
#
# def f(a, b):
#     if b == 0:
#         raise ProZero('Деление на нуль невозможно', {'a':a, 'b': b})
#     return a / b
#
#
# try:
#     result = f(10, 2)
# except ProZero as e:
#     print('Не очень хороший день, мы словили ошибку')
#     print(f'Сообщение об ошибке {e.message}')
#     print(f'Дополнительная информация {e.extra_info}')