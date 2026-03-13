import random
from fastmcp import FastMCP

mcp = FastMCP(name='Calculator Tools')

@mcp.tool
def subtract_two_numbers(first_number: float, second_number: float):
    """Subtracts two numbers."""
    return first_number - second_number

@mcp.tool
def add_two_numbers(first_number: float, second_number: float):
    """Adds two numbers."""
    return first_number + second_number

@mcp.tool
def multiply_two_numbers(first_number: float, second_number: float):
    """Multiplies two numbers."""
    return first_number * second_number

@mcp.tool
def divide_two_numbers(first_number: float, second_number: float):
    """Divides two numbers."""
    if second_number == 0:
        return "Error: Cannot divide by zero."
    return first_number / second_number

@mcp.tool
def modulo_two_numbers(first_number: float, second_number: float):
    """Finds the modulo of two numbers."""
    if second_number == 0:
        return "Error: Cannot divide by zero."
    return first_number % second_number


if __name__ == "__main__":
    mcp.run()