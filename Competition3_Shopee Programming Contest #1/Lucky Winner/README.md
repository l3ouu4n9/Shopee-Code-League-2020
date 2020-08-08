## Lucky Winner

Ding Ding Ding! You have been chosen to be the one and only winner of SHOPEE LUCK LEAGUE.

We’re giving you K tokens to pick items on our shopee search results page for FREE!

Each token can get two adjacent items on the grid (horizontally or vertically).

Given that shopee search results page is a grid of N rows and 3 columns (actually it’s 5, but we specially change our UI to make your life easier). Each item on the grid has a price (the price can be negative). 

The rule are you have to use all of your tokens, one item can only be covered by one token (no overlapping here, you can’t buy one item twice). Your goal is to find the maximum worth of items you can bring home.

## Input

First line, number N (number of rows) (1 <=N <= 1000), and K (number of tokens) (1 <= K <= 1000)

N next lines, each line contain 3 numbers, the values of the board (abs(a[i,j]) <= 1e6)

## Output

A single number of the maximum worth of items that can be cover with exactly K non-overlapping tokens

SAMPLE INPUT<br>
5 3<br>
100 -9 -1<br>
-1 3 2<br>
-9 2 3<br>
2 5 1<br>
3 3 4

SAMPLE OUTPUT<br>
113

##### Explanation
Second example: It’s optimal to use 3 tokens on [100, -1], [2, 5], and [3,4]
