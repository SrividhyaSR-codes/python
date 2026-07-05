
import sys

from new_directory.package import add_numbers
print("Sum of 5 and 3:", add_numbers(5, 3))

def sum_values(a, b):
	"""Return sum of two numbers."""
	return a + b


def main():
	# Try to read two numbers from command-line arguments, else from input
	if len(sys.argv) >= 3:
		try:
			a = float(sys.argv[1])
			b = float(sys.argv[2])
		except ValueError:
			print('Invalid numbers')
			return
	else:
		try:
			parts = input('Enter two numbers separated by space: ').strip().split()
			a = float(parts[0])
			b = float(parts[1])
		except Exception:
			print('Invalid input')
			return

	result = sum_values(a, b)
	# Print as integer if both inputs were integers
	if a.is_integer() and b.is_integer():
		print(int(result))
	else:
		print(result)


if __name__ == '__main__':
	main()
