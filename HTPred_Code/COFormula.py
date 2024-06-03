def andcfc(cc0, cc1):
    return min(cc0) + 1, sum(cc1) + 1


def nandcfc(cc0, cc1):
    return sum(cc1) + 1, min(cc0) + 1


def orcfc(cc0, cc1):
    return sum(cc0) + 1, min(cc1) + 1


def norcfc(cc0, cc1):
    return min(cc1) + 1, sum(cc0) + 1


def xorcfc(cc0, cc1):
    f_cc0 = min(cc0[0],cc1[0])
    f_cc1 = min(cc1[0],cc0[0])

    for i in range(1,len(cc0)):
        temp_cc0 = min(f_cc0 + cc0[i], f_cc1 + cc1[i])
        temp_cc1 = min(f_cc1 + cc0[i], f_cc0 + cc1[i])
        f_cc0 = temp_cc0
        f_cc1 = temp_cc1

    return f_cc0 + 1, f_cc1 + 1


def xnorcfc(cc0, cc1):
    f_cc0 = min(cc1[0], cc0[0])
    f_cc1 = min(cc0[0], cc1[0])

    for i in range(1, len(cc0)):
        temp_cc0 = min(f_cc1 + cc0[i], f_cc0 + cc1[i])
        temp_cc1 = min(f_cc0 + cc0[i], f_cc1 + cc1[i])
        f_cc0 = temp_cc0
        f_cc1 = temp_cc1

    return f_cc0 + 1, f_cc1 + 1


def notcfc(cc0, cc1):
    return cc1[0] + 1, cc0[0] + 1


def dffcfc(cc0, cc1):
    if len(cc0) > 1:
        if cc0[0] == 1 and cc1[0] == 1:
            return cc0[1], cc1[1]
        else:
            return cc0[0], cc1[0]

    return cc0[0], cc1[0]


def buffcfc(cc0, cc1):
    return cc0[0], cc1[0]


CC0CC1Functions = {'DFF': dffcfc,
                   'OR': orcfc,
                   'NOT': notcfc,
                   'AND': andcfc,
                   'NAND': nandcfc,
                   'NOR': norcfc,
                   'XOR': xorcfc,
                   'XNOR': xnorcfc,
                   'BUFF': buffcfc
                   }


def andsfc(sc0, sc1):
    return min(sc0), sum(sc1)


def nandsfc(sc0, sc1):
    return sum(sc1), min(sc0)


def orsfc(sc0, sc1):
    return sum(sc0), min(sc1)


def norsfc(sc0, sc1):
    return min(sc1), sum(sc0)


def xorsfc(sc0, sc1):
    f_sc0 = min(sc0[0], sc1[0])
    f_sc1 = min(sc1[0], sc0[0])

    for i in range(1, len(sc0)):
        temp_sc0 = min(f_sc0 + sc0[i], f_sc1 + sc1[i])
        temp_sc1 = min(f_sc1 + sc0[i], f_sc0 + sc1[i])
        f_sc0 = temp_sc0
        f_sc1 = temp_sc1

    return f_sc0, f_sc1


def xnorsfc(sc0, sc1):
    f_sc0 = min(sc1[0], sc0[0])
    f_sc1 = min(sc0[0], sc1[0])

    for i in range(1, len(sc0)):
        temp_sc0 = min(f_sc1 + sc0[i], f_sc0 + sc1[i])
        temp_sc1 = min(f_sc0 + sc0[i], f_sc1 + sc1[i])
        f_sc0 = temp_sc0
        f_sc1 = temp_sc1

    return f_sc0, f_sc1


def notsfc(sc0, sc1):
    return sc1[0], sc0[0]


def dffsfc(sc0, sc1):
    if len(sc0) > 1:
        if sc0[0] == 0 and sc1[0] == 0:
            return sc0[1] + 1, sc1[1] + 1
        else:
            return sc0[0] + 1, sc1[0] + 1

    return sc0[0] + 1, sc1[0] + 1


def buffsfc(sc0, sc1):
    return sc0[0] + 1, sc1[0] + 1


SC0SC1Functions = {'DFF': dffsfc,
                   'OR': orsfc,
                   'NOT': notsfc,
                   'AND': andsfc,
                   'NAND': nandsfc,
                   'NOR': norsfc,
                   'XOR': xorsfc,
                   'XNOR': xnorsfc,
                   'BUFF': buffsfc
                   }


def andcfo(cc0, cc1, co):
    r_co = []
    sum_cc1 = sum(cc1)
    sum_co = sum(co)
    for i in cc1:
        r_co.append(sum_co + sum_cc1 - i + 1)
    return r_co


def nandcfo(cc0, cc1, co):
    r_co = []
    sum_cc1 = sum(cc1)
    sum_co = sum(co)
    for i in cc1:
        r_co.append(sum_co + sum_cc1 - i + 1)
    return r_co


def orcfo(cc0, cc1, co):
    r_co = []
    sum_cc0 = sum(cc0)
    sum_co = sum(co)
    for i in cc0:
        r_co.append(sum_co + sum_cc0 - i + 1)
    return r_co


def norcfo(cc0, cc1, co):
    r_co = []
    sum_cc0 = sum(cc0)
    sum_co = sum(co)
    for i in cc0:
        r_co.append(sum_co + sum_cc0 - i + 1)
    return r_co


def __rec_xorcfo(cc0_array,cc1_array,sum_co):

    if len(cc0_array) == 2:
        return [sum_co + min(cc0_array[1], cc1_array[1]), [sum_co + min(cc0_array[0], cc1_array[0])] ]

    input_cc0 = [cc0_array.pop(0), cc0_array.pop(0)]
    input_cc1 = [cc1_array.pop(0), cc1_array.pop(0)]

    new_cc0_cc1 = CC0CC1Functions['XOR'](input_cc0,input_cc1)

    cc0_array.insert(0,new_cc0_cc1[0])
    cc1_array.insert(0,new_cc0_cc1[1])

    output_co = __rec_xorcfo(cc0_array,cc1_array,sum_co)

    sum_co = output_co[0]
    collected_co = output_co[1]

    collected_co.insert(0, sum_co + min(input_cc0[0], input_cc1[0]))

    return [ sum_co + min(input_cc0[1], input_cc1[1]) , collected_co]


def xorcfo(cc0, cc1, co):
    sum_co = sum(co)

    if len(cc0) == 2:
        return [sum_co + min(cc0[1], cc1[1]) + 1, sum_co + min(cc0[0], cc1[0]) + 1]

    else:
        initial_cc0_cc1 = CC0CC1Functions['XOR'](cc0[0:2],cc1[0:2])
        cc0_progressive_array = [initial_cc0_cc1[0]] + cc0[2:]
        cc1_progressive_array = [initial_cc0_cc1[1]] + cc1[2:]

        result = __rec_xorcfo(cc0_progressive_array,cc1_progressive_array,sum_co)
        sum_co = result[0]

        ret_l = [sum_co + min(cc0[1], cc1[1]), sum_co + min(cc0[0], cc1[0])] + result[1]

        for i in range(len(ret_l)):
            ret_l[i] += 1

        return ret_l


def xnorcfo(cc0, cc1, co):
    return xorcfo(cc0,cc1,co)


def notcfo(cc0, cc1, co):
    return [sum(co) + 1]


def dffcfo(cc0, cc1, co):
    return [sum(co)]


def buffcfo(cc0, cc1, co):
    return [sum(co)]


COFunctions = {'DFF': dffcfo,
               'OR': orcfo,
               'NOT': notcfo,
               'AND': andcfo,
               'NAND': nandcfo,
               'NOR': norcfo,
               'XOR': xorcfo,
               'XNOR': xnorcfo,
               'BUFF': buffcfo
               }


def andsfo(sc0, sc1, so):
    r_so = []
    sum_sc1 = sum(sc1)
    sum_so = sum(so)
    for i in sc1:
        r_so.append(sum_so + sum_sc1 - i)
    return r_so


def nandsfo(sc0, sc1, so):
    r_so = []
    sum_sc1 = sum(sc1)
    sum_so = sum(so)
    for i in sc1:
        r_so.append(sum_so + sum_sc1 - i)
    return r_so


def orsfo(sc0, sc1, so):
    r_so = []
    sum_sc0 = sum(sc0)
    sum_so = sum(so)
    for i in sc0:
        r_so.append(sum_so + sum_sc0 - i)
    return r_so


def norsfo(sc0, sc1, so):
    r_so = []
    sum_sc0 = sum(sc0)
    sum_so = sum(so)
    for i in sc0:
        r_so.append(sum_so + sum_sc0 - i)
    return r_so


def __rec_xorsfo(sc0_array,sc1_array,sum_so):

    if len(sc0_array) == 2:
        return [sum_so + min(sc0_array[1], sc1_array[1]), [sum_so + min(sc0_array[0], sc1_array[0])] ]

    input_sc0 = [sc0_array.pop(0), sc0_array.pop(0)]
    input_sc1 = [sc1_array.pop(0), sc1_array.pop(0)]

    new_sc0_sc1 = SC0SC1Functions['XOR'](input_sc0,input_sc1)

    sc0_array.insert(0,new_sc0_sc1[0])
    sc1_array.insert(0,new_sc0_sc1[1])

    output_so = __rec_xorsfo(sc0_array,sc1_array,sum_so)

    sum_so = output_so[0]
    collected_so = output_so[1]

    collected_so.insert(0, sum_so + min(input_sc0[0], input_sc1[0]))

    return [ sum_so + min(input_sc0[1], input_sc1[1]), collected_so]


def xorsfo(sc0, sc1, so):
    sum_so = sum(so)

    if len(sc0) == 2:
        return [sum_so + min(sc0[1], sc1[1]), sum_so + min(sc0[0], sc1[0])]

    else:
        initial_sc0_sc1 = SC0SC1Functions['XOR'](sc0[0:2], sc1[0:2])
        sc0_progressive_array = [initial_sc0_sc1[0]] + sc0[2:]
        sc1_progressive_array = [initial_sc0_sc1[1]] + sc1[2:]

        result = __rec_xorsfo(sc0_progressive_array, sc1_progressive_array, sum_so)
        sum_so = result[0]

        return [sum_so + min(sc0[1], sc1[1]), sum_so + min(sc0[0], sc1[0])] + result[1]


def xnorsfo(sc0, sc1, so):
    return xorsfo(sc0,sc1,so)


def notsfo(sc0, sc1, so):
    return [sum(so)]


def dffsfo(sc0, sc1, so):
    return [sum(so)+1]*len(sc0)


def buffsfo(sc0, sc1, so):
    return [sum(so)+1]


SOFunctions = {'DFF': dffsfo,
               'OR': orsfo,
               'NOT': notsfo,
               'AND': andsfo,
               'NAND': nandsfo,
               'NOR': norsfo,
               'XOR': xorsfo,
               'XNOR': xnorsfo,
               'BUFF': buffsfo
               }
