# Initialize an empty list to store numbers
numbers = []

print("Enter a list of numbers, type 0 when finished.")

# Loop to collect numbers from the user
while True:
    try:
        num = int(input("Enter number: "))  # Convert input to an integer
        if num == 0:  # Stop when the user enters 0
            break
        numbers.append(num)  # Add the number to the list
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Check if the list is empty
if len(numbers) == 0:
    print("No numbers were entered.")
else:
    # Calculate the sum of the numbers
    total = sum(numbers)
    
    # Calculate the average (sum divided by the number of elements)
    average = total / len(numbers)
    
    # Find the largest number
    largest = max(numbers)

    # Display the main results
    print(f"\nThe sum is: {total}")
    print(f"The average is: {average}")
    print(f"The largest number is: {largest}")

    # Extra challenge: Find the smallest positive number
    positive_numbers = [num for num in numbers if num > 0]
    if positive_numbers:  # If there are positive numbers
        smallest_positive = min(positive_numbers)
        print(f"The smallest positive number is: {smallest_positive}")

    # Extra challenge: Sort and display the list
    sorted_numbers = sorted(numbers)
    print("\nThe sorted list is:")
    for num in sorted_numbers:
        print(num)

# Prevent the program from closing immediately
input("\nPress Enter to exit...")
