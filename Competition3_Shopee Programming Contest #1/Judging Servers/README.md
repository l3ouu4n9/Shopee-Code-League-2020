## Judging Servers

As we all know, you are the chief judge for the upcoming Shopee Code League hosted by our favorite E-Commerce platform Shopee. You have already selected N problems from hundreds of thousand of problems from your quality Problem Bank. Since you want to make every contestant happy even if he/she got Wrong Answers on every problem during the contest, you have decided to judge each problem on a different server.

Now you have to buy N judging servers from SEA Server Limited which is a reputed company. SEA Server Limited has total S servers in a row numbered from 1 to S and you have to choose N servers from these S servers. The i’th server has a price tag of Pi where 1 ≤ i ≤ S. You cannot rent these servers on an hour or day basis. However, SEA Server Limited has a lifetime offer for you. If you buy any server then you get one of the adjacent servers for free if you wish. If you choose to buy the i’th server then you can get the (i-1)’th or (i+1)’th server for free if you want to take it for free. The contest date has a tag of coming soon and the contest organizers want to know the total cost for the problem set and judging servers from you. Since you are the ultimate chief judge who wants to maximize your profit and as well as make every contestant happy. You have to choose N servers with lowest cost possible to maximize your profit.

## Input

Input starts with an integer T (1 ≤ T ≤ 50), denoting the number of test cases.

Each case starts with two integers S (1 ≤ S ≤ 1000) and N (1 ≤ N ≤ S). Next line contains S integers separated by space and the i’th integer of this line represents the price tag Pi of the i’th server (0 ≤ Pi ≤ 109).

## Output

For each case, print the case number and the minimum cost to buy the N servers.


SAMPLE INPUT
2
3 2
15 14 15
5 3
1000 560 30 85 100


SAMPLE OUTPUT
Case 1: 14
Case 2: 115

##### Explanation
In the second case, you can pay for the 3rd and the 4th servers with a cost of 115 and take the 2nd or 5th server for free.