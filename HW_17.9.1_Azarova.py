list_sequence = []

while not list_sequence:
    try:
        list_sequence = list(map(int, input("Введите несколько чисел через пробел: ").split()))
        if not list_sequence:
            print("Вы ничего не ввели.")

    except ValueError as e:
        print("Некорректный ввод")

other_numb = 0

while not other_numb:
    try:
        other_numb = int(input("Введите любое число: "))

    except ValueError as e:
        print("Некорректный ввод")


def sort():
    for i in range(1, len(list_sequence)):
        y = list_sequence[i]
        idx = i
        while idx > 0 and list_sequence[idx - 1] > y:
            list_sequence[idx] = list_sequence[idx - 1]
            idx -= 1
            list_sequence[idx] = y
    print('Список: ' + str(list_sequence))


def binary_search(array, element, left, right):
    if left > right:
        return left  # В списке нет числа, возвращаем ближайшее большее
    middle = (right + left) // 2
    if array[middle] == element:
        if middle == 0 or element > array[middle - 1]:
            return middle  # Найдено первое вхождение числа
        else:
            return binary_search(array, element, left, middle - 1)
            # Найдено вхождение числа, но оно не первое. Продолжаем искать слева
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)  # Продолжаем искать слева
    else:
        return binary_search(array, element, middle + 1, right)  # Продолжаем искать справа


sort()

if other_numb > list_sequence[-1]:
    print(f"Индекс числа перед числом {other_numb}: {len(list_sequence) - 1}.")
elif other_numb <= list_sequence[0]:
    print("В списке нет числа, меньше введенного.")
else:
    result = binary_search(list_sequence, other_numb, 0, len(list_sequence) - 1)
    print(f"Индекс числа, которое меньше числа {other_numb}: {result - 1}.")
