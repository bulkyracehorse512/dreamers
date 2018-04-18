#!/usr/bin/env
# Pemdas Challenge
# Time Estimate: 2 hours

# Using digits 1, 3, 4, 6 and any operation, reach a total of 24
from itertools import (
    chain,
    combinations_with_replacement,
    permutations,
)
import operator
import time


def operations(num):
    """ Orders math operations in all possible permutations and all possible
    combinations. Operations may be performed in any order, any number of
    times.
    """
    ops = [operator.add, operator.sub, operator.truediv, operator.mul]
   
    # List all combinations of operators
    combinations = list(combinations_with_replacement(ops, num))

    # For each combination list all possible orders of operations
    perms = []
    for combo in combinations:
        perms.append(list(permutations(combo)))

    # Return flattened permutations
    return set(chain(*perms))


def num_perms(inputs):
    """ Orders integers in all permutations.  Digits must be used once and only
    once, in any order.
    """
    return list(permutations(inputs))


def generate_solutions(digits, target):
    string = ""
   
    def compute(digits, target, operations):
        nonlocal string

        head, *tail = digits
        if tail == [] or operations == []:
            string += "{})".format(head)
            return head
        op = operations.pop()

        string += "{} ({}, ".format(op.__name__, head)
        try:
            return op(head, compute(tail, target, operations))
        except ZeroDivisionError:
            return

    op_set = operations(len(digits) - 1)
    combos = num_perms(digits)
    answers = []
    for ops in op_set:
        for combo in combos:
            total  = compute(combo, 24, list(ops))
            if total == target:
                answers.append((total, string))
            string = ""
    return answers


def format_results(results, inputs, perms, total):
    """
    """
    inputs = ', '.join(str(i) for i in inputs)
    
    if results:
        print ("".join([
            "The following combinations for the given inputs: {} ",
            "successfully totaled to '{}': ",
        ]).format(inputs, str(total)))
        print ("\n".join(results))
        print ("There were {} total solutions.".format(len(results)))

    else:
        print ("".join([
            "No combination of operations resulted in the given total {} ",
            "for inputs {}",
        ]).format(inputs, str(total)))

    print("The program exexuted {} total permutations".format(len(perms)))


def main():
    initial_input = (1, 3, 4, 6)
    initial_total = 24
    
    # Perform calculation for inputs: 1, 3, 4, 6 and total: 24
    results = generate_solutions(initial_input, initial_total)

    print("solutions: {}".format(results))
    # Format results for user readability
    # format_results(results, initial_input, 10, initial_total)

    while(True):
        cont = input("Would you like to continue testing values? (y/n) ")

        if cont == 'n':
            break
        
        # Gather user inputs for n floats
        numbers = []
        while len(numbers) < 2:
            try:
                input_vals = input(
                    "Enter the numeric values you would like to test separated"
                    "by a space: ")
                numbers = [float(s) for s in input_vals.split()]
                if len(numbers) < 2:
                    print("Please enter at least 2 values.")
            except ValueError:
                print("Please only enter numeric values.")

        # Gather user input for total
        input_total = input(
            "Enter the total you would like to compute: "
        )
        total = float(input_total)
        
        # Perform calculation for specified user inputs and total
        start = time.time()
        results = generate_solutions(numbers, total)
        stop = time.time()

        print("This iteration took {} seconds".format(stop-start))
        # Format results for user readability
        # format_results(results, numbers, 10, total)



main()