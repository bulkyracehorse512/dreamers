#!/usr/bin/env
"""
Apply operations with all combinations of parentheses structures,
to preserve various orders of operations.
"""
from itertools import izip_longest


operator_to_str = {
    'add': "+",
    'truediv': "/",
    'mul': "x",
    'sub': "-",
}


def results_to_string(nums, ops, format_str):
    """
    Format operations and numbers into readable string.
    """
    # Convert operations to mathematical symbol.
    str_ops = [operator_to_str[op.__name__] for op in ops]
    str_vals = [
        val for vals in izip_longest(nums, str_ops) for val in vals if val]
    return format_str.format(*str_vals)


def pemdas_1(nums, ops, total):
    """
    Compute operations with parentheses ordered as:
    (((a op_1 b) op_2 c) op_3 d)
    """
    num_1, num_2, num_3, num_4 = nums
    op_1, op_2, op_3 = ops

    try:
        result_1 = op_1(num_1, num_2)
        result_2 = op_2(result_1, num_3)
        result_3 = op_3(result_2, num_4)
    except ZeroDivisionError:
        return

    if result_3 == total:
        return results_to_string(nums, ops, '(({} {} {}) {} {}) {} {}')


def pemdas_2(nums, ops, total):
    """
    Compute operations with parentheses ordered as:
    (a op_1 b) op_2 (c op_3 d)
    """
    num_1, num_2, num_3, num_4 = nums
    op_1, op_2, op_3 = ops

    try:
        result_1 = op_1(num_1, num_2)
        result_2 = op_3(num_3, num_4)
        result_3 = op_2(result_1, result_2)
    except ZeroDivisionError:
        return

    if result_3 == total:
        return results_to_string(nums, ops, '({} {} {}) {} ({} {} {})')


def pemdas_3(nums, ops, total):
    """
    Compute operations with parentheses ordered as:
    a op_1 (b op_2 (c op_3 d))
    """
    num_1, num_2, num_3, num_4 = nums
    op_1, op_2, op_3 = ops

    try:
        result_1 = op_3(num_3, num_4)
        result_2 = op_2(num_2, result_1)
        result_3 = op_1(num_1, result_2)
    except ZeroDivisionError:
        return

    if result_3 == total:
        return results_to_string(nums, ops, '{} {} ({} {} ({} {} {}))')


def pemdas_4(nums, ops, total):
    """
    Compute operations with parentheses ordered as:
    (a op_1 (b op_2 c)) op_3 d
    """
    num_1, num_2, num_3, num_4 = nums
    op_1, op_2, op_3 = ops

    try:
        result_1 = op_2(num_2, num_3)
        result_2 = op_1(num_1, result_1)
        result_3 = op_3(result_2, num_4)
    except ZeroDivisionError:
        return

    if result_3 == total:
        return results_to_string(nums, ops, '{} {} ({} {} {})) {} {})')


def pemdas_5(nums, ops, total):
    """
    Compute operations with parentheses ordered as:
    a op_1 (b op_2 c)) op_3 d))
    """
    num_1, num_2, num_3, num_4 = nums
    op_1, op_2, op_3 = ops

    try:
        result_1 = op_2(num_2, num_3)
        result_2 = op_3(result_1, num_4)
        result_3 = op_1(num_1, result_2)
    except ZeroDivisionError:
        return

    if result_3 == total:
        return results_to_string(nums, ops, '{} {} (({} {} {}) {} {}))')
