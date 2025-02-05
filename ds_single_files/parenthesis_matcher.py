from typing import Any

class ParenthesisMatcher:
    '''

    >>> m = ParenthesisMatcher()
    >>> m.add_match('(', ')')
    >>> m.add_match('[', ']')

    >>> m.as_dict()
    {'(': ')', '[': ']'}

    >>> m
    ParenthesisMatcher({'(': ')', '[': ']'})
    >>> m = ParenthesisMatcher({'(': ')', '[': ']'})
    >>> m
    ParenthesisMatcher({'(': ')', '[': ']'})
    
    >>> m.is_opening_paren('(')
    True
    >>> m.is_opening_paren(')')
    False
    >>> m.is_opening_paren('{')
    False
    
    >>> m.is_closing_paren(')')
    True
    >>> m.is_closing_paren('(')
    False
    >>> m.is_closing_paren('}')
    False
        
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
        self._reverse_matches = ParenthesisMatcher.reverse_dict(self._matches)
        
    @staticmethod
    def reverse_dict(d: dict[Any, Any]) -> dict[Any, Any]:
        result = {}
        for k, v in d.items():
            if v in result:
                raise ValueError(f"dict {d} must be reversible")
            result[v] = k
        return result
        

    def add_match(self, opening: str, closing: str) -> None:
        self._matches[opening] = closing
        self._reverse_matches[closing] = opening

    def match(self, opening, closing):
        if opening in self._matches:
            return self._matches[opening] == closing
        else:
            return False
        
    def is_opening_paren(self, c: str) -> bool:
        return c in self._matches
    
    def is_closing_paren(self, c: str) -> bool:
        return c in self._reverse_matches

    def as_dict(self) -> dict[str, str]:
        return self._matches

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self._matches})'

if __name__ == '__main__':
    import doctest
    doctest.testmod()
