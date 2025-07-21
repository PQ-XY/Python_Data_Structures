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

    #Initialize min and max
    if firstTime and line_nums:
        min = line_nums[0]
        max = line_nums[0]
        firstTime = False

    for i in line_nums:
        total += i
        count += 1

        #update min and max
        if i < min:
            min = i
        if i > max:
            max = i

    #Calculate average with valid count value
    if count > 0:
        average = total / count
    else:
        average = 0

inFile.close()

# Display the: 
print("Total: ", total)
print("Average: ", average)
print("Minimum: ", min)
print("Maximum: ", max)

print("\nDone")


