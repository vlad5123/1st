# 1 - iterators
# 0  1  2  3  4
lessons = [1, 2, 3, 4, "Test5", 8, 10, 22, "Serhii", True, 1.0]
iterator = iter(lessons)
# print(iterator)
'''
try:
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
except StopIteration:
    print("StopIteration")
'''
try:
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    for elem in iterator:
        print(f"from for: {elem}")
    print(next(lessons))
except TypeError as te:
    print(te)
