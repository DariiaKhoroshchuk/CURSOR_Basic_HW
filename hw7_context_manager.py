import pickle
import openpyxl

# 1
with open('task1.txt', 'r') as file:
    dict_sub = {}
    subtitles = file.readlines()
    for line in range(0, len(subtitles), 2):
        subtitles[line] = subtitles[line].replace('\n', '')
        subtitles[line+1] = subtitles[line+1].replace('\n', '')
        dict_sub.update({subtitles[line]: subtitles[line+1]})
for key, val in dict_sub.items():
    print(f'{key} : {val}')

# output:
# 00:00 : We all know you should take a sick day
# 00:01 : or a mental health day
# 00:03 : or even a personal day.
# 00:04 : But a financial day is just as important.
# ...

with open('task1_sub.txt', 'w') as file:
    for line in dict_sub.values():
        file.write(f'{line} ')

# file content:
# We all know you should take a sick day or a mental health day or even a personal day. But a financial day is just...

# 2
quantity = 0
total_sum = 0
with open('task2', 'rb') as file2:
    numbers = file2.read()
    numbers_b = pickle.loads(numbers)
print(f'List of numbers from the file: {numbers_b}.')
for i in numbers_b:
    total_sum += i
    quantity += 1
print(f'The sum of the file numbers is equal to {total_sum}.')
arithmetic_mean = total_sum / quantity
print(f'The arithmetic mean of the file numbers is equal to {arithmetic_mean}.')

# output:
# List of numbers from the file: [1, 1, 1, 1, 1, 1, 1, 2, 11, 11, 3123, 34, 12, 2, 324, 9, 9, 9, 10].
# The sum of the file numbers is equal to 3563.
# The arithmetic mean of the file numbers is equal to 187.52631578947367.


# 3
class OpenExcelFile:
    def __init__(self, file_name):
        self.file_obj = openpyxl.load_workbook(file_name)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file_obj.close()


with OpenExcelFile('task3.xlsx') as file:
    sheet = file.active
    sheet["A1"] = "Hello"
    sheet["B1"] = "world!"
    file.save('task3.xlsx')

print(sheet["A1"].value)
print(sheet["B1"].value)

# output:
# Hello
# world!
