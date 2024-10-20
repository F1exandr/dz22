import threading
import time

values = []

def input_values():
    while True:
        value = input("Введите значение (или 'q' для выхода): ")
        if value.lower() == 'q':
            break
        values.append(int(value))

def find_max():
    for _ in range(5):
        max_value = max(values)
        print(f"Максимум: {max_value}")
        time.sleep(1)

def find_min():
    for _ in range(5):
        min_value = min(values)
        print(f"Минимум: {min_value}")
        time.sleep(1)

input_values()

max_thread = threading.Thread(target=find_max)
min_thread = threading.Thread(target=find_min)

max_thread.start()
min_thread.start()

max_thread.join()
min_thread.join()