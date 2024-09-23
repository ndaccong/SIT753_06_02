"""
The main function of the application.
"""

from fastapi import FastAPI

def square(number: int = 10):
    """
    Calculates the square of a number.

    Args:
        n: The number to square.

    Returns:
        The square of n.
    """
    return number * number

app = FastAPI()

@app.get("/")
async def get_square(number: int = 10):
    """Returns the square of a number"""
    return square(number=number)

if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser("Square example")
    parser.add_argument("--number", help="Any number.", type=int)
    args = parser.parse_args()

    print(f"The square of {args.number} is: {square(args.number)}")
