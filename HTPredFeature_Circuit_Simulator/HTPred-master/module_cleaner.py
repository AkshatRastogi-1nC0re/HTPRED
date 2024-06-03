class output_gate:
    outp = None
    gname = None
    inp = None

    def __init__(self):
        self.inp = []

    def addi(self,wi):
        return self.inp.append(wi)

    def seto(self,o):
        self.outp = o

    def setgate(self,gate):
        self.gname = gate

    def geti(self):
        return self.inp

    def geto(self):
        return self.outp


class module_cleaner:

    __usages = None
    __output_gates = None

    def __init__(self):
        self.__usages = dict()
        self.__output_gates = dict()

    def post_gate(self,outpg):
        non_used = dict()

        for i in outpg.geti():
            if i in self.__usages:
                self.__usages[i] += 1
            else:
                self.__usages[i] = 1
            if outpg.geto() == '!UNCONNECTED':
                if i in non_used:
                    non_used[i] += 1
                else:
                    non_used[i] = 1
            else:
                self.__output_gates[outpg.geto()] = outpg

        for nu in non_used.keys():
            self.__usages[nu] -= non_used[nu]

    def clear(self):
        to_del = []
        for i in self.__usages.keys():
            if self.__usages[i] == 0:
                to_del.append(i)
        self.__rec_del(to_del)

    def __rec_del(self,list_del):
        if len(list_del) == 0:
            return
        new_list_del = []
        for i in list_del:
            if i not in self.__output_gates:
                continue
            for m in self.__output_gates[i].geti():
                self.__usages[m] -= 1
                if self.__usages[m] == 0:
                    new_list_del.append(m)

        for i in list_del:
            if i in self.__output_gates:
                del self.__output_gates[i]

        self.__rec_del(new_list_del)

    def get_outp_text(self):
        outp = str()
        for m in self.__output_gates.keys():
            t = self.__output_gates[m]
            outp += t.outp + ' = ' + t.gname + '('
            for j in t.inp:
                outp += j
                if j is not t.inp[len(t.inp)-1]:
                    outp += ','
            outp += ')\n'
        return outp









