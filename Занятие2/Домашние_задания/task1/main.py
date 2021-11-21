from itertools import count

def task():
    for i in count(2, 1):
        q = 2
        z = i - 1
        # TODO с помощью yield до бесконечности
        yield z ** q




if __name__ == "__main__":
    numbers = task()

    for _ in range(11):
        print(next(numbers))


