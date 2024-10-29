#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# составить программу с использованием классов и объектов для решения задачи. Во всех заданиях, помимо указанных в
# задании операций, обязательно должны быть реализованы следующие методы:
# •	метод инициализации __init__;
# •	ввод с клавиатуры read;
# •	вывод на экран display.
# Номер варианта необходимо уточнить у преподавателя. В раздел программы, начинающийся после инструкции
# if __name__ = '__main__': добавить код, демонстрирующий возможности разработанного класса.
# Создать класс Point для работы с точками на плоскости. Координаты точки — декартовы. Обязательно должны быть
# реализованы: перемещение точки по оси X, перемещение по оси Y, определение расстояния до начала координат,
# расстояния между двумя точками, преобразование в полярные координаты, сравнение на совпадение и несовпадение.

import math
from abc import ABC, abstractmethod

# Интерфейс для работы с точками
class IPoint(ABC):
    @abstractmethod
    def distance_to_origin(self):
        pass

    @abstractmethod
    def distance_to_point(self, other_point):
        pass

    @abstractmethod
    def to_polar(self):
        pass

# Класс Point реализует интерфейс IPoint
class Point(IPoint):
    def __init__(self, x=0.0, y=0.0):
        """Инициализация координат точки (по умолчанию точка в начале координат)"""
        self.x = x
        self.y = y

    def move_x(self, dx):
        """Перемещение точки по оси X на dx"""
        self.x += dx

    def move_y(self, dy):
        """Перемещение точки по оси Y на dy"""
        self.y += dy

    def distance_to_origin(self):
        """Определение расстояния до начала координат"""
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def distance_to_point(self, other_point):
        """Определение расстояния между двумя точками"""
        if not isinstance(other_point, Point):
            raise ValueError("Переданный объект должен быть типа Point")
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

    def to_polar(self):
        """Преобразование координат точки в полярные координаты (r, θ)"""
        r = math.sqrt(self.x ** 2 + self.y ** 2)  # Радиус-вектор
        theta = math.atan2(self.y, self.x)  # Угол в радианах
        return (r, theta)

    def __eq__(self, other):
        """Сравнение точек на совпадение"""
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        """Сравнение точек на несовпадение"""
        return not self.__eq__(other)

# Интерфейс для ввода данных
class IReader(ABC):
    @abstractmethod
    def read(self) -> IPoint:
        pass

# Реализация ввода с консоли
class ConsoleReader(IReader):
    def read(self) -> Point:
        try:
            x = float(input("Введите координату X: "))
            y = float(input("Введите координату Y: "))
            return Point(x, y)
        except ValueError:
            print("Ошибка: координаты должны быть числами.")
            return None

# Интерфейс для вывода данных
class IDisplay(ABC):
    @abstractmethod
    def display(self, point: IPoint):
        pass

# Реализация вывода на консоль
class ConsoleDisplay(IDisplay):
    def display(self, point: Point):
        if point is None:
            print("Данные не заполнены.")
        else:
            print(f"Точка имеет координаты: ({point.x}, {point.y})")

# Фабрика для создания объекта Point
class PointFactory:
    @staticmethod
    def create(x: float, y: float) -> Point:
        return Point(x, y)

if __name__ == '__main__':
    # Демонстрация возможностей класса Point через фабрику
    print("Создание точки через фабрику:")
    point1 = PointFactory.create(3.0, 4.0)
    display = ConsoleDisplay()
    display.display(point1)

    # Ввод данных с консоли
    print("\nВвод данных с клавиатуры:")
    reader = ConsoleReader()
    point2 = reader.read()
    if point2:
        display.display(point2)

    # Перемещение точки по осям
    print("\nПеремещение первой точки:")
    point1.move_x(2.0)
    point1.move_y(-1.0)
    display.display(point1)

    # Вычисление расстояния до начала координат
    print(f"\nРасстояние от первой точки до начала координат: {point1.distance_to_origin():.2f}")

    # Вычисление расстояния между двумя точками
    if point2:
        print(f"Расстояние между первой и второй точками: {point1.distance_to_point(point2):.2f}")

    # Преобразование в полярные координаты
    r, theta = point1.to_polar()
    print(f"\nПолярные координаты первой точки: радиус = {r:.2f}, угол = {math.degrees(theta):.2f} градусов")

    # Сравнение точек
    if point2:
        print("\nСравнение точек:")
        if point1 == point2:
            print("Точки совпадают.")
        else:
            print("Точки не совпадают.")
