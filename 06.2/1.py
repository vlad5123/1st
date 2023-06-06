import time

def calculate_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Початковий час виконання

        result = func(*args, **kwargs)  # Виклик оригінальної функції

        end_time = time.time()  # Кінцевий час виконання
        execution_time = end_time - start_time  # Час виконання

        return result

    return wrapper
