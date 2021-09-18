## Objective
## In this challenge, we practice calculating the interquartile range. We recommend you complete the Quartiles challenge before attempting this problem.

## Task
## The interquartile range of an array is the difference between its first (Q1) and third (Q3) quartiles (i.e.,Q3-Q1 ).

## Given an array, values, of n integers and an array,freqs , representing the respective frequencies of values's elements, construct a data set, S values, where each value[i] occurs at frequency freqs[i]. Then calculate and print S's interquartile range, rounded to a scale of 1 decimal place (i.e., 99.9 format).

## Tip: Be careful to not use integer division when averaging the middle two elements for a data set with an even number of elements, and be sure to not include the median in your upper and lower data sets.


---------------------X---------------------X---------------------X---------------------X---------------------X---------------------X---------------------X---------------------X---------------------X---------------------X---------------------X---------------------X---------------------X---------------------X---------------------X---------------------X
---------------------X---------------------X---------------------X---------------------X---------------------X---------------------X---------------------X---------------------X---------------------X---------------------X---------------------X---------------------X---------------------X---------------------X---------------------X---------------------X


def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function
    S = []
    for i in range(len(values)):
        for j in range(freqs[i]):
            S.append(values[i])
    S = sorted(S)
    mid  = math.floor(len(S)/2)
    if len(S)%2==0:
        lower = S[:mid]
        upper = S[mid:]
        lower = statistics.median(lower)
        upper = statistics.median(upper)
        diff = upper - lower
        print("{0:.1f}".format(diff))
    else:
        lower = S[:mid]
        upper = S[mid+1:]
        lower = statistics.median(lower)
        upper = statistics.median(upper)
        diff = upper - lower
        print("{0:.1f}".format(diff))
  
  
