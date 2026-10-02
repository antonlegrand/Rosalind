def revc(sequence:str)-> str: 

    revc =""

    for lettre in sequence:
        if lettre == "A":
            revc += "C"
        elif lettre == "T":
            revc += "G"
        elif lettre == "C":
            revc += "A"
        elif lettre == "G":
            revc += "T"
    return revc

print(revc("GATGGAACTTGACTACGTAAATT"))