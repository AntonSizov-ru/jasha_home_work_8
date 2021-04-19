from random import randint
from time import time

list_len = [1000, 2000, 5000, 10000]


def random_generate(length):
    x = []
    for i in range(1, length):
        x.append(randint(1, length))
    return x


for a in list_len:
    random_list = random_generate(a)


    def selection_sort(input_list):

        start_time = time()  # время старта функции
        for i in range(len(input_list)):
            min_i = i
            for j in range(i + 1, len(input_list)):
                if input_list[min_i] > input_list[j]:
                    min_i = j
                input_list[i], input_list[min_i] = input_list[min_i], input_list[i]
        return time() - start_time  # время выполнения в секундах

    def insertion_sort(input_list):

        start_time = time()  # время старта функции
        for i in range(0, len(input_list)):
            item_to_insert = input_list[i]
            # И сохранить ссылку на индекс предыдущего элемента
            j = i - 1
            # Переместить все элементы отсортированного сегмента вперед, если они больше, чем элемент для вставки
            while j >= 0 and input_list[j] > item_to_insert:
                input_list[j + 1] = input_list[j]
                j -= 1
            # Вставляем элемент
            input_list[j + 1] = item_to_insert
        return time() - start_time  # время выполнения в секундах

    def py_sort(input_list):

        start_time = time()  # время старта функции
        for i in range(len(input_list)):
            input_list.sort()
        return time() - start_time  # время выполнения в секундах

    print(f'Размер списка - {a}, время сортировки этого списка функцией selection_sort - {selection_sort(random_list)}.'
          f'\nВремя сортировки этого списка функцией insertion_sort - {insertion_sort(random_list)}'
          f'\nВ то время как используя встроенную в python функцию list.sort() время сортировки составило - '
          f'{py_sort(random_list)}.\n')

'''
    Выводы:
    Одного взгляда достаточно чтобыувидеть, что сортировка вставками работает бысрее сортировки выбором, но при этом 
    сортировка встроенной функцией list.sort() для сортировки списков в python не так сильно отстаёт по затраченному 
    времени от сортировки вставками.
    Я думаю, что нет смысла изобретать велосипед, так как вряд ли он будет опережать на скорость света строенную 
    функцию, тем более, что python - не самый шустрый язык. 
    Результаты на моём ПК:
        Размер списка - 1000, время сортировки этого списка функцией selection_sort - 0.04684877395629883.
        Время сортировки этого списка функцией insertion_sort - 0.0
        В то время как используя встроенную в python функцию list.sort() время сортировки составило - 
        0.002992391586303711.
        
        Размер списка - 2000, время сортировки этого списка функцией selection_sort - 0.24733877182006836.
        Время сортировки этого списка функцией insertion_sort - 0.0
        В то время как используя встроенную в python функцию list.sort() время сортировки составило - 
        0.01296544075012207.
        
        Размер списка - 5000, время сортировки этого списка функцией selection_sort - 1.233701229095459.
        Время сортировки этого списка функцией insertion_sort - 0.001995086669921875
        В то время как используя встроенную в python функцию list.sort() время сортировки составило - 
        0.08377599716186523.
        
        Размер списка - 10000, время сортировки этого списка функцией selection_sort - 5.9700376987457275.
        Время сортировки этого списка функцией insertion_sort - 0.0019948482513427734
        В то время как используя встроенную в python функцию list.sort() время сортировки составило - 
        0.4438133239746094.
'''