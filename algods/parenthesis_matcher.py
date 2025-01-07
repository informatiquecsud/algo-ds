from ds.stack import ListStack
    
class ParenthesisMatcher:
    '''

    >>> m = ParenthesisMatcher()
    >>> m.add_match('(', ')')
    >>> m.add_match('[', ']')

    >>> m.as_dict()
    {'(': ')', '[': ']'}

    >>> m
    ParenthesisMatcher({'(': ')', '[': ']'})
    
    >>> m.match('(', ')')
    True
    >>> m.match('(', '(')
    False
    >>> m.match('(', ']')
    False
    >>> m.match('[', ']')
    True
    >>> m.match('[', ')')
    False
    >>> m.match('{', '}')
    False

    >>> m.add_match('{', '}')
    >>> m.match('{', '}')
    True
    
    '''
    ...


if __name__ == '__main__':
    import doctest
    doctest.testmod()
