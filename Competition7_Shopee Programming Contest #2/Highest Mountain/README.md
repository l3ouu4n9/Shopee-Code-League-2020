## Highest Mountain

Victor is assigned a task for planning quarterly team outings in Shopee. He is trying to organize an outdoor activity to climb the highest mountain among a mountain range. However, it is difficult to tell which mountain is the highest in the mountain range from a distance. Help Victor to identify the highest mountain given the height of the mountains.

In order to climb a mountain, the mountain needs to either increase or decrease consistently by 1 and has at least one side to be able to be seen connected to the ground. Given that 1 is ground level, “2324” is not a valid mountain to be climbed, while “1234” and “4321” are valid mountains with height of 4.

Find the height of the highest climbable mountain.

## Input

The first line will specify the N number of mountain ranges

Subsequent N sets will have length L and a series of numbers separated by space representing the height (H)

Height: 1 <= H <= 1000

Length: 1 <= L <= 1000

## Output

Integer specifying the height (H) of the highest mountain and index (I) of the peak. If there are multiple mountains with the same height, return the leftmost mountain.

If the height or index is not available, return -1. Return the result for each case with format “Case #{N}: H I”

SAMPLE INPUT<br>
6<br>
<br>
10<br>
1 2 3 2 3 4 2 3 2 5<br>
<br>
10<br>
3 2 3 2 3 4 3 2 1 4<br>
<br>
5<br>
1 1 1 1 1<br>
<br>
10<br>
10 9 8 7 6 5 4 3 2 1<br>
<br>
1<br>
5<br>
<br>
1<br>
1

SAMPLE OUTPUT<br>
Case #1: 3 2<br>
Case #2: 4 5<br>
Case #3: 1 0<br>
Case #4: 10 0<br>
Case #5: -1 -1<br>
Case #6: 1 0

##### Explanation
1 2 3 2 3 4 2 3 2 5

3 has a way to enter from the ground while 4 and 5 doesn’t.

The highest mountain will be "1 2 3" with the height of 3 because a mountain can only be either increase or decrease consistently by 1 and not both. When it increase from 1 to 3, it cannot decrease to 2 again.

3 2 3 2 3 4 3 2 1 4

4 has a way to enter from the ground and it is decreasing consistently by 1.

2 3 4 5 6

There is no way to enter from the ground.

1 2 4 5

The mountain is unable to jump from 2 to 4.
