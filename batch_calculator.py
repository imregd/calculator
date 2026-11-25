"""Complete this function for the SCCM4910 coursework.

Place this file beside your existing lab calculator.py. The runner and
file handling are supplied; write your own processing logic and tests.
"""

from calculator import add, subtract, multiply, divide


def process_calculation(operation, a_text, b_text):
    """Return (status, result, error_code) for one calculation.

    Inputs are strings. Trim whitespace and use the four imported lab functions.
    Success: ("OK", numeric_result, "").
    The error_code is empty on success because there is no error to report.
    Error: ("ERROR", "", error_code).

    Check errors in order: UNKNOWN_OPERATION, INVALID_NUMBER, DIVISION_BY_ZERO.
    See the brief for the full contract. You may add small helper functions.
    """



    trimmedOperation = operation.strip()


    if trimmedOperation != "add" and trimmedOperation != "subtract" and trimmedOperation != "divide" and trimmedOperation != "multiply":
        return ("ERROR", "", "UNKNOWN_OPERATION")

    result = 0
    

    try:
        aTrim = a_text.strip()
        bTrim = b_text.strip()

        a = float(aTrim)
        b = float(bTrim)

    except ValueError:
        return ("ERROR", "", "INVALID_NUMBER")



    
    if trimmedOperation == "add":
        
        result = add(a, b)
    elif trimmedOperation == "subtract":
        result = subtract(a, b)
    elif trimmedOperation == "multiply":
        result =  multiply(a, b)
    elif trimmedOperation == "divide":

        if b == 0:
            return ("ERROR", "", "DIVISION_BY_ZERO")
        

        result =  divide(a, b)



    return ("OK", result, "")
