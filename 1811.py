#n = int(input())
#while n != 0:
 #   last_digit = n % 10
  #  n = n // 10
   # print(n)
#num = int(input())
#has_seven = False
#
#while num != 0:
 #   last_digit = num % 10
 #   if last_digit == 7:
 #       has_seven = True
 #   num = num // 10
#
  #  if has_seven == True:
  #      print('YES')
  #  else:
      #  print('NO')
#num = 123456789
#total = 0
#while num != 0:
 #   last_digit = num % 10
#    if last_digit > 4:
 #       total += 1

 #   num = num // 10

#print(total)


n = int(input())
sum = 0
product = 1
total = 0
while n != 0:
    last_digit = n % 10
    sum = sum + last_digit
    product = product * last_digit
    total += 1
    sar = sum / total
    n = n // 10
print(sum)
print(product)
print(total)
print(sar)
