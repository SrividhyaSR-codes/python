
"""Examples of Python functions with explanatory comments.
A function is like a mini program inside ur program. You give it a name, and it does something when you call it. 
Functions can take inputs (parameters) and return outputs (return values).
They help organize code, avoid repetition, and make programs easier to read and maintain.
"""

from typing import Callable, Iterable, Iterator, Any, Dict
import asyncio


# 1) Simple function with positional arguments
def add(a: float, b: float) -> float:
	# Returns the sum of two numbers
	return a + b


# 2) Function with default arguments
def greet(name: str, greeting: str = "Hello") -> str:
	# greeting has a default value; call greet('Alice') -> 'Hello, Alice!'
	return f"{greeting}, {name}!"


# 3) Function accepting a variable number of positional args (*args)
def mean(*values: float) -> float:
	# *values collects extra positional arguments into a tuple
	# Example: mean(1, 2, 3) -> 2.0
	if not values:
		raise ValueError("mean() requires at least one value")
	return sum(values) / len(values)


# 4) Function accepting keyword-only and variable keyword args (**kwargs)
def describe_person(name: str, /, age: int, **attributes: Any) -> Dict[str, Any]:
	# The slash (/) marks positional-only parameters (Python 3.8+)
	# **attributes collects extra keyword arguments into a dict
	info = {"name": name, "age": age}
	info.update(attributes)
	return info


# 5) Higher-order function: takes and returns functions
def make_multiplier(factor: float) -> Callable[[float], float]:
	# Returns a new function that multiplies its input by factor
	def multiplier(x: float) -> float:
		return x * factor
	return multiplier


# 6) Lambda (anonymous) function usage
square = lambda x: x * x  # short anonymous function for squaring


# 7) Recursive function example (factorial)
def factorial(n: int) -> int:
	# Computes n! recursively. Raises ValueError for negative input.
	if n < 0:
		raise ValueError("factorial() not defined for negative values")
	return 1 if n in (0, 1) else n * factorial(n - 1)


# 8) Generator function example
def countdown(n: int) -> Iterator[int]:
	# Yields numbers from n down to 0. Generators are memory-efficient.
	while n >= 0:
		yield n
		n -= 1


# 9) Async function example (requires asyncio to run)
async def async_wait_and_double(x: int) -> int:
	# Simulates asynchronous work using asyncio.sleep
	await asyncio.sleep(0.01)
	return x * 2


# 10) Function with type hints and docstring
def find_max(numbers: Iterable[float]) -> float:
	"""Return the maximum value in an iterable of numbers.

	Raises ValueError if the iterable is empty.
	"""
	iterator = iter(numbers)
	try:
		max_val = next(iterator)
	except StopIteration:
		raise ValueError("find_max() arg is an empty iterable")
	for v in iterator:
		if v > max_val:
			max_val = v
	return max_val


if __name__ == '__main__':
	# Example calls and printed outputs for quick testing
	print("add(2, 3):", add(2, 3))
	print("greet('Alice'):", greet('Alice'))
	print("mean(1,2,3,4):", mean(1, 2, 3, 4))
	print("describe_person('Bob', 30, city='NYC'):", describe_person('Bob', 30, city='NYC'))
	double = make_multiplier(2)
	print("double(5):", double(5))
	print("square(6):", square(6))
	print("factorial(5):", factorial(5))
	print("countdown(3):", list(countdown(3)))

	# Run the async example
	result = asyncio.run(async_wait_and_double(7))
	print("async_wait_and_double(7):", result)

	# find_max example
	print("find_max([3,1,4,2]):", find_max([3, 1, 4, 2]))
