result = []

def divider(a, b):
    try:
        if a < b:
            raise ValueError("Перше число менше за друге")
        if b > 100:
            raise IndexError("Значення b більше 100")
        return a / b
    except ValueError as ve:
        print(f"ValueError: {ve}")
        return None
    except IndexError as ie:
        print(f"IndexError: {ie}")
        return None
    except ZeroDivisionError as zde:
        print(f"ZeroDivisionError: {zde}")
        return None
    except TypeError as te:
        print(f"TypeError: {te}")
        return None

data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}  # Видалено [] як ключ

for key in data:
    try:
        res = divider(key, data[key])
        if res is not None:
            result.append(res)
    except Exception as e:
        print(f"Помилка при обробці пари ({key}, {data[key]}): {e}")

print("Результат:", result)
