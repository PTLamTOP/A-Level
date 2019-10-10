# # # Пример 1 (нечетные числа)
# number = int(input())
# range_of_number = int(input())

# while number <= range_of_number:
#   if number%2:
#     print(number, end = ', ')
#   number += 1

# #..............................................................................................

# # Пример 2 (умножение суммы до какого-то числа)
# # #Вариант 1
# number1 = int(input())
# number2 = int(input())
# summ_1_2 = 0

# while number1 < number2:
# 	multiplication = number1*(number1+1)
# 	summ_1_2 += multiplication
# 	number1 += 1
# print(summ_1_2)

# # #Вариант 2
# number = int(input())
# x = 1
# summ = 0

# while x < number:
# 	summ += x*(x+1)
# 	x += 1
# print(summ)

# #..............................................................................................

# # Пример 3 (for and enumerate)
# sequence = [1, 2, 7, 19]

# for i in sequence:
# 	print(i)

# print("and")

# for key, value in enumerate(sequence):
# 	sequence[key] = value + 5
# 	sequence.sort
# print(sequence)


# #..............................................................................................
# # Пример 4 (срезы)
# String_1 = 'Hello guys! My name is Lam'
# List_1 = [1, 2, 5, 6, 7, 49, 86, 41]

# print(String_1[0:5]) 
# print(List_1[0:3])

# print('From: ', String_1[6:])
# print('Through 2 numbers: ', List_1[::3])

# print('From the end: ', List_1[::-1])

# #..............................................................................................
# # Пример 5 (строки)
print('he\'s very cool man \n but i am better:)')
print('i'*3)