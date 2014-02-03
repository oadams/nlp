import distance

def word_error_rate(ref, hypo):
    """Returns the word error rate of the supplied hypothesis with respect to
    the reference string."""

    min_edit_distance = distance.min_edit_distance(ref, hypo)
    return 100 * float(min_edit_distance) / len(ref)
