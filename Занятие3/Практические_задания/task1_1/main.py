def task():
    filename = "input.txt"
    f2 = r"C:\Users\murmam\PycharmProjects\PythonPY1101\Занятие3\Практические_задания\task1_2\output.txt"
    with open(filename) as f:  # менеджер контекста открывает файл в режиме чтения в текстовом формате "rt"
        for line in f:  # файл является итератором, который построчно возвращает свое содержимое
            # TODO c помощью метода строки strip очистить строку от непечатыемых символов
            line = line.strip()
            print(line)


if __name__ == "__main__":
    task()
