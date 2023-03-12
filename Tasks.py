# nabor = ['s', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 's', 'd', 'f', 's', 'd', 'f', 'h', 'j', 'k']
# for i in range(len(nabor)):
#     k = 1
#     for j in range(i + 1, len(nabor)):
#         if nabor[j] == nabor[i]:
#             nabor[j] = nabor[j] + '_' + str(k)
#             k += 1
# print(nabor)

# string = 'a s d f g h j k l a s d f g d f g h j k'
# my_list = string.split()
# my_dict = {}
# new_list = []
# for letter in my_list:
#     my_dict[letter] = my_dict.get(letter, 0) + 1
#     if my_dict.get(letter) > 1:
#         new_list.append(letter + '_' + str(my_dict.get(letter)))
#     else:
#         new_list.append(letter)
# print(' '.join(new_list))



# string = 'asdf     asdfg  asdfgh   asdf  zxc     zxcv zxcv zxcvb'
# my_list = string.split()
# my_set = set(my_list)
# print(len(my_set))

# text = set(input().split())
# print(len(text))



# numbers = [1, 2, 3, 4, 5, 1, 3, 4]
# my_dict = {}
# new_list = []
# for num in numbers:
#     my_dict[num] = my_dict.get(num, 0) + 1
# for num in numbers:
#     if my_dict.get(num) <= 1:
#             new_list.append(num)
# print(new_list)

numbers = [1, 2, 3, 4, 5, 1, 3, 4]
# new_list = []
# for item in numbers:
#      if numbers.count(item) == 1:
#           new_list.append(item)
# print(new_list)

print([num for num in numbers if numbers.count(num) == 1])