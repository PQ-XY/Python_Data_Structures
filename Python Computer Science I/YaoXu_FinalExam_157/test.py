########################################
#
# Final Exam:
# Type the code to solve this exam as specified
#
# CSC 157
# Dept. of CS - OAKTON COLLEGE
#
# Author: [Yao Xu]
#
########################################

# Must use the following variables :
# total - for the sum of all the ints
# average - for the average of all the ints

# min - for the minimum of all the ints
# max - for the maximum of all the ints
firstTime = True
# min & max must be initialized in the loop

#Initialize total, count, average variables
total = 0
count = 0
average = 0.0

fileName = "numbers.txt"
numbers = []

# Open the numbers.txt file
inFile = open('numbers.txt', mode="r")

# In the following for-loop read the ints in the numbers.txt file and
# compute  their total, average, min, and max
for line in inFile:
    #
    # Find min, max, average, total in this loop
    # Remember: min & max must be initialized in the loop
    #
    line_nums = list(map(int, line.split()))
    numbers.extend(line_nums)

numbers.sort()
min = numbers[0]
max = numbers[-1]
total = sum(numbers)
average = total / len(numbers)

inFile.close()

# Display the:
print("Total numbers of integers: ", len(numbers))
print("Total: ", total)
print("Average: ", average)
print("Minimum: ", min)
print("Maximum: ", max)

print("\nDone")