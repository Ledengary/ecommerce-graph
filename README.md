# Detecting Communities in Graph
The final project of the "Data Structures" course
Besides implementing Graph data structure (in both Adjacency List and Adjacency Matrix), there are three phases in this project. 
__Phase One__ is dedicated to detecting communities in a given graph. Example: 

![Example](https://user-images.githubusercontent.com/60043933/90342916-3b339400-e021-11ea-95f3-65071f3768d1.JPG)
![Example](https://user-images.githubusercontent.com/60043933/90343302-771c2880-e024-11ea-9b1b-d7ae926a5496.JPG)

The specific algorithm for community detection uses a specific function to score each edge: (refer to papers directory)

![Example](https://user-images.githubusercontent.com/60043933/90342996-f4926980-e021-11ea-86b6-d649d272c2ee.JPG)

By calculating this score for every edge included in the graph, we delete the least scored edge which divides our graph into two communities. This process is intelligently  continued till it stops dividing the network into sub-communities. 

__Phase Two__ is dedicated to building an E-commerce app in which there are products published and rated. E-commerce app's products will be converted to graph vertices and passed to phase one to be interpreted \
First, we define each product as a vertex. Then by measuring Euclidean Distance Scores of all vertices we choose either to connect two of them with an edge or not. at the end of this phase, we have built up a graph.

![Example](https://user-images.githubusercontent.com/60043933/90343423-8059c500-e025-11ea-9a0d-0c46e9427a26.JPG)

__Phase Three__ is dedicated to plotting different sorting algorithms efficiency when applied on graph scores. Besides time and memory complexities will be compared too.

![Example](https://user-images.githubusercontent.com/60043933/90343444-b008cd00-e025-11ea-8b6a-3c3c50b8bb20.JPG)
