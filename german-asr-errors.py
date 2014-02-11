from distance import min_edit_distance_align
from distance import cluster_alignment_errors
from collections import defaultdict

ref = open("/home/oadams/Desktop/oliver-phonemes/ref.txt").readlines()
hypo = open("/home/oadams/Desktop/oliver-phonemes/hypo.txt").readlines()

assert len(ref) == len(hypo)

errors = []
for i in xrange(len(ref)):
    print i, len(ref)
    refline = ref[i].split()
    hypoline = hypo[i].split()
    alignment = min_edit_distance_align(refline, hypoline)
    clustered = cluster_alignment_errors(alignment)
    for align_item in clustered:
        if align_item[0] != align_item[1]:
            errors.append(align_item)

print errors
error_dict = defaultdict(int)
for error in errors:
    tuple_error = (tuple(error[0]), tuple(error[1]))
    error_dict[tuple_error] += 1

sorted_errors = sorted(error_dict.items(), key=lambda item: item[1])
for error in sorted_errors:
    print error
