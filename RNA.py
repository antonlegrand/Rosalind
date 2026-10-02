def rna(sequence:str) -> str:


    rna =""

    for lettre in sequence:
        if lettre == "T":
            rna += "U"
        else:
            rna += lettre

    return rna


print(rna("GATGGAACTTGACTACGTAAATT"))