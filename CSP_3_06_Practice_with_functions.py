#Herons Formula
import math

#returns the square root of the number n
def root(n):
    return math.sqrt(n)

#Takes in the 3 side lengths of a triangle as arguments and returns half of
#the perimeter of a triangle.
def semiPerimeter(s1, s2, s3):
    return (s1+s2+s3)/2


#Modify the below function such that it takes in 4 arguments. multiply the first
#argument by the difference between itself and each individual argument. Reference herons formula for more context.
import math
def multiplyDifferences(s, a, b, c):
        return math.sqrt(s * (s - a) * (s - b) * (s - c))
multiplyDifferences(3, 2, 2, 2)

#Given the 3 sides of a triangle return the area.
#use herons formula
#Use the functions above.
import math
def herons(a, b, c):
    s = (a + b + c)/2
    #s = semiPerimeter(a,b,c)
    s_less_a = s - a
    s_less_b = s - b
    s_less_c = s - c
    return math.sqrt(s*s_less_a*s_less_b*s_less_c)
    #return( root(multiplyDifferences(s,a,b,c))


#quadratic equation
#takes in a number as an argument and returns that number multiplied by 2.
def denominator(a):
    return (a*2)

#Takes in two arguments. multiply the first argument by negative 1. Then
#return the modified first argument added and subtracted by the second argument.
def plusMinus(a, b):
    neg_a = a*-1
    return (neg_a + b, neg_a - b)

#takes in three numbers as arguments. The first and third multiplied together then
#multiplied by 4.Then subtract that result from the second argument squared.
#Return the overall result.
def mainCalc(a, b, c):
    number = (b**2) - (a * c * 4)
    return number

#The below function should take the inputs of the quadratic equation and return the result
#Make sure to use all the formulas from this section.
def quadratic(a, b, c):
    d = b**2 - 4*a*c
    if d < 0:
        return "No roots"
    root1 = (-b + math.sqrt(d)) / (2 * a)
    root2 = (-b - math.sqrt(d)) / (2 * a)
    return root1, root2
