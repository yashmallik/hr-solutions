# Objective
# In the previous challenge, we calculated a mean. In this challenge, we practice calculating a weighted mean. Check out the Tutorial tab for learning materials and an instructional video!

# Task
# Given an array, X, of N integers and an array, W, representing the respective weights of X's elements, calculate and print the weighted mean of X's elements. Your answer should be rounded to a scale of 1 decimal place (i.e., 12.2 format

# Function Description
# Complete the weightedMean function in the editor below.

# weightedMean has the following parameters:
# - int X[N]: an array of values
# - int W[N]: an array of weights

# Prints
# - float: the weighted mean to one decimal place

--------------------------X-----------------------X--------------------------X-----------------------X--------------------------X-----------------------X--------------------------X-----------------------X--------------------------X-----------------------X--------------------------X-----------------------X
--------------------------X-----------------------X--------------------------X-----------------------X--------------------------X-----------------------X--------------------------X-----------------------X--------------------------X-----------------------X--------------------------X-----------------------X

def weightedMean(X, W):
    # Write your code here
    arr = []
    for i in range(len(X)):
     weight = X[i]*W[i] 
     arr.append(weight) 
    wMean = sum(arr)/sum(W) 
    print("{0:.1f}".format(wMean))
