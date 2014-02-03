import numpy

def min_edit_distance(source, target,
        ins_cost=lambda _x: 1,
        del_cost=lambda _x: 1,
        sub_cost=lambda x, y: 0 if x == y else 1):
    """Finds the minimum edit distance between two strings using the
    Levenshtein weighting as a default, but offers keyword arguments to supply
    functions to measure the costs for editing with different characters.

    ins_cost -- A function describing the cost of inserting a given char
    del_cost -- A function describing the cost of deleting a given char
    sub_cost -- A function describing the cost of substituting one char for
    another

    """

    # Initialize an m+1 by n+1 array. Note that the strings start from index 1,
    # with index 0 being used to denote the empty string.
    n = len(target)
    m = len(source)
    distance = numpy.zeros([m+1, n+1], dtype=numpy.int16)

    # Initialize the zeroth row and column to be the distance from the empty
    # string.
    for i in xrange(1, m+1):
        distance[i, 0] = distance[i-1, 0] + ins_cost(source[i-1])
    for j in xrange(1, n+1):
        distance[0, j] = distance[0, j-1] + ins_cost(target[j-1])

    # Do the dynamic programming to fill in the matrix with the edit distances.
    for j in xrange(1, n+1):
        for i in xrange(1, m+1):
            distance[i, j] = min(
                    distance[i-1, j] + ins_cost(source[i-1]),
                    distance[i-1, j-1] + sub_cost(source[i-1],target[j-1]),
                    distance[i, j-1] + del_cost(target[j-1]))

    return distance[len(source), len(target)]

assert min_edit_distance("intention", "execution") == 5
assert min_edit_distance("kitten", "sitting") == 3
assert min_edit_distance("rosettacode", "raisethysword") == 8
assert min_edit_distance("saturday", "sunday") == 3
assert min_edit_distance("donkey", "horse") == 4
assert min_edit_distance("industry", "interest") == 6
