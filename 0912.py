# s = 'foO BaR 123 BAZ quX'
# print(s.capitalize()) # делает строку с большой буквы
# print(s.swapcase())  # меняет размер символов на противоположный
# print(s.title()) # каждое слово с большой буквы
# print(s.lower()) # все символы маленькие
# print(s.upper()) # всё с большой буквы
# s = input()
# if s == s.title():
#     print('YES')
# else:
#     print('NO')
# s = input()
# g = 'хорош'
# if g in s.lower():
#     print('YES')
# else:
#     print('NO')
# s = 'foobar'
# print(s.endswith('bar'))
# print(s.find("foo"))
# print(s.find("bar"))
# s = input()
# print(s.count(' ') + 1)
# a = input()
# total = 0
# for g in '0123456789':
#     total += a.count(g)
# print(total)
# t = input()
# if t.endswith('.com') or t.endswith('.ru'):
#     print('YES')
# else:
#     print('NO')
t = input()
first = t.find('f')
last = t.rfind('f')
if first == -1:
    print('NO')
elif first == last:
    print(first)
else:
    print(first, last)