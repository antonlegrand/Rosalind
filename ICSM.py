"""
Problem
A common substring of a collection of strings is a substring of every member of the collection. We say that a common substring is a longest common substring if there does not exist a longer common substring. For example, "CG" is a common substring of "ACGTACGT" and "AACCGTATA", but it is not as long as possible; in this case, "CGTA" is a longest common substring of "ACGTACGT" and "AACCGTATA".

Note that the longest common substring is not necessarily unique; for a simple example, "AA" and "CC" are both longest common substrings of "AACC" and "CCAA".

Given: A collection of k
 (k≤100
) DNA strings of length at most 1 kbp each in FASTA format.

Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)

Sample Dataset
>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA
"""

def longest_common_substring() -> str:
    sample_data = """>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA
"""
    with open("input.fasta", "w", encoding="utf-8") as f:
        f.write(sample_data)

    sequences = {}
    label, seq = "", ""
    with open("input.fasta", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if label:
                    sequences[label] = seq
                label, seq = line[1:], ""
            else:
                seq += line
    if label:
        sequences[label] = seq

    seqs = list(sequences.values())
    ref = min(seqs, key=len)

    for length in range(len(ref), 0, -1):
        candidates = {
            ref[i:i + length]
            for i in range(len(ref) - length + 1)
            if all(ref[i:i + length] in s for s in seqs)
        }
        if candidates:
            return min(candidates)
    return ""


print(longest_common_substring())
