# Pi Estimator

## Problem Description

Let rdn() be a function that generates float a number within [0,1]
return an approximation of pi

## Solution

we will be using the rdn function twice to generate points (x and y values)
now lets generate a circunference with 1cm as radius
then we count how many points are within the circunference
(point p is inside the circunference if the \sqrt{x²+y²} < 1)
