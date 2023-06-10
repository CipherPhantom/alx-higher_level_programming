#!/usr/bin/python3
def check_tuple(tuple_1):
    if len(tuple_1) == 0:
        return (0, 0)
    elif len(tuple_1) == 1:
        return (tuple_1[0], 0)
    else:
        return tuple_1


def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = check_tuple(tuple_a)
    tuple_b = check_tuple(tuple_b)
    one = tuple_a[0] + tuple_b[0]
    two = tuple_a[1] + tuple_b[1]
    return (one, two)
