# Network Interpretation Task

Load one of the datasets. Adjust the node size, coloring and layout as you wish. You may also want to filter out some characters with a low number of scenes or a low degree (number of edges). Explore the graph to help you think through the following questions. You may want to partition the graph into a smaller number of nodes, such as a single house or community to help you think things through. 

If you ever want to view the scores of metrics directly, they will be available in the data laboratory after you run the appropriate statistic.



> ### A reminder of what the graph represents
>
> Each node is a character from a tv series or movie franchise. Each edge indicates that characters were co-present in a scene (not necessarily that they interacted). The weight of each edge indicates how many scenes they were co-present in. Communities show collections of characters that were more commonly co-present. Depending on the dataset characters may spread off into different groupings, or all cluster to varying degrees of closeness to central characters.

## 1. Degree
> You can calculate degree on the currently visible nodes and edges by going to Statistics > and running 'Average Degree'. Degree will now be available as an option in the dropdown when adjusting appearance.

Degree is the measure of how many edges are connected to a node. If a character has a high degree what does this tell us about that character?

## 2. Weighted Degree
> You can calculate weighted degree by running the Avg. Weighted Degree statistic.

Weighted degree is the sum total of all the edge weights connected to a node. Given what we know about the design of this network, what would a high weighted degree tell us about a character? What would it mean if a character had a low degree, but a high weighted degree?

## 3. Betweenness Centrality

> You can calculate betweeness centrality by running the Network Diameter statistic.

Betweeness centrality asks if a node wanted to reach every other node, which other node are most likely to be on the 'path' to get there? What would a high betweeness centrality mean for a character?

## 4. PageRank

> You can calculate PageRank from the statistics panel.

PageRank is like degree in that it ranks nodes by the number of connections it has. However it also then increases a node's score if it is connected to a highly connected node. We can think of it as influence. A person with only one connection may be low ranked, but if that one connection is to highest scoring person in the network, then their score will increase by association. What does it mean for a character to have a high PageRank in your network?





