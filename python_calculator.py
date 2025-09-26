# Function to add two numbers
def add_numbers(a, b):
    return a + b

# Function to subtract two numbers  # Added by Manideep
def subtract_numbers(a, b):
    result = a - b
    return result
    
# Function to divide two numbers
def divide_numbers(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b

# Test the function
if __name__ == "__main__":
    
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    print("Sum:", add_numbers(a, b))
    print("Difference",subtract_numbers(a,b))
    print("Division result:", divide_numbers(a, b))
