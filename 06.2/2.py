
def perform_calculation(n):

    result = 0
    for i in range(n):
        result += i
    return result


result = perform_calculation(1000000)
print(result)

def test_calculation():
    result = perform_calculation(1000000)
    expected_result = 499999500000
    assert result == expected_result

test_calculation()
