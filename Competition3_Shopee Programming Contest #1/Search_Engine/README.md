## Search Engine

Who doesn’t like to search and see these unexpected search suggestions floating just below the search bar. Everyone likes it!!!  As we all know Shopee, one of the largest E-commerce platforms, also has a search bar where users can search for all kinds of items. Shopee wants to build a new search engine. And you are to help Shopee to implement this new engine.

You are given a data set that contains all the item’s names, and an item’s name is represented as an ordered sequence of strings separated by a single space and the strings contain only lowercase English alphabets(a-z) and digits(0-9). for example, a valid name could be, “apple iphone se 2”. Queries for the new search engine will be a sequence of alphanumeric strings separated by space. For example, “se 2” or “11 pro max” and the search engine has to answer how many different items are there in the data set containing the query sequence in their name in exact order. For example, “se 2” matches the item “apple iphone se 2”, however “app” doesn’t match this item.

## Input

Input starts with an integer T (1 ≤ T ≤ 15), denoting the number of test cases. The first line of each test case will contain two integers N (1 ≤ N ≤ 10<sup>4</sup>) and Q (1 ≤ Q ≤ 10<sup>4</sup>). Here, N is the number of items in the database and Q is the total number of queries. Each of the next N lines will contain an item’s name as described.  Each of the next Q lines will contain a search query as described. You can safely assume that each item’s name will contain at most 10 spaces and the total length will be between 1 to 50.

## Output

For each case, print the case number in a single line. Then for each query Q print the number of different names in the database who contains the query sequence in their name in exact order.

## Constraints

Total number of characters in the dataset will be not more than 7×10<sup>5</sup>


SAMPLE INPUT<br>
2<br>
3 6<br>
apple lettuce limes avocado<br>
onion cranberries apple limes<br>
escarole corn28corn apple lettuce limes avocado<br>
limes avocado<br>
apple lettuce<br>
limes<br>
apple<br>
app<br>
apple limes<br>
3 3<br>
apple iphone se 2<br>
iphone 11 max pro<br>
iphone 11 pro max<br>
apple iphone<br>
max pro<br>
iphone

SAMPLE OUTPUT<br>
Case 1:<br>
2<br>
2<br>
3<br>
3<br>
0<br>
1<br>
Case 2:<br>
1<br>
1<br>
3

##### Explanation
For the first test case, both “limes avocado” and “apple lettuce” match both 1st and 3rd items, “limes” and “apple” match in all three items, “app” doesn’t match any item and “apple limes” matches the second item.
