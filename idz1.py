#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Парой называется класс с двумя полями, которые обычно имеют имена first и second. Требуется реализовать тип данных с
# помощью такого класса. Во всех заданиях обязательно должны  присутствовать:
# метод инициализации __init__ ; метод должен контролировать значения аргументов на корректность;
# ввод с клавиатуры read ;
# вывод на экран display .
# Реализовать внешнюю функцию с именем make_тип() , где тип — тип реализуемой структуры. Функция должна получать в
# качестве аргументов значения для полей структуры и возвращать  структуру требуемого типа. При передаче ошибочных
# параметров следует выводить сообщение и заканчивать работу. В раздел программы, начинающийсяпосле инструкции
# if __name__ = '__main__': добавить код, демонстрирующий возможности разработанного класса.
# Условия варианта 6:
# Поле first — целое положительное число, калорийность 100 г продукта; поле second —  дробное положительное число,
# масса продукта в килограммах. Реализовать метод power() — вычисление общей калорийности продукта.

class IPair:
    """Интерфейс для работы с парами значений."""
    def get_calories(self):
        raise NotImplementedError

class Pair(IPair):
    """Класс для хранения и расчета данных о продукте."""
    def __init__(self, first: int, second: float):
        if not isinstance(first, int) or first <= 0:
            raise ValueError("Поле 'first' должно быть целым положительным числом (калорийность 100 г продукта).")
        if not isinstance(second, (int, float)) or second <= 0:
            raise ValueError("Поле 'second' должно быть положительным числом (масса продукта в килограммах).")

        self.first = first
        self.second = second

    def get_calories(self):
        """Вычисление общей калорийности продукта."""
        return self.first * self.second * 10

class IReader:
    """Интерфейс для ввода данных."""
    def read(self) -> Pair:
        raise NotImplementedError

class ConsoleReader(IReader):
    """Реализация ввода данных с консоли."""
    def read(self) -> Pair:
        try:
            first = int(input("Введите калорийность 100 г продукта (целое положительное число): "))
            if first <= 0:
                raise ValueError
        except ValueError:
            print("Ошибка: значение калорийности должно быть целым положительным числом.")
            return None

        try:
            second = float(input("Введите массу продукта в килограммах (положительное число): "))
            if second <= 0:
                raise ValueError
        except ValueError:
            print("Ошибка: значение массы должно быть положительным числом.")
            return None

        return Pair(first, second)

class IDisplay:
    """Интерфейс для вывода данных."""
    def display(self, pair: Pair):
        raise NotImplementedError

class ConsoleDisplay(IDisplay):
    """Реализация вывода данных на консоль."""
    def display(self, pair: Pair):
        if pair is None:
            print("Данные не заполнены.")
        else:
            print(f"Калорийность 100 г продукта: {pair.first} ккал")
            print(f"Масса продукта: {pair.second} кг")
            print(f"Общая калорийность продукта: {pair.get_calories()} ккал")

class PairFactory:
    """Фабрика для создания объектов Pair."""
    @staticmethod
    def create(first: int, second: float) -> Pair:
        try:
            return Pair(first, second)
        except ValueError as e:
            print(f"Ошибка при создании объекта: {e}")
            return None

if __name__ == '__main__':

    # Пример использования PairFactory
    print("Создание объекта через PairFactory:")
    pair = PairFactory.create(250, 1.5)  # Калорийность 100 г = 250 ккал, масса = 1.5 кг
    display = ConsoleDisplay()
    if pair:
        display.display(pair)

    print("\nВвод данных вручную:")
    reader = ConsoleReader()  # Чтение данных с консоли
    pair2 = reader.read()  # Ввод с клавиатуры
    if pair2:
        display.display(pair2)
