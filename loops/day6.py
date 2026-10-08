#happy number
# n = int(input("enter the number:"))
# while n != 1 and n != 4:
#     total = 0
#     temp = n

#     while temp > 0:
#         last_digit = temp % 10 
#         total += last_digit * last_digit
#         temp //= 10

#     n = total
# if n == 1:
#     print("happy number")
# else: 
#     print("not happy number")

#PERFECT NUMBER 
# n = int(input("Enter a number: "))

# total = 0

# for i in range(1, n):
#     if n % i == 0:
#         total += i

# if total == n:
#     print("Perfect number")
# else:
#     print("Not a perfect number")


# #harshad  number
# n= int(input('enter the number:'))
# temp=n
# sum_of_digits=0
# while temp>0:
#     last_digit=temp%10
#     sum_of_digits+=last_digit
#     temp//=10
# if n%sum_of_digits==0:
#     print('harshad number')
# else:
#     print('not a harshad number')

#AUTOMORPIC NUMBER 

# n = int(input('enter a number:'))
# square = n*n 
# temp = n 
# digits = 0 
# while temp > 0:
#     digits += 1
#     temp //= 10
# power = 1
# for i in range(digits):
#     power *= 10
# if square % power == n:
#     print('automorpic number')
# else :
#     print('not anautomorpic number')

#DIZZARIUM NUMBER 
# n = int(input("enter a number:"))
# digit = 0
# temp = n
# while temp > 0 :
#     digit += 1
#     temp //= 10

# temp = n
# total = 0
# power = digit
# while temp >0:
#     last_digit = temp % 10 
#     total += last_digit ** power 
#     power -= 1
#     temp //= 10
# if total == n:
#     print('dizzarium number')
# else :
#     print('Not a dizzarium number')

#NEON NUMBER 
# n = int(input("Enter a number: "))

# sqr = n * n
# sum_digits = 0

# while sqr > 0:
#     digit = sqr % 10
#     sum_digits += digit
#     sqr 5//= 10

# if sum_digits == n:
#     print(n, "is a Neon number")
# else:
#     print(n, "is not a Neon number")

#SPY NUMBER
# n = int(input("Enter a number: "))

# sum_digits = 0
# product_digits = 1
# temp = n

# while temp > 0:
#     digit = temp % 10
#     sum_digits += digit
#     product_digits *= digit
#     temp //= 10

# if sum_digits == product_digits:
#     print(n, "is a Spy Number")
# else:
#     print(n, "is not a Spy Number")

#.FIBNOCCI SERIES 
# n = int(input("Enter the number of terms: "))

# a, b = 0, 1

# print("Fibonacci Series:")

# for i in range(n):
#     print(a, end=" ")
#     a, b = b, a + b

#or 

# n = int(input("Enter the number of terms: "))

# a = int(input("Enter the first of value terms: "))
# b = int(input("Enter the second of value: "))

# print("Fibonacci Series:")

# for i in range(n):
#     print(a, end=" ")
#     c = a + b
#     a = b
#     b = c 

#GCD

# a = int(input("Enter the first value : "))
# b = int(input("Enter the second value: "))
# gcd = 1
# limit = a
# if b < limit :
#     limit = b 
# for i in range( 1, limit + 1):
#     if a % i == 0 and b % i == 0:
#         gcd = 1 
# print('gretest Common Divisor=',gcd )

# #or 
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# while b != 0:
#     a, b = b, a % b

# print("GCD =", a)

    
# LCM 

a = int(input("Enter the first value : "))
b = int(input("Enter the second value: "))

lcm = a
while lcm % b != 0:
    lcm += a 
print('leeast Common Divisor=',lcm )

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# lcm = max(a, b)

# while True:
#     if lcm % a == 0 and lcm % b == 0:
#         break
#     lcm += 1

# print("LCM =", lcm)