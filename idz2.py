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

class Point:
    def __init__(self, x=0.0, y=0.0):
        """Инициализация координат точки (по умолчанию точка в начале координат)"""
        self.x = x
        self.y = y

    def read(self):
        """Ввод координат точки с клавиатуры"""
        try:
            self.x = float(input("Введите координату X: "))
            self.y = float(input("Введите координату Y: "))
        except ValueError:
            print("Ошибка: координаты должны быть числами.")

    def display(self):
        """Вывод координат точки на экран"""
        print(f"Точка имеет координаты: ({self.x}, {self.y})")

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
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

    def to_polar(self):
        """Преобразование координат точки в полярные координаты (r, θ)"""
        r = math.sqrt(self.x ** 2 + self.y ** 2)  # Радиус-вектор
        theta = math.atan2(self.y, self.x)  # Угол в радианах
        return (r, theta)

    def __eq__(self, other):
        """Сравнение точек на совпадение"""
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        """Сравнение точек на несовпадение"""
        return not self.__eq__(other)

if __name__ == '__main__':
    # Демонстрация возможностей класса Point

    # Создание точки с помощью ввода с клавиатуры
    point1 = Point()
    point1.read()
    point1.display()

    # Создание второй точки через параметры
    point2 = Point(3.0, 4.0)
    print("Вторая точка:")
    point2.display()

    # Перемещение точки по осям
    print("\nПеремещение первой точки:")
    point1.move_x(2.0)
    point1.move_y(-1.0)
    point1.display()

    # Вычисление расстояния до начала координат
    print(f"\nРасстояние от первой точки до начала координат: {point1.distance_to_origin():.2f}")

    # Вычисление расстояния между двумя точками
    print(f"Расстояние между первой и второй точками: {point1.distance_to_point(point2):.2f}")

    # Преобразование в полярные координаты
    r, theta = point1.to_polar()
    print(f"\nПолярные координаты первой точки: радиус = {r:.2f}, угол = {math.degrees(theta):.2f} градусов")

    # Сравнение точек
    print("\nСравнение точек:")
    if point1 == point2:
        print("Точки совпадают.")
    else:
        print("Точки не совпадают.")
