# calculate_hap_redundancy.py

This script calculates **haplotype-level sequence redundancy** from a PAF file (output from tools like `minimap2`) by summing redundant basepairs aligned to a reference genome or assembly.

It is useful for estimating how much of a haplotype assembly is non-unique (e.g., duplicated or collapsed), which can help with assembly curation, redundancy filtering, and genome size validation.

## 🔧 Requirements

- Python 3.6+
- [intervaltree](https://pypi.org/project/intervaltree/)

Install required packages:
```bash
pip install intervaltree

Inputs
A .paf file (Pairwise mApping Format) produced by aligning one haplotype assembly to another (e.g., using minimap2)

The script assumes that the haplotype contig lengths can be inferred from column 2 of the PAF file (query length)

Usage
bash
Copy
Edit
python calculate_hap_redundancy.py
You can modify the script to change the path to your input .paf file:

python
Copy
Edit
paf_file = "/full/path/to/your/input.paf"

Output
Printed to standard output:
Total basepairs in hap.fa
Total basepairs aligned (redundant)
Total basepairs unaligned (unique)
Percentage of redundant and unique basepairs

Example:
yaml
Copy
Edit
Total basepairs in hap.fa: 125,000,000
Total basepairs aligned (redundant): 28,000,000
Total basepairs unaligned (unique): 97,000,000
% redundant: 22.40%
% unique: 77.60%

Related Tools
minimap2: For generating the .paf alignment file

purge_dups: For identifying and filtering redundant contigs
