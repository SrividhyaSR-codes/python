# error-handling.py
# This script demonstrates various error handling techniques in Python, including try, except, else, finally, and raising custom exceptions.
# EError handling is crucial for writing robust programs that can gracefully handle unexpected situations.
def divide_numbers(a, b):
    try:
        # try: run code that may raise an exception
        result = a / b
    except ZeroDivisionError as e:
        # except: handle a specific exception
        print("Error: Cannot divide by zero.")
        print(f"Exception details: {e}")
        return None
    except TypeError as e:
        # except: handle another type of exception
        print("Error: Both inputs must be numbers.")
        print(f"Exception details: {e}")
        return None
    else:
        # else: runs only if no exception occurred
        print("Division succeeded.")
        return result
    finally:
        # finally: always runs, whether there was an exception or not
        print("Cleaning up resources (if any).")

# Example function showing input validation with ValueError.
def get_int(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError as e:
            print("Invalid input. Please enter an integer.")
            print(f"Exception details: {e}")
            continue
        else:
            return value
        finally:
            print("Input attempt completed.")

if __name__ == "__main__":
    print("Example 1: divide_numbers(10, 2)")
    print(divide_numbers(10, 2))
    print()

    print("Example 2: divide_numbers(10, 0)")
    print(divide_numbers(10, 0))
    print()

    print("Example 3: divide_numbers('10', 2)")
    print(divide_numbers('10', 2))
    print()

    print("Example 4: ask user for integer and raise custom error")
    try:
        number = get_int("Enter an integer: ")
        if number < 0:
            # raise: manually raise a custom exception
            raise ValueError("Negative numbers are not allowed here.")
    except Exception as e:
        print("Caught a custom error:", e)
    else:
        print("You entered:", number)
    finally:
        print("Program finished.")
