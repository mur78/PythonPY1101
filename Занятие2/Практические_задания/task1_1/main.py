import sys


if __name__ == "__main__":
    squares_gen = (x * x for x in range(1000000))  # выражение генератор
    print(f"Размер выражения генератора: {sys.getsizeof(squares_gen)}")

    squares_list = [x * x for x in range(1000000)]  # list comprehension
    print(f"Размер списка: {sys.getsizeof(squares_list)}")

    print("-" * 10)

    print(f"Сумма с использованием выражения генератора: {sum(squares_gen)}")
    print(f"Сумма с использованием списка: {sum(squares_list)}")




