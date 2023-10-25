"""
    Topic: Assignment 4 - Question 4
    Date: 19 Oct 2023
    Author: Kathleen
"""

number = int(input("Enter a number of three digits to check if it is an Armstrong number: "))
digits = list(map(int, str(number))) ## put each digit of the number into a list

is_armstrong = lambda x: x == sum(digit ** 3 for digit in digits) ## test if the sum of the cubes of each digit of the number x is equal to the number x


print(is_armstrong(number))