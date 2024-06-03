import enum


class LOGIC(enum.Enum):
    ZERO = 0
    ONE = 1
    X = 2


class LogicRules:

    @staticmethod
    def andF(values):
        if LOGIC.ZERO in values:
            return [LOGIC.ZERO]
        elif LOGIC.X not in values:
            return [LOGIC.ONE]
        else:
            return [LOGIC.X]

    @staticmethod
    def orF(values):
        if LOGIC.ONE in values:
            return [LOGIC.ONE]
        elif LOGIC.X not in values:
            return [LOGIC.ZERO]
        else:
            return [LOGIC.X]

    @staticmethod
    def notF(values):
        if LOGIC.ONE in values:
            return [LOGIC.ZERO]
        elif LOGIC.ZERO in values:
            return [LOGIC.ONE]
        else:
            return [LOGIC.X]

    @staticmethod
    def nandF(values):
        return LogicRules.notF(LogicRules.andF(values))

    @staticmethod
    def norF(values):
        return LogicRules.notF(LogicRules.orF(values))

    @staticmethod
    def xorF(values):
        if LOGIC.X not in values:
            one_count = 0
            for i in values:
                if i == LOGIC.ONE:
                    one_count += 1
            if one_count % 2 == 0:
                return [LOGIC.ZERO]
            else:
                return [LOGIC.ONE]
        else:
            return [LOGIC.X]

    @staticmethod
    def xnorF(values):
        return LogicRules.notF(LogicRules.xorF(values))

    @staticmethod
    def dffF(values):
        return values

    @staticmethod
    def buffF(values):
        return values

    @staticmethod
    def getResult(gate, values):
        gatemap = {"AND": LogicRules.andF,
                   "OR": LogicRules.orF,
                   "NOT": LogicRules.notF,
                   "NAND": LogicRules.nandF,
                   "NOR": LogicRules.norF,
                   "DFF": LogicRules.dffF,
                   "XOR": LogicRules.xorF,
                   "XNOR": LogicRules.xnorF,
                   "BUFF": LogicRules.buffF}

        return gatemap.get(gate)(values)

