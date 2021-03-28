# 1
import logging
import time

class NoProgramInList(Exception):
    pass

Dict_program = {1: 'Calculator', 2: 'Vacuum cleaner operation'}
for key, val in Dict_program.items():
    print(f'{key}: {val}')

program = int(input('Enter the program you want to run from the list using the key: '))
try:
    if program == 1:

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
            logging.info(f'Called root_of_num function with numbers: {num_1}, {num_2}.')
            try:
                root = (num_1 ** (1/num_2))
            except ZeroDivisionError:
                logging.error('ZeroDivisionError', exc_info=True)
                root = 'ZeroDivisionError'
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
                print('You chose percentage of the number (%). First number must be a percentage,'
                      ' second number - number.')

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
    elif program == 2:

        class LowWater(Exception):
            pass


        class NotEnoughCharge(Exception):
            pass


        class OverflowingGarbageCan(Exception):
            pass


        class WaterIsOver(Exception):
            pass


        class ChargeIsOver(Exception):
            pass


        class CleanGarbageCan(Exception):
            pass


        class VacuumCleaner:
            used_charge = 5
            used_water = 10
            used_occupancy = 3

            def __init__(self, charge, occupancy, water):
                self.charge = charge
                self.occupancy = occupancy
                self.water = water

            def wash(self):
                if self.water <= self.used_water:
                    self.water = 0
                else:
                    self.water -= self.used_water
                    print(f'Washing... There is {self.water}% of water.')
                if 0 < self.water < 20:
                    self.water -= self.used_water
                    raise LowWater
                if self.water == 0:
                    raise WaterIsOver
                # print(f'Washing... There is {self.water}% of water.')

            def vac_cleaner(self):
                if self.occupancy >= 100 - self.used_occupancy:
                    self.occupancy = 100
                else:
                    self.occupancy += self.used_occupancy
                    print(f'Cleaning... Used {self.occupancy}% of garbage can.')
                if 90 < self.occupancy < 100:
                    raise OverflowingGarbageCan
                if self.occupancy == 100:
                    raise CleanGarbageCan
                # print(f'Cleaning... Used {self.occupancy}% of garbage can.')

            def move(self):
                while True:
                    print(f'Start vacuum... Charge: {self.charge}%, water: {self.water}%, trash: {self.occupancy}%')
                    try:
                        if self.charge <= self.used_charge:
                            self.charge = 0
                        else:
                            self.charge -= self.used_charge
                        if 5 < self.charge < 10:
                            self.water -= self.used_water
                            raise NotEnoughCharge
                        if self.charge == 0:
                            raise ChargeIsOver
                        print(f'There is {self.charge}% of charge.')
                    except NotEnoughCharge:
                        print('>>NotEnoughCharge<<')
                        print('>>Please, charge me... The charge expires. It may not be enough for the next flight.<<')
                    except ChargeIsOver:
                        print('>>ChargeIsOver<<')
                        print('>>I am dying...<<')
                        break

                    try:
                        self.wash()
                    except LowWater:
                        print('>>LowWater<<')
                        print('>>Please, add water... The water expires. It may not be enough for the next flight.<<')
                    except WaterIsOver:
                        print('>>WaterIsOver<<')
                        print('>>The water is over. Washing stopped...<<')
                        continue

                    try:
                        self.vac_cleaner()
                    except OverflowingGarbageCan:
                        print('>>OverflowingGarbageCan<<')
                        print('>>Please, clean garbage can... The space for trash expires. '
                              'It may not be enough for the next flight.<<')
                    except CleanGarbageCan:
                        print('>>CleanGarbageCan<<')
                        print('>>Please, clean garbage can. The garbage can is full.<< \n>>Cleaning stopped...<<')
                        continue
                    time.sleep(1)

        print('Test1. Cleaning...')
        vacuum_cleaner1 = VacuumCleaner(charge=50, water=80, occupancy=0)
        vacuum_cleaner1.move()
        print('Test2. Cleaning...')
        vacuum_cleaner2 = VacuumCleaner(charge=80, water=35, occupancy=50)
        vacuum_cleaner2.move()
        print('Test3. Cleaning...')
        vacuum_cleaner3 = VacuumCleaner(charge=80, water=80, occupancy=90)
        vacuum_cleaner3.move()

    else:
        raise NoProgramInList

except NoProgramInList:
    print('There is no such key in the list. Try again...')


