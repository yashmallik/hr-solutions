# Objective
# In this challenge, we practice calculating standard deviation. Check out the Tutorial tab for learning materials and an instructional video!

# Task
# Given an array, arr, of n integers, calculate and print the standard deviation. Your answer should be in decimal form, rounded to a scale of 1 decimal place (i.e.,10.2 format). An error margin of +-1 will be tolerated for the standard deviation.

----------------X----------------X----------------X----------------X----------------X----------------X----------------X----------------X----------------X----------------X----------------X----------------X----------------X----------------X----------------X----------------X
----------------X----------------X----------------X----------------X----------------X----------------X----------------X----------------X----------------X----------------X----------------X----------------X----------------X----------------X----------------X----------------X

def stdDev(arr):
    # Print your answers to 1 decimal place within this function
    mue = statistics.mean(arr)
    total =0
    for i in arr:
        total += (i-mue)**2
    alpha = math.sqrt(total/len(arr))
    print("{0:.1f}".format(alpha))
    
    
    
