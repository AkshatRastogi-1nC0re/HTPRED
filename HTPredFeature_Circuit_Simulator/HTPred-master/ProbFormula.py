def andf(inp_prob1):
    t = 1
    for i in inp_prob1:
        t *= i
    return t


def orf(inp_prob1):
    t = 1
    for i in inp_prob1:
        t *= (1-i)
    return 1-t


def nandf(inp_prob1):
    return notf([andf(inp_prob1)])


def norf(inp_prob1):
    return notf([orf(inp_prob1)])


def bufff(inp_prob1):
    return inp_prob1[0]


def dfff(inp_prob1):
    return inp_prob1[0]


def notf(inp_prob1):
    return 1-inp_prob1[0]


def __rec_xorf(inp_prob1):
    x = inp_prob1[0]
    y = inp_prob1[1]

    return orf( [ x * (1-y) , y * (1-x) ] )


def xorf(inp_prob1):
    ret_v = __rec_xorf( [ inp_prob1[0], inp_prob1[1] ] )
    for i in range(2,len(inp_prob1)):
        ret_v = __rec_xorf( [ ret_v, inp_prob1[i] ] )

    return ret_v


def xnorf(inp_prob1):
    return notf( [ xorf(inp_prob1) ] )


ProbFunctions = {'DFF': dfff,
                 'OR': orf,
                 'NOT': notf,
                 'AND': andf,
                 'NAND': nandf,
                 'NOR': norf,
                 'XOR': xorf,
                 'XNOR': xnorf,
                 'BUFF': bufff
               }
