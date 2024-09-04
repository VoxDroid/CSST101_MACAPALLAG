def forall(predicate, domain):
    """
    Check if a predicate is true for all elements in a domain.
    
    :param predicate: function, predicate to apply on elements.
    :param domain: list, elements over which to apply the predicate.
    :return: bool, True if predicate holds for all elements.
    """
    return all(predicate(x) for x in domain)

def exists(predicate, domain):
    """
    Check if a predicate is true for at least one element in a domain.
    
    :param predicate: function, predicate to apply on elements.
    :param domain: list, elements over which to apply the predicate.
    :return: bool, True if predicate holds for at least one element.
    """
    return any(predicate(x) for x in domain)
