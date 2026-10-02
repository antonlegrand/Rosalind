def dna (sequence : str  ) -> dict[str,int]:

    lettre_count: dict[str,int]= {
        "A":0,
        "C":0,
        "T":0,
        "G":0,
    }# dictionnaire 


    # boucle 

    for lettre in sequence:

        if lettre not in lettre_count:
            print("la lettre n'est pas un nucléotide")# error traitement
        else:
            lettre_count[lettre] += 1
    return lettre_count

print(dna("AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGAGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTG"))