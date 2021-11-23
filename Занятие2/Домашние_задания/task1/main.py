from itertools import count



def task(q):
      for i in count(2, 1):
        z = i - 1
        # TODO с помощью yield до бесконечности
        yield q ** z


if __name__ == "__main__":
    numbers = task(int(input("Введите q: ")))

    for _ in range(11):
        print(next(numbers))


