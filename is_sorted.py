def is_sorted(numbers):
    """
    Determine if list is sorted.

    A function that determines if an input list of integers is sorted in non-decreasing order.
    :param numbers: a list of integers
    :precondition: numbers must be a list of integers
    :postcondition: correctly verifies if numbers is sorted in non-decreasing order or not
    :return: True if numbers is sorted else false

    >>> is_sorted([1, 2, 3])
    True
    >>> is_sorted([3, 2, 1])
    False
    """
    sorted_numbers = sorted(numbers)
    if len(numbers) == 0:
        return False
    elif numbers == sorted_numbers:
        return True
    else:
        return False

print(is_sorted([]))
print(len([]))
