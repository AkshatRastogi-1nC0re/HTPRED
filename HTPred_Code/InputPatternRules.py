from Logic import LOGIC

class Gate:

    @staticmethod
    def for0(input_logic):
        raise NotImplementedError("Not implemented")

    @staticmethod
    def for1(input_logic):
        raise NotImplementedError("Not implemented")

    @classmethod
    def get_input_logic(cls, output_logic, input_logic):
        if output_logic == LOGIC.ONE:
            return cls.for1(input_logic), True
        elif output_logic == LOGIC.ZERO:
            return cls.for0(input_logic), True
        else:
            return output_logic, False


class AND(Gate):

    @staticmethod
    def for0(input_logic):
        if LOGIC.ZERO in input_logic:
            return input_logic

        elif LOGIC.X in input_logic:
            for i in range(len(input_logic)):
                if input_logic[i] == LOGIC.X:
                    input_logic[i] = LOGIC.ZERO
            return input_logic

        else:
            new_input_logic = []
            for i in input_logic:
                new_input_logic.append(LOGIC.ZERO)
            return new_input_logic


    @staticmethod
    def for1(input_logic):
        new_input_logic = []
        for i in input_logic:
            new_input_logic.append(LOGIC.ONE)
        return new_input_logic


class OR(Gate):

    @staticmethod
    def for0(input_logic):
        new_input_logic = []
        for i in input_logic:
            new_input_logic.append(LOGIC.ZERO)
        return new_input_logic

    @staticmethod
    def for1(input_logic):
        if LOGIC.ONE in input_logic:
            return input_logic

        elif LOGIC.X in input_logic:
            for i in range(len(input_logic)):
                if input_logic[i] == LOGIC.X:
                    input_logic[i] = LOGIC.ONE
            return input_logic

        else:
            new_input_logic = []
            for i in input_logic:
                new_input_logic.append(LOGIC.ONE)
            return new_input_logic


class NOT(Gate):

    @staticmethod
    def for0(input_logic):
        return [LOGIC.ONE]

    @staticmethod
    def for1(input_logic):
        return [LOGIC.ZERO]


class NAND(Gate):

    @staticmethod
    def for0(input_logic):
        return AND.for1(input_logic)

    @staticmethod
    def for1(input_logic):
        return AND.for0(input_logic)


class NOR(Gate):

    @staticmethod
    def for0(input_logic):
        return OR.for1(input_logic)

    @staticmethod
    def for1(input_logic):
        return OR.for0(input_logic)


class DFF(Gate):

    @staticmethod
    def for0(input_logic):
        return [LOGIC.ZERO]*len(input_logic)

    @staticmethod
    def for1(input_logic):
        return [LOGIC.ONE]*len(input_logic)


class BUFF(Gate):
    @staticmethod
    def for0(input_logic):
        return [LOGIC.ZERO]

    @staticmethod
    def for1(input_logic):
        return [LOGIC.ONE]


class XOR(Gate):
    @staticmethod
    def for0(input_logic):
        ones = 0
        for i in input_logic:
            if i == LOGIC.ONE:
                ones += 1

        if ones % 2 == 0:
            return input_logic

        if LOGIC.X in input_logic:
            for i in range(len(input_logic)):
                if input_logic[i] == LOGIC.X:
                    input_logic[i] = LOGIC.ONE
            return input_logic

    @staticmethod
    def for1(input_logic):
        ones = 0
        for i in input_logic:
            if i == LOGIC.ONE:
                ones += 1

        if ones % 2 == 1:
            return input_logic

        if LOGIC.X in input_logic:
            for i in range(len(input_logic)):
                if input_logic[i] == LOGIC.X:
                    input_logic[i] = LOGIC.ONE
            return input_logic


class XNOR(Gate):

    @staticmethod
    def for0(input_logic):
        return XOR.for1(input_logic)

    @staticmethod
    def for1(input_logic):
        return XOR.for0(input_logic)


gatemap = {"AND":AND,
           "OR":OR,
           "NOT":NOT,
           "NAND":NAND,
           "NOR":NOR,
           "DFF":DFF,
           "XOR":XOR,
           "XNOR":XNOR,
           "BUFF":BUFF}


def get_input_logic(expected_input_logic,expected_output_logic,gate_type):

    return gatemap[gate_type].get_input_logic(expected_output_logic,expected_input_logic)
