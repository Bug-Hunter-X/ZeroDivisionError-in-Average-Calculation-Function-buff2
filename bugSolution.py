def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case gracefully
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage demonstrating the fix
my_list = []
average = calculate_average(my_list)
print(f"The average is: {average}")  # Output: The average is: 0

my_list = [10, 20, 30, 40, 50]
average = calculate_average(my_list)
print(f"The average is: {average}") # Output: The average is: 30.0