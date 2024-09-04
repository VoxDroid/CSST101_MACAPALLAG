import re

def evaluate(statement, values):
    """
    Evaluate a logical statement based on given truth values.

    :param statement: str, logical expression using variables.
    :param values: dict, mapping variables to their truth values.
    :return: bool, evaluated truth value of the statement.
    """
    # Replace variable names with their corresponding boolean values
    for var, val in values.items():
        # Use word boundaries to avoid partial replacements
        statement = re.sub(rf'\b{var}\b', str(val), statement)
    
    # Replace logical operators to match Python syntax
    statement = statement.replace('AND', 'and').replace('OR', 'or').replace('NOT', 'not')

    try:
        # Evaluate the final expression
        return eval(statement)
    except SyntaxError as e:
        print(f"SyntaxError: {e}")
        return None
