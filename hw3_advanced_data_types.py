from functools import reduce

# 1. Define the id of next variables:
int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}

print(id(int_a))
print(id(str_b))
print(id(set_c))
print(id(lst_d))
print(id(dict_e))

# output:
# 9786624
# 140577465893296
# 140577465898816
# 140577466796224
# 140577466753728

# 2. Append 4 and 5 to the lst_d and define the id one more time.

lst_d.append(4)
lst_d.append(5)
print(lst_d)
print(id(lst_d))

# output:
# [1, 2, 3, 4, 5]
# 139813667215552

# 3. Define the type of each object from step 1.

print(type(int_a))
print(type(str_b))
print(type(set_c))
print(type(lst_d))
print(type(dict_e))

# output:
# <class 'int'>
# <class 'str'>
# <class 'set'>
# <class 'list'>
# <class 'dict'>

# 4*. Check the type of the objects by using isinstance.

print(isinstance(int_a, int))
print(isinstance(str_b, str))
print(isinstance(set_c, set))
print(isinstance(lst_d, list))
print(isinstance(dict_e, dict))

# output:
# True
# True
# True
# True
# True

# String formatting:
# Replace the placeholders with a value:
# "Anna has ___ apples and ___ peaches."

# 5. With .format and curly braces {}

print("Anna has {} apples and {} peaches.".format(5, 10))

# output:
# Anna has 5 apples and 10 peaches.

# 6. By passing index numbers into the curly braces.

print("Anna has {1} apples and {0} peaches.".format(5, 10))

# output:
# Anna has 10 apples and 5 peaches.

# 7. By using keyword arguments into the curly braces.

print("Anna has {apples} apples and {peaches} peaches.".format(apples=5, peaches=10))

# output:
# Anna has 5 apples and 10 peaches.

# 8*. With indicators of field size (5 chars for the first and 3 for the second)

print("Anna has {0:5} apples and {1:3} peaches.".format(5, 10))

# output:
# Anna has     5 apples and  10 peaches.

# 9. With f-strings and variables

apples = 6
peaches = 8
print(f"Anna has {apples} apples and {peaches} peaches.")

# output:
# Anna has 6 apples and 8 peaches.

# 10. With % operator

print("Anna has %s apples and %s peaches." % (apples, peaches))

# output:
# Anna has 6 apples and 8 peaches.

# 11*. With variable substitutions by name (hint: by using dict)

data_dict = {"apple": apples, "peach": peaches }
print("Anna has %(apple)s apples and %(peach)s peaches." % data_dict)

# output:
# Anna has 6 apples and 8 peaches.

# Comprehensions:
# (1)
lst = []
for num in range(10):
    if num % 2 == 1:
        lst.append(num ** 2)
    else:
        lst.append(num ** 4)
print(lst)

# (2)
list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]
print(list_comprehension)

# 12. Convert (1) to list comprehension

lst_comp1 = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(lst_comp1)

# output:
# [0, 1, 16, 9, 256, 25, 1296, 49, 4096, 81]
# output of (1):
# [0, 1, 16, 9, 256, 25, 1296, 49, 4096, 81]

# 13. Convert (2) to regular for with if-else

lst1 = []
for num in range(10):
    if num % 2 == 0:
        lst1.append(num // 2)
    else:
        lst1.append(num * 10)
print(lst1)

# output:
# [0, 10, 1, 30, 2, 50, 3, 70, 4, 90]
# output of (2):
# [0, 10, 1, 30, 2, 50, 3, 70, 4, 90]

# (3)
d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
print(d)

# (4)
d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
    else:
        d[num] = num // 0.5
print(d)

# (5)
dict_comprehension = {x: x**3 for x in range(10) if x**3 % 4 == 0}
print(dict_comprehension)

# (6)
dict_comprehension = {x: x**3 if x**3 % 4 == 0 else x for x in range(10)}
print(dict_comprehension)

# 14. Convert (3) to dict comprehension.

dict_comp1 = {num: num ** 2 for num in range(1, 10) if num % 2 == 1}
print(dict_comp1)

# output:
# {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
# output of (3):
# {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}

# 15*. Convert (4) to dict comprehension.

dict_comp2 = {num: num ** 2 if num % 2 == 1 else num // 0.5 for num in range(1, 11)}
print(dict_comp2)

# output:
# {1: 1, 2: 4.0, 3: 9, 4: 8.0, 5: 25, 6: 12.0, 7: 49, 8: 16.0, 9: 81, 10: 20.0}
# output of (4):
# {1: 1, 2: 4.0, 3: 9, 4: 8.0, 5: 25, 6: 12.0, 7: 49, 8: 16.0, 9: 81, 10: 20.0}


# 16. Convert (5) to regular for with if.

dict_comp3= {}
for x in range(10):
    if x ** 3 % 4 == 0:
        dict_comp3[x] = x ** 3
print(dict_comp3)

# output:
# {0: 0, 2: 8, 4: 64, 6: 216, 8: 512}
# output of (5):
# {0: 0, 2: 8, 4: 64, 6: 216, 8: 512}

# 17*. Convert (6) to regular for with if-else.

dict_comp4 = {}
for x in range(10):
    if x**3 % 4 == 0:
        dict_comp4[x] = x ** 3
    else:
        dict_comp4[x] = x
print(dict_comp4)

# output:
# {0: 0, 1: 1, 2: 8, 3: 3, 4: 64, 5: 5, 6: 216, 7: 7, 8: 512, 9: 9}
# output of (6):
# {0: 0, 1: 1, 2: 8, 3: 3, 4: 64, 5: 5, 6: 216, 7: 7, 8: 512, 9: 9}

# Lambda:

# (7)


def foo7(x, y):
    if x < y:
        return x
    else:
        return y


# (8)S


foo8 = lambda x, y, z: z if y < x and x > z else y


# 18. Convert (7) to lambda function


func = lambda x, y: x if x < y else y
print(func(6, 3))
print(foo7(6, 3))


# output:
# 3
# output of (7)
# 3

# 19*. Convert (8) to regular function

def func1(x, y, z):
    if y < x and x > z:
        return z
    else:
        return y


print(func1(2, 5, 9))
print(foo8(2, 5, 9))

# output:
# 5
# output of (7)
# 5

lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]

# 20. Sort lst_to_sort from min to max

print(sorted(lst_to_sort))

# output:
# [1, 5, 13, 15, 18, 24, 33, 55]

# 21. Sort lst_to_sort from max to min

print(sorted(lst_to_sort, reverse=True))

# output:
# [55, 33, 24, 18, 15, 13, 5, 1]

# 22. Use map and lambda to update the lst_to_sort by multiply each element by 2

new_lst_to_sort = list(map(lambda x: x * 2, lst_to_sort))
print(new_lst_to_sort)

# output:
# [10, 36, 2, 48, 66, 30, 26, 110]

# 23*. Raise each list number to the corresponding number on another list:

list_A = [2, 3, 4]
list_B = [5, 6, 7]

new_list_A = list(map(lambda i, k: i * k, list_A, list_B))
print(new_list_A)
# output:
# [10, 18, 28]

# 24. Use reduce and lambda to compute the numbers of a lst_to_sort.

new_lst_to_sort1 = reduce(lambda a, b: a + b, lst_to_sort)
print(new_lst_to_sort1)

# output:
# 164

# 25. Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.

new_lst_to_sort2 = list(filter(lambda elem: elem % 2 == 1, lst_to_sort))
print(lst_to_sort)
print(new_lst_to_sort2)

# output:
# [5, 18, 1, 24, 33, 15, 13, 55]
# [5, 1, 33, 15, 13, 55]

# 26. Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers.

b = range(-10, 10)
negative_num_lst = list(filter(lambda b: b < 0, b))
print(negative_num_lst)

# output:
# [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1]

# 27*. Using the filter function, find the values that are common to the two lists:
list_1 = [1,2,3,5,7,9]
list_2 = [2,3,5,6,7,8]

common_num = list(filter(lambda i: i in list_1, list_2))
print(list_1)
print(list_2)
print(common_num)

# output:
# [1, 2, 3, 5, 7, 9]
# [2, 3, 5, 6, 7, 8]
# [2, 3, 5, 7]

