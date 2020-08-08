## Connectivity

In Shopee Data Center, there are many switches and some of the switches are interconnected to form a network. Sometimes, we add a new connection to the network and if we find that there is some issue, we may remove the last added connections. You will need to solve a similar problem.

You are given an empty network with N switches (numbered 1 to N) and no connections between switches. You will also face Q scenarios in chronological order. Each scenario can be any of the following:

PUSH u v : You have to add a new connection between switches u and v. (u ≠ v, 1 <= u, v <= N). Note that there can be multiple connections between the same pair of switches.

POP : From all the connections currently present in the network, remove the one that was added most recently. There will be at least one connection in the network when this scenario is given.

Also, after performing the operation in each scenario, print the number of connected components formed by the switches in this network.

## Input

The first line of test case begins with integer Q (1 <= Q <= 5 * 105) and N (1 <= N <= 5 * 105) indicating the number of scenarions and number of switches in the network. Next, Q lines will each contain a scenario as described above.

## Output

For each query, you will need to print the answer in a separate line.

SAMPLE INPUT
12 5
PUSH 1 2
PUSH 2 3
PUSH 1 4
POP
PUSH 1 3
PUSH 4 5
PUSH 1 4
POP
POP
POP
POP
POP

SAMPLE OUTPUT
4
3
2
3
3
2
1
2
3
3
4
5