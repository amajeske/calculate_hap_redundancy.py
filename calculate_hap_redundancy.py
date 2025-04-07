#!/usr/bin/env python

from collections import defaultdict
from intervaltree import Interval, IntervalTree

# Set path to your PAF file and hap.fa file
paf_file = "/mnt/gs21/scratch/k0017008/ragtag.mapped.purged.vs.hap.paf"
hap_fa_lengths = {}

# Step 1: Get contig lengths from the PAF file (column 2)
with open(paf_file) as f:
    for line in f:
        fields = line.strip().split('\t')
        contig = fields[0]
        length = int(fields[1])
        hap_fa_lengths[contig] = length  # Will be overwritten, but lengths should be consistent

# Step 2: Build interval trees for alignments
aligned_intervals = defaultdict(IntervalTree)

# Track the contigs aligned in the first round
first_round_mapped = set()
second_round_mapped = set()

with open(paf_file) as f:
    for line in f:
        fields = line.strip().split('\t')
        contig = fields[0]
        q_start = int(fields[2])
        q_end = int(fields[3])
        aligned_intervals[contig].add(Interval(q_start, q_end))

# Step 3: Merge intervals and calculate aligned bp
total_aligned_bp = 0
total_hap_bp = 0

for contig, intervals in aligned_intervals.items():
    intervals.merge_overlaps()
    aligned_length = sum(iv.end - iv.begin for iv in intervals)
    total_aligned_bp += aligned_length
    total_hap_bp += hap_fa_lengths[contig]

# Add unaligned contigs (completely unmapped contigs won't be in the PAF file)
for contig, length in hap_fa_lengths.items():
    if contig not in aligned_intervals:
        total_hap_bp += length

# Step 4: Report
print(f"Total basepairs in hap.fa: {total_hap_bp:,}")
print(f"Total basepairs aligned (redundant): {total_aligned_bp:,}")
print(f"Total basepairs unaligned (unique): {total_hap_bp - total_aligned_bp:,}")
print(f"% redundant: {100 * total_aligned_bp / total_hap_bp:.2f}%")
print(f"% unique: {100 * (total_hap_bp - total_aligned_bp) / total_hap_bp:.2f}%")
