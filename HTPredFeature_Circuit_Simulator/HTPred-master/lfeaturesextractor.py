

def Obth(L, CO_list):
    highco = max(CO_list)
    return (highco - ((highco * L)/100))

def getLfeatures(co_list):

    listx = []

    for i in range(0,101,5):
        listx.append(Obth(i, co_list))

    return listx