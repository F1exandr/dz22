import threading
import random
import time

values = []

filled = False

def fill_list():
    global filled
    for _ in range(10):
        values.append(random.randint(1, 100))
        time.sleep(0.1)
    filled = True

def find_sum():
    while not filled:
        time.sleep(0.1)
    sum_value = sum(values)
    print(f"Сумма: {sum_value}")

def find_average():
    while not filled:
        time.sleep(0.1)
    average_value = sum(values) / len(values)
    print(f"Среднее арифметическое: {average_value}")

fill_thread = threading.Thread(target=fill_list)
sum_thread = threading.Thread(target=find_sum)
average_thread = threading.Thread(target=find_average)

fill_thread.start()
sum_thread.start()
average_thread.start()

fill_thread.join()
sum_thread.join()
average_thread.join()

print(f"Список: {values}")