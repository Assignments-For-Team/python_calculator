# Function to add two numbers
def add_numbers(a, b):
    return a + b

# Test the function
if __name__ == "__main__":
    print("Sum:", add_numbers(10, 12))
    
# Function to divide two numbers
def divide_numbers(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b

# Test the function
if __name__ == "__main__":
    print("Division result:", divide_numbers(10, 2))
    print("Division by zero attempt:", divide_numbers(10, 0))
