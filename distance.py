import numpy as np

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
    distance = np.zeros([m+1, n+1], dtype=np.int16)

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

def min_edit_distance_align(source, target,
        ins_cost=lambda _x: 1,
        del_cost=lambda _x: 1,
        sub_cost=lambda x, y: 0 if x == y else 1):
    """Finds the minimum cost alignment between two strings using the
    Levenshtein weighting as a default, but offering keyword arguments to
    supply functions to measure the costs for editing with different
    characters.

    ins_cost -- A function describing the cost of inserting a given char
    del_cost -- A function describing the cost of deleting a given char
    sub_cost -- A function describing the cost of substituting one char for
    another

    """

    # Initialize an m+1 by n+1 array. Note that the strings start from index 1,
    # with index 0 being used to denote the empty string.
    n = len(target)
    m = len(source)
    distance = np.zeros([m+1, n+1], dtype=np.int16)

    # Initialize the array that holds pointers to the previous cell in the
    # alignment path.
    pointers = np.zeros([m+1, n+1], dtype=np.dtype(("int16", (2,))))

    # Initialize the zeroth row and column to be the distance from the empty
    # string.
    for i in xrange(1, m+1):
        distance[i, 0] = distance[i-1, 0] + ins_cost(source[i-1])
        pointers[i, 0] = np.array([i-1, 0])
    for j in xrange(1, n+1):
        distance[0, j] = distance[0, j-1] + ins_cost(target[j-1])
        pointers[0, j] = np.array([0, j-1])

    # Do the dynamic programming to fill in the matrix with the edit distances.
    for j in xrange(1, n+1):
        for i in xrange(1, m+1):
            options = [
                    (distance[i-1, j] + ins_cost(source[i-1]),
                        np.array([i-1, j])),
                    (distance[i-1, j-1] + sub_cost(source[i-1],target[j-1]),
                        np.array([i-1, j-1])),
                    (distance[i, j-1] + del_cost(target[j-1]),
                        np.array([i, j-1]))]
            (minimum, pointer) = sorted(options, key=lambda x: x[0])[0]
            distance[i, j] = minimum
            pointers[i, j] = pointer

    print distance
    print pointers
    # Put the backtrace in a list
    """"
    cell = np.array([m, n])
    backtrace = [cell]
    while True:
        cell = pointers[cell[0], cell[1]]
        backtrace.append(cell)
        if cell[0] == 0 and cell[1] == 0:
            break
    backtrace.reverse()

    print backtrace

    if cell[0] - prev_cell[0] == 1 and cell[1] - prev_cell[1] == 1:
        backtrace
    """
