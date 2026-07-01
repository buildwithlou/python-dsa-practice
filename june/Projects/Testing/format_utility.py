def format_currency(amount: float) -> str:
    """
    Formats a numeric float into a clean USD currency string.

    Example:
    >>> format_currency(1250.5)
    '$1.250.50'
    >>> format_currency(0.99)
    '$0.99'
    >>> format_currency(-50)
    '$-50.00'
    """
    if amount < 0:
        return f"-${abs(amount):,.2f}"
    return f"${amount:,.2f}"


if __name__ == "__main__":
    import doctest

    doctest.testmod()
