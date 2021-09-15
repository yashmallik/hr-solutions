Given integers a and b, find the smallest integer h, such that there exists a triangle of height h, base b, having an area of at least a.
Function Description

Complete the lowestTriangle function in the editor below.


lowestTriangle has the following parameters:

int b: the base of the triangle
int a: the minimum area of the triangle

------------------------------x---------------------------------------------------x------------------------------------------------------x----------------------------------------x--

def lowestTriangle(trianglebase, area):
    # Write your code here
    return math.ceil(2*(area/trianglebase))
