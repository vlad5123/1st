result = []

def divider(a, b):
    try:
        if a < b:
            raise ValueError("ValueError: a < b")
        if b > 100:
            raise IndexError("IndexError: b > 100")
        return a / b
    except Exception as e:
        print(type(e).__name__ + ": " + str(e))
        raise

data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8: 4}

for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except Exception as e:
        print(type(e).__name__ + ": " + str(e))

print(result)
