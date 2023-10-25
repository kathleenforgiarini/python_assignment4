"""
    Topic: Assignment 4 - Question 1
    Date: 21 Oct 2023
    Author: Kathleen

QUESTION A
    The output for this question is [0,1,2,3,4,5,6,7,8,9] because we are printing the list of numbers. 
    We can modify and add the odd numbers in the list called 'n':
     for i in numbers:
        if odd(i):
            n.append(i)
            continue
        else: 
            break
    It will return an empty list, because the first number i is 0, that is even, so it goes to the else condition and breaks the loop, leaving an empty list.

    
QUESTION B

    The output for this question is an exception, because we are removing items (if the number of index i is odd) from the list during iteration, which changes the 
    length of the list. To solve this problem, we can remove the del and create another list to save the numbers that are not odd.
    The output of the new list will be: [0,2,4], removing 1 and 3

    
QUESTION C
    The output for this question is False True. It is testing with lambda if the number is odd and returns a boolean. 20 is even and 21 is odd.

    
QUESTION D
    The output for this question is 24. It is using reduce from functools to get one final number, and lambda to multiply the numbers 
    from the list l. It multiplies 1 and 2, then the result multiplies 3, and the result multiplies 4.

    
QUESTION E
    The output for this question is [1, -2, -3], that are less than 2. It is using filter to filter numbers using the function f1, which will return false if the number
    is greater than 2, and return true if the number is less than 2. The filter will take the numbers that the function returned true,
    and converting it to a list to display, instead of display the address of the object

    
QUESTION F
    The output for this question is [False, True, True, False, False]. It is similar to the previous question, the only thing is the map, it will return the result
    of the function for each number of list l, instead of returning the number like filter. So it will test each number of the list it they are less than -1 and return
    the boolean for each value. And converting to list to display it.

    
QUESTION G
    The output for this question is 5, it is using reduce function to return just one value, and using the lambda to compare 2 variables and return the largest one.
    So with the reduce, we are passing each element from list l to lambda to compare one with the other, from left to right, to return the largest value.

    
QUESTION H
    The code provided was missing the import functools to use the reduce, and the syntax of reduce is incorrect, reduce needs to have a function with two arguments, 
    and pass an iterable object as second argument for reduce. After running the code, I realized that the lambda function is incorrect too, because the in range also 
    needs to have two arguments. So it will return an exception.

"""