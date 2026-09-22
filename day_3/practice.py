# squares = [i for i in range (1,6)]
# print(squares)


#2
# num = 10
# if num %  2 == 0:
#     print("even")
# else:
#     print("odd")

# for i in range (1,11):
#     print(i)

#4
# sum = 0
# for i in range (1,11):
#     sum += i
# print(sum)

#5
# numbers = [10,25,5,40,15]
# largest = numbers[0]
# for num in numbers:
#     if num > largest:
#         largest = num
# print(largest)

# #6
# text = "dhruv"
# reverse = text[::-1]
# print(reverse)

# text = "madam"
# if text == text [::-1]:
#     print("palindrome")
# else:
#     print("non palindrome")

#7
text = "python programming"
count = 0
for i in text:
    if i in "aeiou":
        count += 1
print(count)
