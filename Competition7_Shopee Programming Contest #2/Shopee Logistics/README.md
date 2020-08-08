## Shopee Logistics

We have a lot of interesting tasks at Shopee. One of them is a logistics problem. In this problem we need to deliver goods from the hub to the final customer. But before that we can move goods between the hubs. Shopee has a giant network of hubs but in this task will be used the network with N hubs and N - 1 routes between hubs. Each hub is reachable from any other hub.

One of the problems of logistics is to optimise network. Before optimising we need to do some research and find some routes with problems. For example, find the largest path and make a route between two hubs the most distant. We are calling it “The longest path”.

In this task we are asking you to find the second longest path in the Shopee network.

Don’t need to output the path! We need only the length!

## Input

Input starts with an integer N (5 ≤ N ≤ 105), denoting the number of hubs. Next N - 1 lines contain three values: two hubs and the route length between them. Li ≤ 105.

## Output

Print one line. The length of the second longest path.

SAMPLE INPUT
5
1 2 5
2 3 1
2 4 2
2 5 3

SAMPLE OUTPUT
7

##### Explanation
The longest path will be 1->2->5: (8). The second longest path will be 1->2->4. (7)