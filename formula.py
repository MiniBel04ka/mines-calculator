import math

def calculate_formula(mines, turn):
    # We calculate the possibilities of choosing x diamonds from the remaining (25 - b) cells
    numerator = math.comb(25 - mines, turn)  # Combinations for successful elections
    denominator = math.comb(25, turn)    # Common combinations for all selections
    
    # Return the result as a multiplier
    return (denominator / numerator) * 0.97

# Examples of use
print(f"11 mines, 3 taps = {calculate_formula(11, 3):.2f}")
print(f"11 mines, 4 taps = {calculate_formula(11, 4):.2f}")
print(f"15 mines, 3 taps = {calculate_formula(15, 3):.2f}")
print(f"15 mines, 4 taps = {calculate_formula(24, 1):.2f}")
