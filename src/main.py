"""
The main function of the application.
"""

def square(n):
    """
    Calculates the square of a number.

    Args:
        n: The number to square.

    Returns:
        The square of n.
    """
    return n * n

if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser("Square example")
    parser.add_argument("-n", help="Any number.", type=int)
    args = parser.parse_args()

    print(f"The square of {args.n} is: {square(args.n)}")
