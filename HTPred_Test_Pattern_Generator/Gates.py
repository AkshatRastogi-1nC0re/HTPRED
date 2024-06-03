# All types of Fundamental Devices. -> AND OR NOT XOR NOR NAND DFF
import enum
import uuid


class FAN(enum.Enum):
    IN = 0
    OUT = 1


class Port:
    __fan = None
    __parent_gate = None
    __uniqueID = None
    __connected_wire = None

    def __init__(self, fan: FAN, parent_gate):
        self.__fan = fan
        self.__parent_gate = parent_gate
        self.__uniqueID = uuid.uuid4()

    def get_fan(self):
        return self.__fan

    def get_parent_gate(self):
        return self.__parent_gate

    def set_parent_gate(self, parent_gate):
        self.__parent_gate = parent_gate

    def get_unique_id(self) -> uuid.UUID:
        return self.__uniqueID

    def connect_wire(self, wire) -> None:
        self.__connected_wire = wire

    def get_connected_wire(self):
        return self.__connected_wire


class Gate:
    _inputPins = None
    _outputPins = None
    _uniqueID = None
    _gateName = None
    _gateType = None

    def __init__(self, gate_name):
        self._gateName = gate_name
        self.__uniqueID = uuid.uuid4()

    def get_inputs(self) -> dict:
        return self._inputPins

    def get_outputs(self) -> dict:
        return self._outputPins

    def get_name(self) -> str:
        return self._gateName

    def get_type(self) -> str:
        return self._gateType

    def get_unique_id(self) -> uuid.UUID:
        return self.__uniqueID


# The following are different gates :

class ANDGate(Gate):
    def __init__(self, gate_name, module_arg):
        super().__init__(gate_name)
        self._inputPins = dict()
        for i in range(len(module_arg) - 1):
            self._inputPins[module_arg[i]] = [Port(FAN.IN, self)]
        self._outputPins = {module_arg[len(module_arg) - 1]: [Port(FAN.OUT, self)]}
        self._gateType = 'AND'

    def operate(self):
        pass


class ORGate(Gate):
    def __init__(self, gate_name, module_arg):
        super().__init__(gate_name)
        self._inputPins = dict()
        for i in range(len(module_arg) - 1):
            self._inputPins[module_arg[i]] = [Port(FAN.IN, self)]
        self._outputPins = {module_arg[len(module_arg) - 1]: [Port(FAN.OUT, self)]}
        self._gateType = 'OR'

    def operate(self):
        pass


class NOTGate(Gate):
    def __init__(self, gate_name, module_arg):
        super().__init__(gate_name)
        self._inputPins = dict()
        for i in range(len(module_arg) - 1):
            self._inputPins[module_arg[i]] = [Port(FAN.IN, self)]
        self._outputPins = {module_arg[len(module_arg) - 1]: [Port(FAN.OUT, self)]}
        self._gateType = 'NOT'

    def operate(self):
        pass


class XORGate(Gate):
    def __init__(self, gate_name, module_arg):
        super().__init__(gate_name)
        self._inputPins = dict()
        for i in range(len(module_arg) - 1):
            self._inputPins[module_arg[i]] = [Port(FAN.IN, self)]
        self._outputPins = {module_arg[len(module_arg) - 1]: [Port(FAN.OUT, self)]}
        self._gateType = 'XOR'

    def operate(self):
        pass


class NANDGate(Gate):
    def __init__(self, gate_name, module_arg):
        super().__init__(gate_name)
        self._inputPins = dict()
        for i in range(len(module_arg) - 1):
            self._inputPins[module_arg[i]] = [Port(FAN.IN, self)]
        self._outputPins = {module_arg[len(module_arg) - 1]: [Port(FAN.OUT, self)]}
        self._gateType = 'NAND'

    def operate(self):
        pass


class NORGate(Gate):
    def __init__(self, gate_name, module_arg):
        super().__init__(gate_name)
        self._inputPins = dict()
        for i in range(len(module_arg) - 1):
            self._inputPins[module_arg[i]] = [Port(FAN.IN, self)]
        self._outputPins = {module_arg[len(module_arg) - 1]: [Port(FAN.OUT, self)]}
        self._gateType = 'NOR'

    def operate(self):
        pass


class XNORGate(Gate):
    def __init__(self, gate_name, module_arg):
        super().__init__(gate_name)
        self._inputPins = dict()
        for i in range(len(module_arg) - 1):
            self._inputPins[module_arg[i]] = [Port(FAN.IN, self)]
        self._outputPins = {module_arg[len(module_arg) - 1]: [Port(FAN.OUT, self)]}
        self._gateType = 'XNOR'

    def operate(self):
        pass


class DFF(Gate):
    def __init__(self, gate_name, module_arg):
        super().__init__(gate_name)
        self._inputPins = dict()
        for i in range(len(module_arg) - 1):
            self._inputPins[module_arg[i]] = [Port(FAN.IN, self)]
        self._outputPins = {module_arg[len(module_arg) - 1]: [Port(FAN.OUT, self)]}
        self._gateType = 'DFF'

    def operate(self):
        pass


class BUFF(Gate):
    def __init__(self, gate_name, module_arg):
        super().__init__(gate_name)
        self._inputPins = dict()
        for i in range(len(module_arg) - 1):
            self._inputPins[module_arg[i]] = [Port(FAN.IN, self)]
        self._outputPins = {module_arg[len(module_arg) - 1]: [Port(FAN.OUT, self)]}
        self._gateType = 'BUFF'

    def operate(self):
        pass


class CUSTOM(Gate):
    def __init__(self, gate_type, gate_name, module_arg):
        super().__init__(gate_name)
        self._inputPins = dict()
        for i in range(len(module_arg) - 1):
            self._inputPins[module_arg[i]] = [Port(FAN.IN, self)]
        self._outputPins = {module_arg[len(module_arg) - 1]: [Port(FAN.OUT, self)]}
        self._gateType = gate_type

    def operate(self):
        pass


def getCustomGate(gate_type, gate_name, module_arg):
    return CUSTOM(gate_type,gate_name,module_arg)

