"""
    Topic: Assignment 4 - Question 2
    Date: 19 Oct 2023
    Author: Kathleen
"""

l = [1, 2, 3, 4, 5]

# using single line: list comprehension
m1 = [x for x in l if x < 0] ## Iterating the list, it will return a list with all the values that is less than 0, in this case, [] 
print(m1)