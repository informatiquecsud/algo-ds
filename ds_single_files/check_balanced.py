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
    
    def build_dictionaries(parentheses):
        opening_paren = {}
        closing_paren = {}
        
        for pair in parentheses:
            opening, closing = list(pair)
            opening_paren[opening] = closing
            closing_paren[closing] = opening
            
        return opening_paren, closing_paren
        
    opening_p, closing_p = build_dictionaries(['()', '{}', '[]'])
    
    p_stack = Stack()
    
    for c in text:
        if c in opening_p:
            p_stack.push(c)
        elif c in closing_p:
            opening = closing_p[c]
            
            try:
                if p_stack.peek() == opening:
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
