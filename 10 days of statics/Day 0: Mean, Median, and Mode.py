# Objective
# In this challenge, we practice calculating the mean, median, and mode. Check out the Tutorial tab for learning materials and an instructional video!

# Task
# Given an array, X, of N integers, calculate and print the respective mean, median, and mode on separate lines. If your array contains more than one modal value, choose the numerically smallest one.

# Note: Other than the modal value (which will always be an integer), your answers should be in decimal form, rounded to a scale of 1 decimal place (i.e., 12.3, 7.0 format).

----------------------X----------------------X----------------------X----------------------X----------------------X----------------------X----------------------X----------------------X----------------------X
----------------------X----------------------X----------------------X----------------------X----------------------X----------------------X----------------------X----------------------X----------------------X

# Enter your code here. Read input from STDIN. Print output to STDOUT
import math 
n = int(input())
arr = input().rstrip().lstrip()
arr = arr.split(' ')
for x in range(len(arr)):
    arr[x] = int(arr[x])

    
    


def mthree(arr):
    num = len(arr)
    mid = math.floor(num/2)
    count = 0
    mean = sum(arr)/num
    print ("{0:.1f}".format(mean))
    
    arr = sorted(arr)
    if num % 2 != 0:
        print(arr[mid])
    else:
        median = ((arr[mid]+arr[mid-1])/2)
        print("{0:.1f}" .format(median))
        
        mode = []
    for x in range(len(arr)):
        for y in range(len(arr)):
            if arr[x]==arr[y]:
                count += 1
        mode.append(count)
        count = 0
    if max(mode)==1:
        print(min(arr))
    else:
        print(arr[mode.index(max(mode))])
    
mthree(arr)
