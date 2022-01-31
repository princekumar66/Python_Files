'''Compute Sin hyperbolic function
Sinh(x) = (exp(x) -exp(-x))/2
Verify the result with python's built-in, sinh function(math module)'''

import math
x = int(input("Enter the value of x\n"))
sinh = (math.exp(x) - math.exp(-x))/2
print("The value for sin hyperbolic function is : ", sinh)