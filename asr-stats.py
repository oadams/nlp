import argparse
from distance import min_edit_distance_align
from distance import cluster_alignment_errors

parser = argparse.ArgumentParser(
        description="Present stats about ASR errors")
parser.add_argument("--ref", type=str)
parser.add_argument("--hypo", type=str)
args = parser.parse_args()

refs = open(args.ref).readlines()
hypos = open(args.hypo).readlines()
assert len(refs) == len(hypos)

alignments = []

errors = []
asr_pairs = zip(refs, hypos)
for asr_pair in asr_pairs:
    ref = asr_pair[0].split()
    hypo = asr_pair[1].split()
    alignment = min_edit_distance_align(ref, hypo)
    alignments.append(alignment)
    #clustered_alignment = cluster_alignment_errors(alignment)
#    print(alignment)
    #print(clustered_alignment)
    for align_item in alignment:
    #for align_item in clustered_alignment:
        if align_item[0] != align_item[1]:
            errors.append(align_item)

err_hist = {}
for error in errors:
    if error in err_hist:
        err_hist[error] += 1
    else:
        err_hist[error] = 1

error_list = sorted(err_hist.items(), key=lambda x: x[1], reverse=True)
for error_count in error_list:
    error = error_count[0]
    print()
    print("Error: %s, count: %d" % (str(error), error_count[1]))
    print("Examples:")
    print()
    count = 0
    for alignment in alignments:
        if error in alignment:
            count += 1
            ref = []
            hypo = []
            for pair in alignment:
                if pair == error:
                    ref.append("**" + pair[0] + "**")
                    hypo.append("**" + pair[1] + "**")
                else:
                    ref.append(pair[0])
                    hypo.append(pair[1])
            print("".join(ref))
            print("".join(hypo))
            print()

        if count == 3:
            break

#print errors
sub_count = 0
del_count = 0
ins_count = 0
for error in errors:
    if error[0] == "":
        ins_count += 1
    elif error[1] == "":
        del_count += 1
    else:
        sub_count += 1

print("substitution %:", (float(sub_count)/len(errors)) * 100)
print("deletion %:", (float(del_count)/len(errors)) * 100)
print("insertion %:", (float(ins_count)/len(errors)) * 100)
