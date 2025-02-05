from stack import EmptyStackError
from list_stack import ListStack
from parenthesis_matcher import ParenthesisMatcher

Stack = ListStack

def check_balanced(text: str) -> str:
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
        
    m = ParenthesisMatcher()
    m.add_match('(', ')')
    m.add_match('[', ']')
    m.add_match('{', '}')
            
    p_stack = Stack()
    
    for c in text:
        if m.is_opening_paren(c):
            p_stack.push(c)
        elif m.is_closing_paren(c):
            try:
                top = p_stack.peek()
                if m.match(top, c):
                    p_stack.pop()
                else:
                    return False
            except EmptyStackError as e:
                return False
        else:
            pass
        
    if p_stack.is_empty():
        return True
    else:
        return False


if __name__ == '__main__':
    import doctest
    doctest.testmod()
