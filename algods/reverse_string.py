from ds.stack import ListStack


def reverse_string(to_reverse: str) -> str:
    """
    Reverses the string `to_reverse` using a stack.

    >>> reverse_string('Salut tout le monde')
    >>> reverse_string('')
    ''
    >>> reverse_string('abba')
    'abba'
    """
    return to_reverse


if __name__ == "__main__":
    import doctest

    doctest.testmod()
