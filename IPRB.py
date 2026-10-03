def iprb(k : int, m:int, n:int )-> float: 

    total = k + m+ n
    nb_total_pairs = total* (total-1)

    dominant = (k * (k-1)+ 2*k*(m+n)+0.75*m*(m-1)+m+n)

    return dominant/nb_total_pairs

print(iprb(2,2,2))