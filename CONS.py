"""
A matrix is a rectangular table of values divided into rows and columns. An m×n
 matrix has m
 rows and n
 columns. Given a matrix A
, we write Ai,j
 to indicate the value found at the intersection of row i
 and column j
.

Say that we have a collection of DNA strings, all having the same length n
. Their profile matrix is a 4×n
 matrix P
 in which P1,j
 represents the number of times that 'A' occurs in the j
th position of one of the strings, P2,j
 represents the number of times that C occurs in the j
th position, and so on (see below).

A consensus string c
 is a string of length n
 formed from our collection by taking the most common symbol at each position; the j
th symbol of c
 therefore corresponds to the symbol having the maximum value in the j
-th column of the profile matrix. Of course, there may be more than one most common symbol, leading to multiple possible consensus strings.

A T C C A G C T
G G G C A A C T
A T G G A T C T
DNA Strings	A A G C A A C C
T T G G A A C T
A T G C C A T T
A T G G C A C T
A   5 1 0 0 5 5 0 0
Profile	C   0 0 1 4 2 0 6 1
G   1 1 6 3 0 1 0 0
T   1 5 0 0 0 1 1 6
Consensus	A T G C A A C T
Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)
"""
from collections import defaultdict
def consensus_and_profile() -> None:
    sample_data = """>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT
"""

    with open("input.fasta", "w", encoding="utf-8") as f:
        f.write(sample_data)

    sequences = {}
    current_label = ""
    current_sequence = ""

    with open("input.fasta", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            if not line:
                continue

            if line.startswith(">"):
                if current_label:
                    sequences[current_label] = current_sequence

                current_label = line[1:]
                current_sequence = ""
            else:
                current_sequence += line

        if current_label:
            sequences[current_label] = current_sequence

    if not sequences:
        print("No sequences found.")
        return

    sequence_length = len(next(iter(sequences.values())))

    if not all(
        len(sequence) == sequence_length
        for sequence in sequences.values()
    ):
        raise ValueError("All sequences must have the same length.")

    profile_matrix = {
        "A": [0] * sequence_length,
        "C": [0] * sequence_length,
        "G": [0] * sequence_length,
        "T": [0] * sequence_length,
    }

    # Construire la matrice de profil
    for sequence in sequences.values():
        for position, nucleotide in enumerate(sequence):
            if nucleotide not in profile_matrix:
                raise ValueError(
                    f"Nucleotide invalid: {nucleotide}"
                )

            profile_matrix[nucleotide][position] += 1

    # Construire la séquence consensus
    consensus = ""

    for position in range(sequence_length):
        nucleotide = max(
            "ACGT",
            key=lambda base: profile_matrix[base][position]
        )
        consensus += nucleotide

    # Affichage
    print(consensus)

    for nucleotide in "ACGT":
        values = " ".join(
            str(count)
            for count in profile_matrix[nucleotide]
        )
        print(f"{nucleotide}: {values}")


if __name__ == "__main__":
    consensus_and_profile()