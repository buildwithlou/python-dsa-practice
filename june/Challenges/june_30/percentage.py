import doctest


def calculate_percentage(total: float, percent: float) -> float:
    """
    Calculates the specific percentage amount of a given total.
    rounded to two decimal places.
    Examples:
    >>> calculate_percentage(100.0, 15.0)
    15.0

    >>> calculate_percentage(50.0, 7.5)
    3.75

    >>> calculate_percentage(80.0, 0.0)
    0.0
    """
    amount = (total * percent) / 100.0
    return round(amount, 2)


if __name__ == "__main__":
    doctest.testmod()
