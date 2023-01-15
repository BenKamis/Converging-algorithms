# Converging-algorithms
Three algorithms that test fractions until they converge to a predetermined float

The float is simplified to only the decimal places
for the algorithms to work with

The first algorithm starts with a test fraction of 0/1
If the test fraction is larger than the decimal:
The numerator is increased by 1
If the test fraction is smaller than the decimal:
The numerator is decreased by 1 and the denominator is increased by 1
This test is repeated until the fraction equals the decimal.

The second algorithm starts with a test fraction of 1/1,
If the test fraction is larger than the decimal:
The denominator is increased by 1
If the test fraction is smaller than the decimal:
The denominator is decreased by 1 and the numerator is increased by 1
This test is repeated until the fraction equals the decimal.

The third algorithm starts with a test fraction of 1/1,
If the test fraction is larger than the decimal:
The denominator is increased by 1
If the test fraction is smaller than the decimal:
The numerator is increased by 1
This test is repeated until the fraction equals the decimal.

Graphs generated include:
All test fractions tested by the algorithms as they converge to the user-input value
The number of loop iterations the algorithms took to reach the float for a range of values
Which algorithm reached the float in fewer loop iterations for a range of values

Note: I refer to "counts" as the number of loop iterations to reach the exact float.

Q&A:
Do negative floats work?
Yes!

Does the algorithms always converge for all floats?
So far, they seem to!

Why are algorithms 2 and 3 symmetrical about x = 0.5?
Rounding is handled differently in these algorithms than in algorithm 1. Algorithm 1 can support negative numerators, but algorithm 2 cannot support a non-natural denominator and algorithm 3 does not subtract from the numerator or denominator

Why do "lines" form over a range of values being tested?
The highest count lines for each algorithm is the max number of steps required. These are discontinuous points have one point between them, which is where the float is divisible by 2, and the fraction was simplified by the algorithms (Ex. The algorithms found 1/500 instead of 2/1000). The points also have gaps every 5 points, because these are also simplified. Each "line" has holes here because 10 is divisible by 2 and 5, and all of these float fractions are some integer divided by a power of 10. Note that when the float interval is 0.001 or so, the highest line has 2x as many counts as the next line, then 4x as many as the next, 5x as many as the next, 8x, 10x, etc. The points in the lines further down become more sparse, so they may not appear as lines.

Why is algorithm 1 faster than algorithm 2 only for floats exactly between 1/2 and 2/3?
The equations of these intersecting lines after being tested over a range of values are y = 1000x + 1000 for the blue line (algorithm 1) and y = -2000x + 3000 for the red line (algorithm 2) (only between floats 0.5 and 1, exclusive). These intersect exactly at 2/3, so they take the same number of loop iterations to converge for an input float of 0.666666. Why these lines have these slopes over this range, I do not know. This part of the question is still unknown.

Why do the points in the number of counts graph form approximate lines at all? These seem too non-random for how simple the algorithms are!
Answer unknown, let me know if you make progress on this!

Why do algorithms 2 and 3 (orange points) have the same count number for a range of values that appears asymptotic?
Answer unknown, let me know if you make progress on this!

Other interesting tidbit:
Repeating a digit to converge to (Ex. 0.111111, 0.666666, etc.) makes the number of loop iterations to reach the float in all three algorithms appear nearly the same, but with a repeated digit in the middle (Ex. 0.666666 requires 833331 steps from algorithm 1, 833331 steps from algorithm 2, and 666665 steps from algorithm 3)

File reupload 1: Some rounding issues, now resolved.
File reupload 2: Adding algorithm 3, fixed another rounding issue, and added the Q&A section here as I understood the theory behind the project more.
