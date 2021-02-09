"""Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * число см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т"""

class Road:
    # Атрибуты класса
    _length_road = 0
    _width_road = 0
    mass_road = 25
    thickness_road = 1
    result = 0

    # Конструктор для получения значения атрибутов из вне
    def __init__(self, length_road, width_road):
        self._length_road = length_road
        self._width_road = width_road
        print(f'Параметры нашей дороги, равны: \n Длина = {length_road} м \n Ширина = {width_road} м \n '
              f'Масса асфальта для покрытия одного кв метра = {Road.mass_road} кг \n '
              f'Толщина покрытия = {Road.thickness_road} см \n')

    # Метод расчета массы асфальта
    def mass_of_asphalt (self):
        Road.result = Road._length_road * Road._width_road * Road.mass_road * Road.thickness_road / 1000
        print(f"Потребуется асфальта = {Road.result} тон")



Road = Road(int(input("Введите длиную дороги в метрах \n")), int(input("Введите ширину дороги в метрах\n ")))
Road.mass_of_asphalt()
