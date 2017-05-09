# DAY 1 ANDELA - PRIME NUMBER GENERATOR

This repo contains Python code that generates prime numbers from 0 to a given number n. It uses two functions, one that accepts input and then generates the prime number based on result from aother is_prime function

Various improvements are made to ensure the code performance is optimal.

Asymptotic analysis is later carried out on the program to measure the time space complexity.

There are also test cases provided

## Getting Started

Some prerequisites are required to have achieved desired output.

    This code is written in Python3 and may have unexpected functionality when run with Python 2.x

Install pytest:
```
$ pip install pytest

```

### Using the Code

clone the code from git using this limk:
```
git clone https://github.com/Bryoo/prime_numbers
```
Ensure you're in the main directory 'prime_numbers' and then run the code
```
python3 primenumbers.py
```

## Executing the tests included

```
$ py.test test_primenums.py
```
Alternatively, if you do not have pytest installed but with to, use:

```
$ python3 test_primenums.py
```

### The test cases present includes some tests for both edge and general cases:

```
### These are test cases for the is_prime function

def test_is_0_prime(self):  Tests output for zero
def test_is_2_prime(self):  Tests output for two
def test_is_5_prime(self):  Tests correct output for five
def test_is_4_prime(self):  Tests correct output for four

### These are test cases for the prime_generator function
def test_negative_num(self):    Tests output if the input n is a negative number
def test_input_type(self):      Tests output if input n is a non-integer


```
## Asymptotic Analysis

The code has got two loops. prime)generator has got a loop that iterates though all numbers till n and tests them against is_prime,

    all_primes = list(filter(is_prime, range(1, max_num)))

    The complexity of this loop is O(n)

The is_prime method has a loop that iterates to the square root of n as opposed to n:

limit = int(math.sqrt(num) + 1)  This for loop computes to a O(log n)
    for x in range(2, limit):
        if num % x == 0:  # not prime if divisible by other numbers
            return False
    else:
        return True
This makes it more efficient with a O(log n)
The rest of the statements compute to O(1)

Overally, the worst case is O(n log n)






