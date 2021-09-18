## Objective
## In this challenge, we practice calculating quartiles. Check out the Tutorial tab for learning materials and an instructional video!

## Task
## Given an array, arr, of n integers, calculate the respective first quartile (Q1), second quartile (Q2), and third quartile (Q3). It is guaranteed that Q1, Q2, and Q3 are integers.


---------------------X---------------------X---------------------X---------------------X---------------------X---------------------X---------------------X---------------------X---------------------X---------------------X
---------------------X---------------------X---------------------X---------------------X---------------------X---------------------X---------------------X---------------------X---------------------X---------------------X

def quartiles(arr):
    # Write your code here
    arr = sorted(arr)
    middle = math.floor(len(arr)/2)
    if len(arr)%2 == 0:
        
        mid = math.floor(statistics.median(arr))
        low = arr[:middle]
        low = statistics.median(low)
        up = arr[middle:]
        up = statistics.median(up)
        return [int(low), mid, int(up)]
    else:
        mid = (arr[middle])
        low = arr[:middle]
        low = statistics.median(low)

        up = arr[middle+1:]
        up = statistics.median(up)
        return [int(low), mid, int(up)]
        
