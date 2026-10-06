def subs(str1 : str , sequence : str ) -> list[int]:


    """
    1 string 
    1 sequence à retrouver 
    Position du début de séquence à redonner 
    si lettre in str = 1 seq , alors tchecker 2, 3 ,4 
    si 
    """
    positions :list[int] =[] #list
    n =len(str1)             # taille de la phrase
    k = len(sequence)        # taille de la séquence


    for i in range (n-k+1):  # 


        if str1[i:i+k] == sequence:
                positions.append(i+1)

    return positions


print(subs("GATATATGCATATACTT","ATAT"))