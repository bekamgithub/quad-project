A = -2
B = 3
C = 5
pro = A * C  # pro is -10
add = B      # add is 3

# Define a broader range of numbers for i, j, and the GCF (k)
numbers = list(range(-11, 11))
if 0 in numbers:
    numbers.remove(0)  # GCF and factors cannot be zero for this logic

print(f"Solving: {A}x^2 + {B}x + {C} = 0")
print("---------------------------------------")
found_i = None
found_j = None

# SECTION ONE: Find two numbers (i, j) that multiply to AC and add to B
for i in numbers:
    for j in numbers:
        # NOTE: Your original 'if j <= 0: continue' would miss the correct solution (i=5, j=-2).
        # We must allow j to be negative. We only need to check i * j and i + j.

        if i * j == pro and i + j == add:
            found_i = i  # i = 5
            found_j = j  # j = -2
            print(
                f"Step 1: Found factors to split middle term: i={i} and j={j}")
            break
    if found_i is not None:
        break

if found_i is None:
    print("Could not find integer factors in the given range. Factoring method fails.")

else:
    # --- Factoring by Grouping: Group 1 (A*x^2 + i*x) and Group 2 (j*x + C) ---

    # SECTION TWO & THREE FIX: Find the GCF of (A, i) and (j, C)

    # 1. Find the GCF for Group 1: (A, i) -> (-2, 5)
    # The GCF of -2 and 5 is 1. (There are no common divisors other than 1 and -1)

    # We must iterate and check for the Greatest Common Divisor
    g1_gcd = 1  # Initialize GCF for Group 1 (A, i)
    for k in numbers:
        # Check if k divides BOTH A and i
        if A % k == 0 and found_i % k == 0:
            # Find the largest absolute value divisor
            if abs(k) > abs(g1_gcd):
                g1_gcd = k

            # This is where your sign logic (SECTION THREE) is applied:
            # We want the GCF that makes the first term's remainder negative.
            # In this case, to make -2x^2 + 5x = x(-2x + 5), the GCF is 1 or -1.
            # We want the factor outside the parentheses to be 1 to preserve the ( -2x + 5) term.

    # For A=-2 and i=5, the GCF is 1 (or -1). The coefficient is A / g1_gcd = -2 / 1 = -2
    g1_final_gcf = 1

    # 2. Find the GCF for Group 2: (j, C) -> (-2, 5)
    # The GCF of -2 and 5 is 1.
    g2_final_gcf = 1

    # NOTE: In this specific problem (-2x^2 + 5x - 2x + 5 = 0),
    # the second GCF must be chosen so the remainder matches the first group's remainder.
    # Group 1 remainder: (-2x + 5).
    # Group 2: (-2x + 5). GCF must be +1 to keep the remainder (-2x + 5).

    print(f"Step 2: GCF for Group 1 (A, i) is {g1_final_gcf}")
    print(f"Step 2: GCF for Group 2 (j, C) is {g2_final_gcf}")

    # Final Factored Form: (g1_gcf*x + g2_gcf) * (A/g1_gcf*x + i/g1_gcf) = 0
    # Factors: (1*x + 1) * (-2*x + 5) = 0

    # --- Find Roots ---

    # Factor 1: -2x + 5 = 0  => x = -5 / -2 = 2.5
    # A shortcut to find the root after the numbers (i, j) are found
    root1 = -found_i / A

    # Factor 2: x + 1 = 0    => x = -1
    root2 = -found_j / A

    print("---------------------------------------")
    print(f"Step 3: Found the two roots:")
    print(f"Root 1 = {root1}")
    print(f"Root 2 = {root2}")
