import argparse
from distance import min_edit_distance

parser = argparse.ArgumentParser(
        description="Evaluate the phoneme error rate of a hypothesis " +
        "transcription with respect to a supplied reference.")
parser.add_argument("--ref", type=str)
parser.add_argument("--hypo", type=str)
parser.add_argument("--n", type=int)
args = parser.parse_args()

ref_lines = open(args.ref).readlines()
hypo_lines = open(args.hypo).readlines()
lines = zip(ref_lines, hypo_lines)
distances = []
for line in lines[:args.n]:
    distances.append(min_edit_distance(line[0].split(), line[1].split()))
print float(sum(distances)) / sum([len(line.split()) for line in ref_lines])
