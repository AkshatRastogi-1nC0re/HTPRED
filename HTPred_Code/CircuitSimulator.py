import Logic
from Logic import LogicRules
import enum
import uuid

FLIPFLOP = {"DFF"}
uninvoked = set()


class FAN(enum.Enum):
    IN = 0
    OUT = 1


class CIRCUIT_TYPE(enum.Enum):
    COMBINATIONAL = 0
    SEQUENTIAL = 1


class Wire:
    id = None
    parent_module = None
    inputsidePins = None
    outputsidePins = None

    def __init__(self, id, parent_module):
        self.id = id
        self.parent_module = parent_module
        self.inputsidePins = []
        self.outputsidePins = []

    def getInputPins(self):
        return self.inputsidePins

    def getOutputPins(self):
        return self.outputsidePins

    def pushLogic(self, value_logic):
        for pin in self.outputsidePins:
            pin.setLogic(value_logic)
            if pin.parent_gate not in self.parent_module.gates_to_invoke_exclusion:
                self.parent_module.gates_to_invoke.append(pin.parent_gate)


class Gate:
    __id = None
    __g_type = None
    parent_module = None
    __inputpins = None
    __outputpins = None

    def __init__(self, inputwires, outputwires, parentmodule, type):
        self.__id = type+"_"+str(uuid.uuid4())
        self.__g_type = type
        self.parent_module = parentmodule
        self.__inputpins = []
        self.__outputpins = []

        for i in inputwires:
            apin = Pin(FAN.IN,self)
            self.__inputpins.append(apin)
            if isinstance(i,str):
                self.parent_module.setPin(i, apin)
            elif isinstance(i,Wire):
                apin.connect_wire(i)

        for i in outputwires:
            apin = Pin(FAN.OUT,self)
            self.__outputpins.append(apin)
            if isinstance(i,str):
                self.parent_module.setPin(i, apin)
            elif isinstance(i,Wire):
                apin.connect_wire(i)

    def getInputPins(self):
        return self.__inputpins

    def getOutputPins(self):
        return self.__outputpins

    def getID(self):
        return self.__id

    def getType(self):
        return self.__g_type

    def printGate(self):
        print("\tINPUTS: ",end='')
        for i in self.__inputpins:
            print(i, end=' ')
        print()
        print("\tOUTPUTS: ",end=' ')
        for i in self.__outputpins:
            print(i, end=' ')
        print()

    def invokeInput_to_Output(self):
        logic_list = []

        for t in self.__inputpins:
            logic_list.append(t.logic_value)

        oV = LogicRules.getResult(self.__g_type, logic_list)
        for m in self.__outputpins:
            if m.changed_logic_value > 2:
                self.parent_module.gates_to_invoke_exclusion.add(self)
            else:
                m.setLogic(oV[0])

        self.removeFromUninvoked()

    def removeFromUninvoked(self):
        if self in uninvoked:
            uninvoked.remove(self)

    def setOutputLogic(self,logic_value):
        for m in self.__outputpins:
            m.setLogic(logic_value)


class Pin:
    type = None
    parent_gate = None
    connected_wires = None

    logic_value = None
    changed_logic_value = None

    def __init__(self, type: FAN, parent_gate: Gate):
        self.type = type
        self.parent_gate = parent_gate
        self.connected_wires = dict()

        self.logic_value = Logic.LOGIC.X
        self.changed_logic_value = 0

    def connect_wire(self,wire: Wire):
        if self.type == FAN.IN:
            wire.outputsidePins.append(self)
        elif self.type == FAN.OUT:
            wire.inputsidePins.append(self)
        self.connected_wires[wire.id] = wire

    def setLogic(self, logic_value):
        if self.logic_value == logic_value:
            return
        self.logic_value = logic_value
        if self.type == FAN.OUT:
            for r in self.connected_wires.keys():
                self.connected_wires[r].pushLogic(logic_value)


class Module:
    __inputpins = None
    __outputpins = None
    __wires = None
    __gates = None

    flipflops = None
    circuit_type = None
    gates_to_invoke = None
    gates_to_invoke_exclusion = None
    max_version = None

    def __init__(self):
        self.__inputpins = dict()
        self.__outputpins = dict()
        self.__wires = dict()
        self.__gates = dict()
        self.__inputpins["VDD"] = set()
        self.__inputpins["GND"] = set()
        self.orderedInputs = []

        self.flipflops = set()
        self.gates_to_invoke = []
        self.gates_to_invoke_exclusion = set()

    def getWires(self):
        return self.__wires

    def getInputpins(self):
        return self.__inputpins

    def getOutputpins(self):
        return self.__outputpins

    def addInput(self,inp):
        self.orderedInputs.append(inp)
        self.__inputpins[inp] = set()

    def addOutput(self,outp):
        self.__outputpins[outp] = set()
        self.__wires[outp] = Wire(outp, self)

    def setPin(self,pinName,pin):
        if pinName in self.__inputpins.keys():
            self.__inputpins[pinName].add(pin)
        elif pinName in self.__outputpins.keys():
            self.__outputpins[pinName].add(pin)
            pin.connect_wire(self.__wires[pinName])

    def addgate(self,inputWires,outputWires,gatetype):
        inputWireObjects = []
        outputWireObjects = []

        for s in inputWires:
            if s in self.__inputpins.keys() or s in self.__outputpins.keys():
                inputWireObjects.append(s)
            else:
                if s not in self.__wires.keys():
                    self.__wires[s] = Wire(s,self)
                inputWireObjects.append(self.__wires[s])

        for s in outputWires:
            if s in self.__inputpins.keys() or s in self.__outputpins.keys():
                outputWireObjects.append(s)
            else:
                if s not in self.__wires.keys():
                    self.__wires[s] = Wire(s,self)
                outputWireObjects.append(self.__wires[s])

        agate = Gate(inputWireObjects,outputWireObjects,self,gatetype)
        self.__gates[agate.getID()] = agate
        if agate.getType() in FLIPFLOP:
            self.flipflops.add(agate)
        uninvoked.add(agate)

    def getgates(self):
        return self.__gates


class CircuitSimulator:
    input_file = None
    m = None
    final_data = None

    def __init__(self, input_file, inputs):
        self.input_file = input_file
        self.m = Module()
        self.__build()
        self.__startCalculation(inputs)

    def __getIOArg(self,inst):
        bopen = -1
        bclose = -1

        for i in range(len(inst)):
            if inst[i] == '(':
                bopen = i
            elif inst[i] == ')':
                bclose = i

        return inst[bopen+1:bclose].strip()

    def __getGateArg(self, inst):
        equal = -1
        bopen = -1
        bclose = -1

        for i in range(len(inst)):
            if inst[i] == '=':
                equal = i
            if inst[i] == '(':
                bopen = i
            elif inst[i] == ')':
                bclose = i

        inps = []
        for t in inst[bopen+1:bclose].split(','):
            inps.append(t.strip())

        outps = []
        for t in inst[0:equal].split(','):
            outps.append(t.strip())

        return inps, outps, inst[equal + 1: bopen].strip()

    def __build(self):
        file = open(self.input_file,'r')

        while True:
            t = file.readline()
            if t == "":
                break
            t = t.strip()
            if len(t) == 0 or t.startswith('#') or t.startswith("//"):
                continue

            if t.startswith("INPUT"):
                self.m.addInput(self.__getIOArg(t))

            elif t.startswith("OUTPUT"):
                self.m.addOutput(self.__getIOArg(t))

            else:
                rt = self.__getGateArg(t)
                self.m.addgate(rt[0],rt[1],rt[2])

        file.close()

        if len(self.m.flipflops) == 0:
            self.m.circuit_type = CIRCUIT_TYPE.COMBINATIONAL
        else:
            self.m.circuit_type = CIRCUIT_TYPE.SEQUENTIAL

    def __assign_logic_non_connected_pin(self):
        # Wires which doesnt connect to input or output, assigning default values to associated pins
        for i in self.m.getWires():
            w = self.m.getWires()[i]
            if len(w.inputsidePins) == 0:
                w.pushLogic(Logic.LOGIC.ZERO)


    def __assign_logic_pseudo_io(self):
        # Assigning values to pseudo input and pseudo outout for flipflops
        for flipflop in self.m.flipflops:
            flipflop.setOutputLogic(Logic.LOGIC.ZERO)

    def __assign_inputlogic_input_pin(self,logic_list):
        for i in self.m.getInputpins().keys():
            for pin in self.m.getInputpins()[i]:
                pin.setLogic(logic_list[i])
                pin.parent_gate.invokeInput_to_Output()

    def __clear_invoke_gates(self):
        self.m.gates_to_invoke.clear()
        self.m.gates_to_invoke_exclusion.clear()

    def __startCalculation(self, logic_list):

        if len(logic_list) != len(self.m.orderedInputs):
            raise Exception('No. of inputs doesnt match input pattern')

        self.__assign_logic_non_connected_pin()
        self.__assign_logic_pseudo_io()

        inputlogicdict = dict()
        for i in range(len(logic_list)):
            assign = None
            if logic_list[i] == '1':
                assign = Logic.LOGIC.ONE
            elif logic_list[i] == '0':
                assign = Logic.LOGIC.ZERO
            else:
                assign = Logic.LOGIC.X

            inputlogicdict[self.m.orderedInputs[i]] = assign

        self.__assign_inputlogic_input_pin(inputlogicdict)

        while len(self.m.gates_to_invoke) != 0:
            gate = self.m.gates_to_invoke.pop(0)
            gate.invokeInput_to_Output()
        self.__clear_invoke_gates()

        uninvoked.clear()

    def result(self):

        data = dict()

        for input_pin in self.m.getInputpins().keys():
            pins = self.m.getInputpins()[input_pin]
            for pin in pins:
                data[input_pin] = pin.logic_value

        for wireL in self.m.getWires():
            wire = self.m.getWires()[wireL]
            for pin in wire.getInputPins():
                data[wireL] = pin.logic_value

        return data

