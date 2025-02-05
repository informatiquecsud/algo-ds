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

    def __init__(self, matches: dict[str, str] = None) -> None:
        self._matches = matches or {}

    def add_match(self, opening: str, closing: str) -> None:
        self._matches[opening] = closing

    def match(self, opening, closing):
        if opening in self._matches:
            return self._matches[opening] == closing
        else:
            return False

    def as_dict(self) -> dict[str, str]:
        return self._matches

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self._matches})'

if __name__ == '__main__':
    import doctest
    doctest.testmod()
