# 1
import logging

temp_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
try:
    logging.basicConfig(level=logging.INFO, filename='file_logging9.log', filemode='a', format=temp_format)
except FileExistsError:
    logging.error('File not found!')
logging.info('Start calculator...')


def adding_num(num_1, num_2):
    addition = num_1 + num_2
    logging.info(f'Called adding_num function with numbers: {num_1}, {num_2}.')
    return addition


def subtraction_of_num(num_1, num_2):
    subtraction = (num_1 - num_2)
    logging.info(f'Called subtraction_of_num function with numbers: {num_1}, {num_2}.')
    return subtraction


def multiplication_of_num(num_1, num_2):
    multiplication = (num_1 * num_2)
    logging.info(f'Called multiplication_of_num function with numbers: {num_1}, {num_2}.')
    return multiplication


def division_of_num(num_1, num_2):
    logging.info(f'Called division_of_num function with numbers: {num_1}, {num_2}.')
    try:
        division = (num_1 / num_2)
    except ZeroDivisionError:
        logging.error('ZeroDivisionError', exc_info=True)
        division = 'ZeroDivisionError'
    return division


def raising_to_power(num_1, num_2):
    raising = (num_1 ** num_2)
    logging.info(f'Called raising_to_power function with numbers: {num_1}, {num_2}.')
    return raising


def root_of_num(num_1, num_2):
    root = (num_1 ** (1/num_2))
    logging.info(f'Called root_of_num function with numbers: {num_1}, {num_2}.')
    return root


def percentage_of_num(num_1, num_2):
    percent = ((num_1 / 100) * num_2)
    logging.info(f'Called percentage_of_num function with numbers: {num_1}, {num_2}.')
    return percent


while True:
    Dict_actions = {1: 'addition (+)', 2: 'subtraction (-)', 3: 'multiplication (*)', 4: 'division (÷)',
                    5: 'raise to the power (^)', 6: 'root (√)', 7: 'percentage of the number (%)'}

    for key, val in Dict_actions.items():
        print(f'{key}: {val}')

    action = int(input('Input the action you want to perform from the list using the key: '))
    logging.info('Action was entered.')

    if action == 6:
        print('You chose root (√). First number must be a number, second number - degree of the root.')
    elif action == 7:
        print('You chose percentage of the number (%). First number must be a percentage, second number - number.')

    try:
        num_1 = float(input('Input first number: '))
    except ValueError:
        print('First number is not a number...')
        continue
    logging.info(f'Entered first number {num_1}')
    try:
        num_2 = float(input('Input second number: '))
    except ValueError:
        print('Second number is not a number...')
        continue
    logging.info(f'Entered second number {num_2}')

    if action == 1:
        # num_1 = float(input('Input first number: '))
        # num_2 = float(input('Input second number: '))
        print(adding_num(num_1, num_2))
    elif action == 2:
        # num_1 = float(input('Input first number: '))
        # num_2 = float(input('Input second number: '))
        print(subtraction_of_num(num_1, num_2))
        # subtraction = a - b
    elif action == 3:
        # num_1 = float(input('Input first number: '))
        # num_2 = float(input('Input second number: '))
        print(multiplication_of_num(num_1, num_2))
        # multiplication = a * b
    elif action == 4:
        # num_1 = float(input('Input first number: '))
        # num_2 = float(input('Input second number: '))
        print(division_of_num(num_1, num_2))
        # division = a / b
    elif action == 5:
        # num_1 = float(input('Input number: '))
        # num_2 = int(input('Input power number: '))
        print(raising_to_power(num_1, num_2))
        # degree = a**b
    elif action == 6:
        # num_1 = float(input('Input number: '))
        # num_2 = int(input('Input power number: '))
        print(root_of_num(num_1, num_2))
    elif action == 7:
        # num_1 = float(input('Input percent number: '))
        # num_2 = float(input('Input number: '))
        print(percentage_of_num(num_1, num_2))
    else:
        print('There is no such key in the list')
        logging.info('No such action in the list.')
    logging.info(f'Action checked. Its {Dict_actions[action]}')
    logging.info('Result found!')

# 2


