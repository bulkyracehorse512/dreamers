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

import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

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


def create_graph(values):
    iteration_nums = [x for x, _ in values]
    permutation_vals = [y for _, y in values]

    plt.plot(iteration_nums, permutation_vals)
    plt.ylabel('Permutations')
    plt.xlabel('Iterations')

    plt.savefig('graph.png')


def generate_solutions(digits, target):
    string = ""
   
    def compute(digits, target, operations):
        """ Recursively compute operations for each set of digits.
        """
        # Build the solution string on each pass of operations and digits
        nonlocal string

        head, *tail = digits
        if tail == [] or operations == []:
            # Add tail to solution string before returning
            string += "{})".format(head)
            return head
        op = operations.pop()

        # Build solution string preserving order of operations
        string += "{} ({}, ".format(op.__name__, head)
        try:
            return op(head, compute(tail, target, operations))
        except (ZeroDivisionError, TypeError) as e:
            return

    # Find all orders of all combinations of operations
    op_set = operations(len(digits) - 1)
    # Find all orders of input digits
    combos = num_perms(digits)
    # List to collect valid answers
    answers = set()

    # Iterate over all operations and digit combos
    for ops in op_set:
        for combo in combos:
            total = compute(combo, 24, list(ops))
            if total == target:
                answers.add((total, string))
            string = ""
    return answers


def format_results(results, inputs, perms, total):
    """ Create human readable outputs for each input, target combination.
    """
    inputs = ', '.join(str(i) for i in inputs)
    
    if results:
        print ("".join([
            "The following combinations for the given inputs: {} ",
            "successfully totaled to '{}': ",
        ]).format(inputs, str(total)))
        print("\n".join(map(str, results)))
        print ("There was/were {} total solution(s).".format(len(results)))

    else:
        print ("".join([
            "No combination of operations resulted in the given total {} ",
            "for inputs {}",
        ]).format(inputs, str(total)))

    print("The program exexuted {} total numeric permutations".format(perms))


def main():
    graph_perms = []
    times = []
    initial_input = (1, 3, 4, 6)
    initial_total = 24
    
    # Set up counter to track iteration number and permutations for graphing
    count = 1
    initial_perm = len(num_perms(initial_input))
    graph_perms.append((count, initial_perm))

    # Perform calculation for inputs: 1, 3, 4, 6 and total: 24
    start = time.time()
    results = generate_solutions(initial_input, initial_total)
    stop = time.time()

    # Format results for user readability
    format_results(
        results, initial_input, initial_perm, initial_total)
    duration = stop - start
    times.append(duration)
    print("This iteration took {} seconds".format(duration))

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
                        
        # Track iteration and permutations for graphing and times
        count += 1
        perms = len(num_perms(numbers))
        duration = stop - start
        times.append(duration)
        graph_perms.append((count, perms))
        
        print("This iteration took {} seconds".format(duration))
        
        # Format results for user readability
        format_results(results, numbers, perms, total)

    avg_time = sum(times) / float(len(times))
    print("The average time per iteration was: {} seconds".format(avg_time))

    create_graph(graph_perms)


main()
