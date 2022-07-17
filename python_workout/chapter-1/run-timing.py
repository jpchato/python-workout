"""
Asks the user repeatedly for numberic input. Prints the average time and number or runs
"""

from cProfile import run


def run_timing():
    numbers_of_runs = 0
    total_time = 0

    while True:
        one_run = input('Enter 10 km run time: ')

        if not one_run:
            break

        numbers_of_runs += 1
        total_time += float(one_run)

    average_time = total_time /  numbers_of_runs

    print(f'Average of {average_time}, over {numbers_of_runs} runs')

if __name__ == "__main__":
    run_timing()