def hamm(str1 : str , str2 : str)-> int:

    """
    Chaine de caractères 
    Par position comparer les lettres , si non identiques 
    incrémenter de 1 le compteur 
    initaliser un compteur 

    """

    compteur = 0 

    for i in range(len(str1)):
        if str1[i] != str2[i]:
                compteur += 1

    return compteur

print(hamm("GAGCCTACTAACGGGAT","CATCGTAATGACGGCCT"))
