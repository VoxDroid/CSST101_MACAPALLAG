# Logical AND (∧)
def and_operation(p, q):
    """
    Perform logical conjunction (AND) on two boolean values.
    
    :param p: bool, first operand.
    :param q: bool, second operand.
    :return: bool, result of p AND q.
    """
    return p and q

# Logical OR (∨)
def or_operation(p, q):
    """
    Perform logical disjunction (OR) on two boolean values.
    
    :param p: bool, first operand.
    :param q: bool, second operand.
    :return: bool, result of p OR q.
    """
    return p or q

# Logical NOT (¬)
def not_operation(p):
    """
    Perform logical negation (NOT) on a boolean value.
    
    :param p: bool, operand.
    :return: bool, result of NOT p.
    """
    return not p

# Logical IMPLIES (→)
def implies_operation(p, q):
    """
    Perform logical implication (p → q).
    
    :param p: bool, antecedent.
    :param q: bool, consequent.
    :return: bool, result of p IMPLIES q.
    """
    return not p or q
