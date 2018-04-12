#!/usr/bin/env
# Pemdas Challenge
# Time Estimate: 2 hours (9:30am EST)

# Using digits 1, 3, 4, 6 and any operation, reach a total of 24
import sys
sys.path.append('/Users/amandaboltax/Code/dreamers')

from itertools import (
    chain,
    combinations_with_replacement,
    permutations,
)
import operator

from .pemdas import (
    pemdas_1,
    pemdas_2,
    pemdas_3,
    pemdas_4,
    pemdas_5,
)


def operations():
    """
    Orders math operations in all possible permutations and all possible
    combinations. Operations may be performed in any order, any number of
    times.
    """
    ops = [operator.add, operator.sub, operator.truediv, operator.mul]
   
    # List all combinations of operators
    combinations = list(combinations_with_replacement(ops, 3))

    # For each combination list all possible orders of operations
    perms = []
    for combo in combinations:
        perms.append(list(permutations(combo)))

    # Return flattened permutations
    return list(chain(*perms))


def num_perms(inputs):
    """
    Orders integers in all permutations.  Digits must be used once and only
    once, in any order.
    """
    return list(permutations(inputs))


def perform_calculations(inputs, total):
    """ Apply combinations of operations to permutations of digits.  Collect
    and store tuples of successful integer-order operation-order pairs.
    """
    numbers = num_perms(inputs)
    num_ops = operations()
    paren_ops = [pemdas_1, pemdas_2, pemdas_3, pemdas_4, pemdas_5]

    success_totals = set()

    for nums in iter(numbers):
        for ops in num_ops:
            for pemdas in paren_ops:
                ret_val = pemdas(nums, ops, total)

                if ret_val:
                    success_totals.add(ret_val) 

    return success_totals


def format_results(results, inputs, total):
    """
    """
    if not results:
        print "No combination of operations resulted in the given total."

    inputs = ', '.join(str(i) for i in inputs)

    print "".join([
        "The following combinations for the given inputs: {} successfully",
        "computed the given total: {} ---"
    ]).format(inputs, str(total))
    print "\n".join(results)


def main():
    initial_input = (1, 3, 4, 6)
    initial_total = 24
    
    # Perform calculation for inputs: 1, 3, 4, 6 and total: 24
    results = perform_calculations(initial_input, initial_total)

    # Format results for user readability
    format_results(results, initial_input, initial_total)
