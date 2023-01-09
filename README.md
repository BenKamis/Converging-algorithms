# Converging-algorithms
Two algorithms that test fractions until they converge to a predetermined float

The float is simplified to only the decimal places
for the algorithms to work with

The first algorithm starts with a test fraction of 0/1,
increases its numerator until it is larger than the float,
at which point it decreases the numerator by 1,
increases the denominator by 1, and repeats until it converges to the float.

The second algorithm starts with a test fraction of 1/1,
increases its denominator until it is smaller than the float,
at which point it decreases the denominator by 1 (unless it is 1)
increases the numerator by 1, and repeats until it converges to the float.

Graphs generated include:
All fractions tested by the algorithms as they converge to a user-input value
The number of loop iterations the algorithms took to reach the float for a range of values
Which algorithm was faster for different values
