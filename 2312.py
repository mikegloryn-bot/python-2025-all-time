# def get_middle_point(x1, y1, x2, y2):
#     mx = (x1 + x2) / 2
#     my = (y1 + y2) / 2
#     return mx, my
# print(get_middle_point(0, 0, 4, 6 ))

# def find_all(target, symbol):
#     result = []
#     for i in range(len(target)):
#         if target[i] == symbol:
#             result.append(i)
#     return result
# print(find_all('abcdabcaaa', 'a'))
# print(find_all('abcdabcaaa', 'e'))
# print(find_all('abcda

# def number_type(n):  # определяет тип числа
#     if n > 0:
#         return 'Положительное'
#     elif n < 0:
#         return 'Отрицательное'
#     else:
#         return 'Ноль'
# print(number_type(3))
# print(number_type(-19))
# print(number_type(0))
# print(number_type(32524))

def detect_type(v):
    if type(v) == int:
        return "int"
    elif type(v) == float:
        return "float"
    elif type(v) == list:
        return "list"
    elif type(v) == str:
        return "str"
    else:
        return "Неизвестный тип"
print(detect_type(232))
print(detect_type(2.5))
print(detect_type([1, 5, 0]))
print(detect_type("Loh"))
print(detect_type(True))