from itertools import permutations

# Define the digits to be used
digits = [1, 2, 3, 4, 5, 6, 7, 8]

# Generate all permutations of 3 digits
three_digit_numbers = permutations(digits, 3)

# Convert permutations to a list of numbers
D = [int(''.join(map(str, perm))) for perm in three_digit_numbers]

# Print the result
print(D)