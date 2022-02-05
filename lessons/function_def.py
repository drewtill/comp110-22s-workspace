"""An example function definition."""


def my_max(a: int, b: int) -> int:
    """Returns the largest argument."""
    if a >= b:
        return a
    else:
        return b


x: int = 6
y: int = 5 + 2
z: int = my_max(x, y)
print(z)


# code from part 1. commented out
# print(my_max(10 + 1, 10))
# result: int = my_max(-50, 100)
# print(result)