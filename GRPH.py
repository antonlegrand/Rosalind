"""
A graph whose nodes have all been labeled can be represented by an adjacency list, in which each row of the list contains the two node labels corresponding to a unique edge.

A directed graph (or digraph) is a graph containing directed edges, each of which has an orientation. That is, a directed edge is represented by an arrow instead of a line segment; the starting and ending nodes of an edge form its tail and head, respectively. The directed edge with tail v
 and head w
 is represented by (v,w)
 (but not by (w,v)
). A directed loop is a directed edge of the form (v,v)
.

For a collection of strings and a positive integer k
, the overlap graph for the strings is a directed graph Ok
 in which each string is represented by a node, and string s
 is connected to string t
 with a directed edge when there is a length k
 suffix of s
 that matches a length k
 prefix of t
, as long as s≠t
; we demand s≠t
 to prevent directed loops in the overlap graph (although directed cycles may be present).

Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.

Return: The adjacency list corresponding to O3
. You may return edges in any order.
Sample Dataset
>Rosalind_0498
AAATAAA
>Rosalind_2391
AAATTTT
>Rosalind_2323
TTTTCCC
>Rosalind_0442
AAATCCC
>Rosalind_5013
GGGTGGG
""" 
from collections import defaultdict

def overlap_graph() -> None:
    # Sample dataset
    sample_data = """>Rosalind_0498
AAATAAA
>Rosalind_2391
AAATTTT
>Rosalind_2323
TTTTCCC
>Rosalind_0442
AAATCCC
>Rosalind_5013
GGGTGGG
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
                current_label = line[1:]  # on enlève le ">"
                current_sequence = ""
            else:
                current_sequence += line
        if current_label:
            sequences[current_label] = current_sequence

    adjacency_list = defaultdict(list)

    for label1, seq1 in sequences.items():
        suffix = seq1[-3:]
        for label2, seq2 in sequences.items():
            if label1 != label2 and seq2.startswith(suffix):
                adjacency_list[label1].append(label2)

    for label, neighbors in adjacency_list.items():
        for neighbor in neighbors:
            print(f"{label} {neighbor}")


if __name__ == "__main__":
    overlap_graph()


