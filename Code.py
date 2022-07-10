"""
The iterative code is provided on VLE.
Major and minor changes have been made to the code since it had a lot of errors, warnings, and it was not on PEP8
standard. PyCharm would not run it with the errors.
"""

import sys  # to use maxsize to indicate that there is no edge between any two vertices
import itertools  # from the PDF

"""
The code is from the provided PDF. Graph2 is an addition
from geeksforgeeks.
I have renamed them for ease of understanding.
"""

NO_PATH = sys.maxsize
Sample_Input1 = [[0, 7, NO_PATH, 8],
                 [NO_PATH, 0, 5, NO_PATH],
                 [NO_PATH, NO_PATH, 0, 2],
                 [NO_PATH, NO_PATH, NO_PATH, 0]]
# On Sample_Input2, I have changed the INF from geeksforgeeks
# to NO_PATH for consistency reason.
Sample_Input2 = [[0, 5, NO_PATH, 10],
                 [NO_PATH, 0, 3, NO_PATH],
                 [NO_PATH, NO_PATH, 0, 1],
                 [NO_PATH, NO_PATH, NO_PATH, 0]]

"""
The PDF named the imperative function floyd(distance). To make it easy to differentiate with the recursive version
I changed its name to imperative_floyd(distance).
"""


def iterative_floyd(distance):
    """
    A simple implementation of Floyd's algorithm
    """
    max_length = len(distance)  # This is relocated inside the function to be able to use it for other inputs.
    for intermediate, start_node, end_node \
            in itertools.product(range(max_length), range(max_length), range(max_length)):
        if start_node == end_node:
            distance[start_node][end_node] = 0
            continue

        # return all possible paths and find the minimum
        distance[start_node][end_node] = min(distance[start_node][end_node],
                                             distance[start_node][intermediate] + distance[intermediate][end_node])

    return distance


"""
The recursive version of Floyd's algorithm is below:
"""


def recursive_floyd(distance, k=0, i=0, j=0):
    """
    The function recursive_floyd is defined to run the Floyd algorithm under the below circumstances
    distance refers to the input graphs.
    type distance: 2D matrix
    param i: start node
    param j: end node
    param k: intermediate node
    Parameters i,j,k should not exceed the maximum limit of the matrix which is defined as max_length
    j needs to be 1 less than the maximum limit of the matrix to run recursively without error.
    i needs to be 1 less than the maximum limit of the matrix to run recursively without error.
    There is no -1 for (k) because the function at the beginning stops the recursive process. Once complete, the number
    reaches the maximum limit which stops the recursion from calling itself since it does not fulfill the requirement of
    being less than the maximum limit of the matrix.
    """
    max_length = len(distance)  # This is placed to inside the function to be able to use it for other inputs.
    if k < max_length:
        distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])  # Floyd's formula
        if j < max_length - 1:
            j += 1
        elif i < max_length - 1:
            j = 0
            i += 1
        elif k < max_length:
            j = 0
            i = 0
            k += 1
        recursive_floyd(distance, k, i, j)
    return distance


def print_graph(distance):
    """
    This utility function prints the solution in a custom format graph.
    Nodes that are within the maximum limit of the array will be printed.
    Nodes that do not reach the edge will have an infinity value which in this program is defined as NO_PATH
    """
    max_length = len(distance)  # This is placed inside the function to be able to use it for other inputs.
    for i in range(max_length):
        for j in range(max_length):
            if distance[i][j] == NO_PATH:
                print("%7s" % "NO_PATH", end=" ")  # creates 7 string positions and fill it with NO_PATH
            else:
                print("%7d\t" % distance[i][j], end="")  # creates 7 digits positions and fill it with the output number
            if j == max_length - 1:  # This creates a new row for the next values
                print()
    print()


print("Sample_Input1 before applying the algorithm to it: ")
print_graph(Sample_Input1)
print("The following matrix shows the SHORTEST routes between every pair of vertices for Sample_Input1 using ITERATION")
print_graph(iterative_floyd(Sample_Input1))
print("The following matrix shows the SHORTEST routes between every pair of vertices for Sample_Input1  using "
      "RECURSION")
print_graph(recursive_floyd(Sample_Input1))
print("---------------")
print("Sample_Input2 before applying the algorithm to it: ")
print_graph(Sample_Input2)
print("The following matrix shows the SHORTEST routes between every pair of vertices for Sample_Input2  using "
      "ITERATION")
print_graph(iterative_floyd(Sample_Input2))
print("The following matrix shows the SHORTEST routes between every pair of vertices for Sample_Input2 using RECURSION")
print_graph(recursive_floyd(Sample_Input2))
