import threading
import time

values = []

def input_values():
    while True:
        value = input("Введите значение (или 'q' для выхода): ")
        if value.lower() == 'q':
            break
        values.append(int(value))

def find_sum():
    for _ in range(5):
        sum_value = sum(values)
        print(f"Сумма: {sum_value}")
        time.sleep(1)

def find_average():
    for _ in range(5):
        average_value = sum(values) / len(values)
        print(f"Среднее арифметическое: {average_value}")
        time.sleep(1)

input_values()

sum_thread = threading.Thread(target=find_sum)
average_thread = threading.Thread(target=find_average)

sum_thread.start()
average_thread.start()

sum_thread.join()
average_thread.join()