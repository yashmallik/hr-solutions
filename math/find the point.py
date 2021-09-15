# Consider two points,  and . We consider the inversion or point reflection, , of point  across point  to be a  rotation of point  around .

# Given  sets of points  and , find  for each pair of points and print two space-separated integers denoting the respective values of  and  on a new line.

# Function Description

# Complete the findPoint function in the editor below.

# findPoint has the following parameters:

# int px, py, qx, qy: x and y coordinates for points  and 
  
---------------------------------x-----------------------------------------x-------------------------------x-------------------------------------------x-----------------------------

def findPoint(px, py, qx, qy):
    # Write your code here
    rx = 2*qx-px
    ry = 2*qy-py
    return rx,ry
    
