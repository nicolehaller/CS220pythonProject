# CSCI 220/620
# Summer 2022
# Assignment 3
# Nicole Haller
import itertools
import random
import math


# part 1:
def find_postage(amount):
    for f in range(amount):
        for r in range(amount):
            if (5*f) + (4*r) == amount:
                return "five cent: " + str(f) + " four cent: " + str(r)
                return 0
    return "n/a"
    return 0


# part 2
def fib_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)


def fib_formula(n):
    fib = (1 / math.sqrt(5)) * ((((1 + math.sqrt(5)) / 2)**n) - (((1 - math.sqrt(5)) / 2)**n))
    return int(fib)


# part 3:
def gcd_recursive(a, b):
    if a == 0:
        return b  # gcd(0, b)= b
    else:
        return gcd_recursive((b % a), a)


#part 4:
# from https://www.codingem.com/python-how-to-get-all-combinations-of-a-list/
# and concept from https://docs.python.org/3/library/itertools.html
def all_strings(alphabet, size):
    prod = []
    for r in range(0, size+1):
         for combination in itertools.product(alphabet, repeat=r):
             prod.append(combination)
    print(prod)


def main():
    # part 1:
    print("part 1:")
    trials = 10
    for trial in range(trials):
        amount = random.randint(1, 100)
        print("Postage for", amount, "is", find_postage(amount))
    # part 2:
    print("part 2:")
    numbers = 10
    for n in range(2, numbers + 1):
        fr = fib_recursive(n)
        ff = fib_formula(n)
        print(n, "Fibonacci number recursive", fr, "formula", ff,
              "MATCH" if fr == ff else "ERROR")
    # part 3:
    print("part 3:")
    trials = 10
    for trial in range(trials):
        amount_1 = random.randint(1, 100)
        amount_2 = random.randint(1, 100)
        my_gcd = gcd_recursive(amount_1, amount_2)
        built_in_gcd = math.gcd(amount_1, amount_2)
        print("gcd of", amount_1, "and", amount_2, "- result from recursive function: ", my_gcd, "vs. result of built in math.gcd:", built_in_gcd,
              "MATCH" if my_gcd == built_in_gcd else "ERROR")
    # part 4:
    print("part 4:")
    print("all_strings(['a'], 10):")
    all_strings(['a'], 10)  # should produce 11 strings
    print()
    print("all_strings(['a', 'b', 'c'], 3):")
    all_strings(['a', 'b', 'c'], 3)  # should produce 3^4 - 1 = 80 strings


if __name__ == "__main__":
    main()
