# Pi Estimator

## Problem Description

Let rdn() be a function that generates float a number within [0,1]
return an approximation of pi

## Solution

we will be using the rdn function twice to generate points (x and y values)
now lets generate a circunference with 1cm as radius
then we count how many points are within the circunference
(point p is inside the circunference if the \sqrt{x²+y²} < 1)

now lets see the circle area formula:
    \pi * r²
but as we are only considering 1st cuadrant it will be:
    (\pi * r²)/(2 * r)²
as the radius is 1 that leaves:
    (\pi)/4
now lts consider the area of the circle as the number of points inside it divided by the number of total points
that leaves then:
    (\pi)/4 = (points inside) / (total points)

aisolating pi, we end up with:
    \pi = 4 * (points inside) / (total points)

