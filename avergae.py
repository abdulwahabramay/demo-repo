# Function to calculate average
def calculate_average(marks):
    if len(marks) == 0:
        return 0  # Avoid division by zero
    return sum(marks) / len(marks)

# Example usage
marks = [85, 90, 78, 92, 88]  # List of marks
average = calculate_average(marks)
print("The average of the marks is:", average)