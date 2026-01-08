# def draw_box():
#     for _ in range(5):
#         print('*' * 7)
# def draw_box(height, width):
#     for i in range(height):
#         print('*' * width)
# draw_box(5, 7)
# print()
# draw_box(4, 4)
# print()
# draw_box(3, 9)
# print()
# draw_box(30, 30)
# n = 3
# m = 9
# draw_box(n, m)
# birds = 5000
# def print_texas():
#     print('В Техасе обитает', birds, 'птиц.')
# def print_california():
#     print('В Калифорнии обитает', birds, 'птиц.')
# print_texas()
# print_california()
# def con_to_byn(mon):
#     result = mon * 2.94
#     return result
# mon = float(input('Введите кол-во долларов:'))
# byn = con_to_byn(mon)
# print(byn, 'BYN')
# def compute_hypotenuse(a, b):
#     c = (a ** 2 + b ** 2) ** 0.5
#     return c
# print(compute_hypotenuse(3, 4))
# print(compute_hypotenuse(5, 12))
# print(compute_hypotenuse(1, 1))
# def sum_digits(n):
#     result = 0
#     while n > 0:
#         result += n % 10
#         n //= 10
#     return result
# n = int(input())
# print(sum_digits(n))
# def average(numbers):
#     result = sum(numbers) / len(numbers)
#     return result
# numbers = [1, 3, 5, 1, 6, 8, 10, 2]
# print(average(numbers))
# def date_format(day, month, year):
#     return f'{year}-{month}-{day}'
# print(date_format(31, 12, 2025))
# def get_highest(names, heights):
#     max_height = max(heights)
#     index_max_height = heights.index(max_height)
#     return names[index_max_height]
# print(
#     get_highest(
#         ['Андрей', 'Валерий', 'Елена', 'Николай', 'Жанна'],
#         [1.75, 1.61, 1.65, 1.83, 1.64],
#     )
# )
# def draw_box(height):
#     for i in range(height):
#         print('*        *')
# print('**********')
# draw_box(13)
# print('**********')
# def draw_treugolnik(weidth):
#     print('*' * weidth)
# draw_treugolnik(1)
# draw_treugolnik(2)
# draw_treugolnik(3)
# draw_treugolnik(4)
# draw_treugolnik(5)
# draw_treugolnik(6)
# draw_treugolnik(7)
# draw_treugolnik(8)
def merge(list1, list2):
    result = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    result.extend(list1[i:])
    result.extend(list2[j:])
    return result
print(merge([1, 2, 3], [5, 6, 7]))
print(mergep)