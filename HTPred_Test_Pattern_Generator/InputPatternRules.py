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
        flag = 0
        # print("AND for0", input_logic)
        if input_logic[0] == LOGIC.X and input_logic[1] == LOGIC.X:
            return [LOGIC.ZERO, LOGIC.ZERO]
        for el in input_logic:
            if el == LOGIC.ZERO:
                return input_logic
            else:
                flag = 1
        if flag == 1:
            input_logic[0] = 1
            return input_logic

    @staticmethod
    def for1(input_logic):
        flag = 0
        new_input_logic = [LOGIC.ONE for x in range(len(input_logic))]
        # print("AND for1", input_logic)
        if input_logic[0] == LOGIC.X and input_logic[1] == LOGIC.X:
            return [LOGIC.ONE, LOGIC.ONE]
        for el in input_logic:
            if el == LOGIC.ZERO:
                return new_input_logic
            else:
                flag = 1
        if flag == 1:
            return input_logic


class OR(Gate):

    @staticmethod
    def for0(input_logic):
        flag = 0
        new_input_logic = [LOGIC.ZERO for x in range(len(input_logic))]
        # print("OR for0", input_logic)
        if input_logic[0] == LOGIC.X and input_logic[1] == LOGIC.X:
            return [LOGIC.ZERO, LOGIC.ZERO]
        for el in input_logic:
            if el == LOGIC.ONE:
                return new_input_logic
            else:
                flag = 1
        if flag == 1:
            return input_logic

    @staticmethod
    def for1(input_logic):
        flag = 0
        # print("OR for1", input_logic)
        if input_logic[0] == LOGIC.X and input_logic[1] == LOGIC.X:
            return [LOGIC.ONE, LOGIC.ZERO]
        for el in input_logic:
            if el == LOGIC.ONE:
                return input_logic
            else:
                flag = 1
        if flag == 1:
            input_logic[0] = 1
            return input_logic


class NOT(Gate):

    @staticmethod
    def for0(input_logic):
        # print("NOT for0", input_logic)
        if input_logic[0] == LOGIC.X:
            return [LOGIC.ONE]
        if input_logic[0] == LOGIC.ONE:
            return input_logic
        else:
            input_logic[0] = LOGIC.ONE
            return input_logic

    @staticmethod
    def for1(input_logic):
        # print("NOT for1", input_logic)
        if input_logic[0] == LOGIC.X:
            return [LOGIC.ZERO]
        if input_logic[0] == LOGIC.ZERO:
            return input_logic
        else:
            input_logic[0] = LOGIC.ZERO
            return input_logic


class NAND(Gate):

    @staticmethod
    def for0(input_logic):
        flag = 0
        new_input_logic = [LOGIC.ONE for x in range(len(input_logic))]
        # print("NANDGATE", input_logic)
        if input_logic[0] == LOGIC.X and input_logic[1] == LOGIC.X:
            return [LOGIC.ONE, LOGIC.ONE]
        for el in input_logic:
            if el == LOGIC.ZERO:
                return new_input_logic
            else:
                flag = 1
        if flag == 1:
            return input_logic

    @staticmethod
    def for1(input_logic):
        # print("NANDGATE", input_logic)
        if input_logic[0] == LOGIC.X and input_logic[1] == LOGIC.X:
            return [LOGIC.ZERO, LOGIC.ONE]
        for el in input_logic:
            if el == LOGIC.ZERO:
                return input_logic
            else:
                flag = 1
        if flag == 1:
            input_logic[0] = LOGIC.ZERO
            return input_logic


class NOR(Gate):

    @staticmethod
    def for0(input_logic):
        flag = 0
        # print("NOR", input_logic)
        for el in input_logic:
            if el == LOGIC.ONE:
                return input_logic
            else:
                flag = 1
        if flag == 1:
            input_logic[0] = LOGIC.ONE
            return input_logic

    @staticmethod
    def for1(input_logic):
        flag = 0
        # print("NOR", input_logic)
        new_input_logic = [LOGIC.ZERO for x in range(len(input_logic))]
        for el in input_logic:
            if el == LOGIC.ONE:
                return new_input_logic
            else:
                flag = 1
        if flag == 1:
            return input_logic


class BUFF(Gate):

    @staticmethod
    def for0(input_logic):
        return [LOGIC.ZERO]

    @staticmethod
    def for1(input_logic):
        return [LOGIC.ONE]


gatemap = {"AND": AND,
           "OR": OR,
           "NOT": NOT,
           "NAND": NAND,
           "NOR": NOR,
           "BUFF": BUFF}


def get_input_logic(expected_input_logic, expected_output_logic, gate_type):
    r = gatemap[gate_type].get_input_logic(expected_output_logic, expected_input_logic)
    # print(r)
    return r
