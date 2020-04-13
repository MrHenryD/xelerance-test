import pandas as pd

def fib_odd_numbers(threshold):
    def fib(n):
        if n not in memoize.keys():
            memoize[n] = _fib(n)
        return memoize[n]

    def _fib(n):
        if n < 2:
            return n
        else:
            return fib(n-1) + fib(n-2)

    def sum_odd(numbers):
        sum_of_odd_numbers = sum([n for n in numbers if n % 2 == 1])
        return sum_of_odd_numbers
    
    memoize = {}
    numbers = []
    for seq in range(1, threshold):
        fib_seq = fib(seq)
        if fib_seq > threshold:
            break
        else:
            numbers.append(fib_seq)

    sum_odd_numbers = sum_odd(numbers)
    return sum_odd_numbers

def parse_residents(file, col):
    residents = pd.read_csv(file)
    if col in residents.columns:
        resident_names = residents[col].values
        print(resident_names)
    else:
        print('Invalid column')


if __name__ == '__main__':
    residents_file = 'address.csv'
    first_result = fib_odd_numbers(22)
    print(first_result)

    _ = parse_residents(residents_file, col='First name')