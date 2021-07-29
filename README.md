# Question3
# Explanation 1

Step 1 :
define the data types according the constrains here all the numbers are very small so we will use integer data type.

Step 2:

Analysis the problem and get the condition that would  make the strip is  valid  or not .
here we would find the conditions which will  make the strip is invalid  if  :

The max of the strip lengths is not the center
The first and the last length are not equal to i 1 which means the strip not start from length 1 and ends  on 1 .
N (number of parts of the strip )is not odd which that means there is no center.
if the parts not increase by 1 from the start to center and not decrease by 1 from center to end .
If there is no case from the past four cases then the strip is valid .

# Explanation 2

In the first strip, all the conditions are satisfied, hence it is valid.

In the second strip, it does not start with a 1, and hence is invalid.

In the third strip, it keeps increasing even past the centre, instead of decreasing. Hence invalid.

The fourth strip does not increase and decrease by exactly 1. Hence invalid.

The fifth satisfies all conditions and hence is valid.

The sixth and seventh strip do not have a 'centre' part. Because for every part, there are either more parts to its right than its left, or more parts on its left than its right. Hence both the strips are invalid.
