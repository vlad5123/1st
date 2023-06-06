
def calculator(func):

    def wrapper(expression):
        try:
            result = func(expression)
            return result
        except Exception as e:
            print(f"Calculation error: {e}")
            return None

    return wrapper



def calculate(expression):
    return eval(expression)
