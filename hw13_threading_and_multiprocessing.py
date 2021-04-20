# 1. Write the method that return the number of threads currently in execution.
# Also prepare the method that will be executed with threads and run during the first method counting.
import time
from threading import Thread, activeCount, current_thread
from datetime import date
from multiprocessing import Process, current_process, Pool, cpu_count
from concurrent.futures import ProcessPoolExecutor


def foo1():
    for num in range(0, 30):
        print(f'Foo1: {num ** 2}')
        time.sleep(0.1)


def foo2():
    for num in range(0, 20):
        print(f'Foo2: {num ** 3}')
        time.sleep(0.3)


def run_time():
    print(f'Number of the active threads is {activeCount()}')


thread_1 = Thread(target=foo1)
thread_2 = Thread(target=foo2)

thread_1.start()
thread_2.start()

run_time()

thread_1.join()
thread_2.join()

# 2. Print current date by using 2 threads.
# #1. Define a subclass using Thread class.
# #2. Instantiate the subclass and trigger the thread.
today = date.today()


class DatePrinting(Thread):
    def current_date(self):
        name = current_thread().getName()
        print(name, "starting")
        d = today.strftime("%B %d, %Y")
        print(f"Today is: {d}")


if __name__ == "__main__":
    worker1 = DatePrinting()
    worker2 = DatePrinting()
    thread_1 = Thread(target=worker1.current_date)
    thread_2 = Thread(target=worker2.current_date)
    thread_1.start()
    thread_2.start()
    print("All threads are in queued, let's see when they finished!")
    thread_1.join()
    thread_2.join()
    print('All threads are finished!')


# 3. Use Pool.apply() to get the row wise common items in list_a and list_b.

list_a = [[1, 2, 3], [5, 6, 7, 8], [10, 11, 12], [20, 21]]
list_b = [[2, 3, 4, 5], [6, 9, 10], [11, 12, 13, 14], [21, 24, 25]]
common_items = []


def get_common_items(a, b):
    set_a = set(a)
    set_b = set(b)
    return list(set_a.intersection(set_b))


with Pool() as pool:
    for i in range(len(list_a)):
        common_items.append(pool.apply(get_common_items, [list_a[i], list_b[i]]))
    print(common_items)

# 4. Divide the work between 2 methods: print_cube that returns the cube of number
# and print_square that returns the square of number.
# These two methods should be executed by using 2 different processes.


def print_cube(number1):
    name = current_process().name
    print(name, "starting")
    cube = pow(number1, 3)
    print(f'The cube of number {number1} equal to: {cube}.')


def print_square(number2):
    name = current_process().name
    print(name, "starting")
    square = pow(number2, 2)
    print(f'The square of number {number2} equal to: {square}.')


with ProcessPoolExecutor(max_workers=2) as pool:
    pool.submit(print_cube)
    pool.submit(print_square)
    cube_result = Process(name='cube of number', target=print_cube, args=(4, ))
    square_result = Process(name='square of number', target=print_square, args=(3, ))
    cube_result.start()
    square_result.start()

    print(f"Starting computations on {cpu_count()} cores.")

    # cube_result.join()
    # square_result.join()

print('All processes are finished!')

