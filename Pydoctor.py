def multiply(a, b):
    """
    Multiply two numbers together.
    
    :param a: The first number to multiply (multiplicand)
    :type a: int or float
    :param b: The second number to multiply (multiplier)
    :type b: int or float
    :returns: The product of a and b
    :rtype: int or float
    :raises ValueError: If either a or b is not an int or float
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError('Both a and b must be ints or floats')
    return a * b



def divide(a, b):
    """
    Divide two numbers.
    
    :param a: The first number of the division (dividend)
    :type a: int or float
    :param b: The second number of the division (divisor)
    :type b: int or float
    :returns: The quotient of a and b
    :rtype: int or float
    :raises ValueError: If either a or b is not an int or float
    :raises ZeroDivisionError: If the divisor equals 0
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError('Both a and b must be ints or floats')
    return a / b


def average(numbers):
    """
    Calculate average of numbers.
    
    :param numbers: A list of numbers, whose average value we will find
    :type numbers: list
    :returns: The average value of numbers
    :rtype: int or float
    :raises ValueError: If the list consists of one or many elements that is not int or float
    :raises ValueError: If the list is empty
    """
    for num in numbers:
        if not isinstance(num, (int, float)):
            raise ValueError("All elements must be int or float")
    if not numbers:
        raise ValueError("List cannot be empty")
    return sum(numbers) / len(numbers)



if __name__ == "__main__":
    print("Testing functions:")
    print(f"multiply(5, 3) = {multiply(5, 3)}")
    print(f"divide(10, 2) = {divide(10, 2)}")
    print(f"average([1, 2, 3, 4]) = {average([1, 2, 3, 4])}")
    
    
    try:
        multiply('d', 7)
    except ValueError as e:
        print(f"multiply('d', 7) raised: {e}")

    try:
        divide(5, 0)
    except ZeroDivisionError as e:
        print(f"divide(5, 0) raised: {e}")
    
    try:
        average([])
    except ValueError as e:
        print(f"average([]) raised: {e}")

    try:
        average([1, 2, 3 , 'd'])
    except ValueError as e:
        print(f"average([1, 2, 3 , 'd']) raised: {e}")

