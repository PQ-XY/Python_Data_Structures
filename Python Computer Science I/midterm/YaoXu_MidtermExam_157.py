########################################
#
# CSC 157-8C1 Python Computer Science I
# Dept. of CS - OAKTON COLLEGE
# 
# Summer 2025 - MIDTERM
# Chapter 5: Programming  Exercise 17. Prime Number List
# 
# Date: [7/1/2025]   <=========
#
# Author: [Yao Xu] <======== IMPORTANT
#
########################################

# Must use the following starter code
# main function
def main():
    # local variable
    totalNumbers = 100
    print('number', '\t', 'is prime')
    print('------------------------')

    # For each number,
    # IF number is prime: print (number, '\t', 'prime')
    # ELSE: print (number, '\t', 'not prime')

    for i in range(1, totalNumbers + 1):
        if is_prime(i):
            print(i, '\t', 'prime')
        else:
            print(i, '\t', 'not prime')

# define the is_prime function 
# it receives a number as a parameter,
# and returns True if number is prime, False otherwise. 
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

# Call the main function.
main()

