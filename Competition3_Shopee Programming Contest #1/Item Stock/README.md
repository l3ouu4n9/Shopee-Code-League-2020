## Item Stock

Items in Shopee can have their stocks derived from other items. For example, 1 stock of item A can be derived from 2 stock of item B + 3 stock of item C. We say that item B and item C are parents of item A. For this problem, we are only interested when an item can only have 1 parent item. In this case, we can see the structure of stock derivation will form a rooted tree.

There are 2 kinds of derivations:

1. Dynamic stock derivation. Suppose that 1 stock of item A equals to Qty stock of item B. Then, the stock of item A will be equal to floor(item_B_stock / Qty).
2. Fixed stock derivation. Suppose that 1 stock of item A equals to Qty stock of item B, and we initially have S stock of item A. Then, item A will deduct stocks from its lowest ancestor which is fixed stock, to make sure that item A will have sufficient stock. It can be assumed that the root of the tree (1st item) will always be fixed stock. Note that the number of reserved stocks depends on the multiplication of the Qty from the path of item A to that ancestor, not just the Qty to item B. Please refer to the example input for clarity.

At first, we only have item 1, which initially has M stock. Then, we add N-1 items one-by-one, possibly changing the stock of some items at each step. In the end, what will be the stock of each item?

## Input

The first line contains 2 integers N (1 ≤ N ≤ 100,000) and M (1 ≤ M ≤ 1,000,000,000), denoting the number of items and the initial stock of the 1st item.

The next N-1 lines contain the description of the i-th item (starting from 2), which can be in one of the 2 following formats:

- 1 Pi Qtyi (1 ≤ Pi < i, 1 ≤ Qtyi ≤ 10), which means the i-th item has dynamic stock with parent item Pi and 1 stock of it equals to Qtyi stock of its parent
- 2 Pi Qtyi Si (1 ≤ Pi < i, 1 ≤ Qtyi ≤ 10, 1 ≤ Si ≤ 1,000,000,000), which means the i-th item has fixed stock with parent item Pi, 1 stock of it equals to Qtyi stock of its parent, and has initial stock of Si.
It is guaranteed that at the end, the stock for each item will be non-negative.

## Output

Output N lines, each containing an integer. The integer in the i-th line denotes the stock of the i-th item.

SAMPLE INPUT<br>
5 15<br>
1 1 2<br>
2 1 3 1<br>
1 2 1<br>
2 4 3 1


SAMPLE OUTPUT<br>
6<br>
3<br>
1<br>
3<br>
1
