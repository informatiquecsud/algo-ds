from parenthesis_matcher import ParenthesisMatcher

def check_balanced(text: str) -> bool:
    '''
    >>> check_balanced("abc")
    True
    >>> check_balanced("(abc)")
    True
    >>> check_balanced("ab[cd]ef")
    True
    >>> check_balanced("a[b]c(d)e")
    True
    >>> check_balanced("a((b)c)d")
    True
    >>> check_balanced("a(b[c()e]f)g")
    True
    
    >>> check_balanced("(")
    False
    >>> check_balanced("abc)")
    False
    >>> check_balanced("ab)c")
    False
    >>> check_balanced("a(b]c")
    False
    >>> check_balanced("a(b(c)d")
    False
    >>> check_balanced("a(b[c)d]e")
    False
    '''
    return True

if __name__ == '__main__':
    import doctest
    doctest.testmod()
