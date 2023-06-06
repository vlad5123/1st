
def perform_calculation(n):

    result = 0
    for i in range(n):
        result += i
    return result


result = perform_calculation(1000000)
print(result)
