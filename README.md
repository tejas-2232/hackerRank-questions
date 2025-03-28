# hackerRank-questions

Problem1: The conversation stack


Ayman and Johnny are yappers. In one conversation, they keep thinking of new topics they want to talk about. In order to make sure all of their topics get covered, these yappers have created a personal "conversation stack". That is, they will take turns talking about topics they have thought of from most recent to oldest. If one person is out of topics, the other person continues through their topics in most recent to oldest order. Ayman and Johnny think this conversation stack is a genius idea and are trying to get Mathew and Stephanie to use it in their conversations too. However, Mathew and Stephanie can't seem to figure out how to do it on their own. Create an algorithm to do it for them!

![image](https://github.com/user-attachments/assets/33f5c75d-f08e-4199-8fcc-5e24a88fb443)

Input Format

The first line contains the number of topics Mathew has.
The second line contains the number of topics Stephanie has.
The third line contains Mathew’s space-separated topics.
The fourth line contains Stephanie’s space-separated topics.
If someone has no topics their line contains " " (single space) and their list's length is 0.
Constraints

0 ≤ number of topics ≤ 1000 per person
Each topic is at most 50 characters long
Each topic is a string containing letters and/or numbers
Output Format

Output a single line of space-separated words representing the topic order.
Mathew speaks first, then Stephanie, alternating through their most recent topics.
If one person runs out of topics, the other continues alone.
There should be no spaces or newlines after the last word.
Sample Input 0

3
5
ACM party anime
CS301 CSEA Weinschenk TRP presentation
Sample Output 0

anime presentation party TRP ACM Weinschenk CSEA CS301
Explanation 0

Starting with Mathew's topics, the topics were outputed in reverse order while alternating between Mathew and Stephanie for both of their last 3 topics. Mathew was then out of topics, so Stephanie's topics continued to be outputed in reverse without alternating.

Sample Input 1

3
2
PDAs Project4 Midterm
anime JJK
Sample Output 1

Midterm JJK Project4 anime PDAs
Explanation 1

Starting with Mathew's topics, the topics were outputed in reverse order while alternating between Mathew and Stephanie for both of their last 2 topics. Stephanie was then out of topics, so Mathews's topics continued to be outputed in reverse without alternating.

Sample Input 2

3
3
I love ACM
Yeah its awesome
Sample Output 2

ACM awesome love its I Yeah
Explanation 2

Starting with Mathew's topics, the topics were outputed in reverse order while alternating between Mathew's and Stephanie's topics.

Solution1: conversation_stack.py

<hr>

## Problem2 Oddly Expensive Loops
After a grueling semester of CS301, Jack finally decides to take a well-desrved vacation. His dream? To visit every spot on his bucket list.

However, there is a catch. The travel agency Jack booked with has an insane surcharge policy: if any part of the trip forms a cycle with an odd number of destinations, he must pay an extra fee because, apparently, "odd cycles create odd vibes".

Unfortunately, Jack already spent most of his money this semester on energy drinks and the textbook, so he cannot afford any surcharge. He decides to plan his vacation route to avoid all odd-length cycles.

Decide whether or not Jack can travel fee-free, or if his journey is doomed?

You must pass ALL test cases to receive credit.

Input Format

The number of locations is given as numLocations. A 2-D adjacency matrix called journey[][] of size numLocations x numLocations where each element is represented by either a 1(there is connection to a location) or 0(no connection to a location).

Constraints

numLocations >= 2

Output Format

Return true if no odd-length cycles found, false otherwise.

Sample Input 0

4
0 1 0 1
1 0 1 0
0 1 0 1
1 0 1 0
Sample Output 0

1
Explanation 0

This graph is a cycle of length 4 so we should return true(1).

Sample Input 1

6
0 1 0 0 0 1
1 0 1 0 0 0
0 1 0 1 1 1
0 0 1 0 1 1
0 0 1 1 0 1
1 0 1 1 1 0
Sample Output 1

0
Explanation 1

There is an odd cyle of length 3(look at 3rd, 4th and 5th row). So return false(0).

### solution:  oddly-loops.py


### Problem3
