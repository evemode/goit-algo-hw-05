import re
from typing import Callable

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

def generator_numbers(text: str):
    '''finds all digits in the text and return them via generator'''
    pattern = r' \d+\.\d+ '
    numbers = re.findall(pattern, text) # searching digits using pattern
    for num in numbers:
        try:
            yield float(num)
        except ValueError: #checking values
            continue

def sum_profit(text: str, func: Callable):
    '''sum of all incomes'''
    result = 0
    for num in func(text):
        result += num #summ all the income to result
    return result

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")