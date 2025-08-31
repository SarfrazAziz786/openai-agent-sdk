from agents import function_tool


@function_tool
def plus(n1:int, n2: int)->int:
 
    """Add two integers together"""

    print("plus tool fire......>")
    return n1 + n2

@function_tool
def multiply(n1:int, n2: int)->int:
    """Multiply two integers together"""
    print("multiply tool fire......>")
    return n1 * n2

@function_tool
def Subtract(n1:int, n2: int)->int:
    """Subtract second integer from first"""

    print("Subtract tool fire......>")
    return n1 - n2


@function_tool
def weather(city:str):
    """Get the current weather for a given city."""
    print("-------weather tool fire------")
    return f"{city} : sunny"