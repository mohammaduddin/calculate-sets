# Problem: 01
# Advanced-Data Structures and Comparison
# Write a Python program that takes two sets from the user and computes their union, intersection, and difference.
# A = {1, 2, 3, 4, 5}
# B = {4, 5, 6, 7, 8}


def get_set_from_input(prompt):

    # Example:
    # setA = {1, 2, 3, 4, 5}
    # setBB = {4, 5, 6, 7, 8}

    while True:
        try:
            input_str = input(prompt)
            elements = input_str.split()
            input_set = set(elements)
            return input_set
        except ValueError:
            print("Invalid input. Please enter space-separated values.")

setA = get_set_from_input("Type 1st set, separated by commas: example  1,2,3,4,5:   ")
setB = get_set_from_input("Type 2nd set, separated by commas: example  4,5,6,7,8:   ")


def set_operations(setA, setB):

    return{
         "union": setA | setB,
         "intersection": setA & setB,
         "difference_setA_minus_setB": setA | setB,
         "difference_setB_minus_setA": setB | setB
    }   


# Calling fuction by passing sets value
results = set_operations(setA, setB)

print("\n")
print(f"Set A: {setA}")
print(f"Set B: {setB}")
print("\n")
print(f"Union: {results['union']}")
print(f"Intersection: {results['intersection']}")
print(f"Difference (SetA - SetB): {results['difference_setA_minus_setB']}")
print(f"Difference (SetB - SetA): {results['difference_setB_minus_setA']}")
print("\n")


#OUTPUT:
# Type 1st set, separated by commas: example  1,2,3,4,5:   1,2,3,4,5
# Type 2nd set, separated by commas: example  4,5,6,7,8:   4,5,6,7,8

# Set A: {'1,2,3,4,5'}
# Set B: {'4,5,6,7,8'}

# Union: {'1,2,3,4,5', '4,5,6,7,8'}
# Intersection: set()
# Difference (SetA - SetB): {'1,2,3,4,5', '4,5,6,7,8'}
# Difference (SetB - SetA): {'4,5,6,7,8'}