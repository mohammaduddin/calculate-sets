# Problem: 01
# Advanced-Data Structures and Comparison
# Write a Python program that takes two sets from the user and computes their union, intersection, and difference.
# A = {1, 2, 3, 4, 5}
# B = {4, 5, 6, 7, 8}

# compute the sets of union, intersection and difference
def set_operations(setA, setB):

    return{
         "union": setA | setB,
         "intersection": setA & setB,
         "difference_setA_minus_setB": setA - setB,
         "difference_setB_minus_setA": setB - setA
    }   


user_input_string_set_a = input("Type 1st set, separated by commas: example(1,2,3,4,5):  ")
user_input_string_set_b = input("Type 2nd set, separated by commas: example(4,5,6,7,8):  ")

setA =set(user_input_string_set_a.split(','))
setB =set(user_input_string_set_b.split(','))



# Calling fuction by passing sets value
results = set_operations(setA, setB)

print(f"Set A: {setA}")
print(f"Set B: {setB}")
print(f"Union: {results['union']}")
print(f"Intersection: {results['intersection']}")
print(f"Difference (SetA - SetB): {results['difference_setA_minus_setB']}")
print(f"Difference (SetB - SetA): {results['difference_setB_minus_setA']}")




#OUTPUT:
# Type 1st set, separated by commas: example(1,2,3,4,5):  1,2,3,4,5
# Type 2nd set, separated by commas: example(4,5,6,7,8):  4,5,6,7,8
# Set A: {'5', '2', '3', '1', '4'}
# Set B: {'8', '7', '5', '6', '4'}
# Union: {'8', '7', '4', '5', '2', '6', '1', '3'}
# Intersection: {'4', '5'}
# Difference (SetA - SetB): {'1', '2', '3'}
# Difference (SetB - SetA): {'8', '6', '7'}