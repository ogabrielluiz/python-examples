"""Convert a m-base Number to a n-base Number."""

import math
from main import DecimalToOctal

def ConvertToDecimal(num, old_base):
    """Convert a old_base Number to a Decimal Number."""
    result = 0
    counter = 0
    while num > 0:
        result += (num%10) * old_base**counter
        counter += 1
        num = int(num/10)

    return result

def ConvertFromDecimal(num, new_base):
    """Convert a Decimal Number to a new_base Number."""
    result = 0
    counter = 0

    while num > 0:
        result = result + (num % new_base) * 10** counter
        counter += 1
        num = int(num / new_base)  # basically /= new_base without remainder if any
    return result

def ConvertToDifferentBases(num, old_base, new_base):
    """Convert a Decimal Number to an Octal Number."""
    # TODO: Consider the case num comprises of characters
    return ConvertFromDecimal( ConvertToDecimal(num, old_base), new_base)

def main():
    """Print octal equivelents of decimal numbers."""  
    print(ConvertToDifferentBases(10, 3, 2))  # = 11
    
if __name__ == '__main__':
    main()