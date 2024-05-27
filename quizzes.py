#ranges
# n = 6
# if (n % 2) != 0:
#     print("Weird")
# elif (n in range(2,6)):
#     print("Not Weird")
# elif n in range(6,21):
#     print("Weird")
# elif n > 20:
#     print("Not Weird")

##calculate leap year
# def is_leap(year):
#     leap = False
        
#     four = year % 4
#     hundred = year % 100
#     fourhundred = year % 400
#     print(four)
#     print(hundred)
#     print(fourhundred)

#     if four == 0 and (hundred != 0 or fourhundred == 0):
#         leap = True
#     print(leap)
    
#     return leap

# is_leap(2020)


## print range without string method
# pattern = range(1,4)
# message = ""
# for i in pattern:
#     message = message + str(i)
# print(message)

#record frequency of each digit in a number in a map
n = 9
frequency_map = {}

while n > 0:
    digit = n % 10
    if digit not in frequency_map:
        frequency_map[digit] = 1
    else:
        frequency_map[digit] = frequency_map[digit] + 1
    n = int(n / 10)
print(frequency_map)