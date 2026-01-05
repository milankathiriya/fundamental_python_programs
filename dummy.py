# Operator: A special symbol to perform certain operations on operands.

'''
Types of Operators
------------------
1.Arithmetic Operators +, -, *, /, //, %, **
2.Comparison Operators ==, !=, <, >, <=, >=
3.Assignment Operators =, +=, -=, *=, /=, //=, %=, **=, :=
4.Logical Operators    and, or, not
5.Identity Operators   is, not is
6.Membership Operators in, not in
'''

# Type casting constructors
'''
- To convert a value from one datatype
to another datatype.

Types:
-----
a. Primitive Constructors
    1. int()
    2. float()
    3. str()
    4. bool()
    5. complex()
    
b. Collection Constructors
    6. list()
    7. tuple()
    8. set()
    9. frozenset()
    10. dict()
'''


# Operator Precedence
'''
- In a given mathematical expression,
the order of executing each operator
along with its associativity is known
as Operator Precedence.

Priority         Associativity
------------------------------
1. ()            Inner to Outer
2. **            Right to Left
3. *, /, //, %   Left to Right
4. +, -          Left to Right
5. =             Right to Left
'''

a = 12 * 6 / ((2 - 10) + 4)

print(a)
