import enum
import uuid
import InputPatternRules
from Logic import LOGIC

uninvoked = []

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

    def __init__(self,id,parent_module):
        self.id = id
        self.parent_module = parent_module
        self.inputsidePins = []
        self.outputsidePins = []

    def getInputPins(self):
        return self.inputsidePins

    def getOutputPins(self):
        return self.outputsidePins

    def setELogic(self,for_output,e_logic):
        for pin in self.inputsidePins:
            pin.setELogic(for_output,e_logic)


class Gate:
    __id = None
    __g_type = None
    parent_module = None
    __inputpins = None
    __outputpins = None

    def __init__(self,inputwires, outputwires, parentmodule, type):
        self.__id = type+"_"+str(uuid.uuid4())
        self.__g_type = type
        self.parent_module = parentmodule
        self.__inputpins = []
        self.__outputpins = []

        for i in inputwires:
            apin = Pin(FAN.IN,self)
            self.__inputpins.append(apin)
            if isinstance(i,str):
                self.parent_module.setPin(i,apin)
            elif isinstance(i,Wire):
                apin.connect_wire(i)

        for i in outputwires:
            apin = Pin(FAN.OUT,self)
            self.__outputpins.append(apin)
            if isinstance(i,str):
                self.parent_module.setPin(i,apin)
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


class Pin:
    type = None
    parent_gate = None
    connected_wires = None

    e_logic = None

    def __init__(self,type: FAN,parent_gate: Gate):
        self.type = type
        self.parent_gate = parent_gate
        self.connected_wires = dict()

    def connect_wire(self,wire: Wire):
        if self.type == FAN.IN:
            wire.outputsidePins.append(self)
        elif self.type == FAN.OUT:
            wire.inputsidePins.append(self)
        self.connected_wires[wire.id] = wire

    def setELogic(self,for_output,e_logic):
        self.e_logic[for_output] = e_logic

        if self.type == FAN.IN:
            for wire_key in self.connected_wires.keys():
                wire = self.connected_wires[wire_key]
                wire.setELogic(for_output,e_logic)
        elif self.type == FAN.OUT:
            uninvoked.append(self.parent_gate)

    def get_e_logic(self):
        return self.e_logic


class Module:
    __inputpins = None
    __outputpins = None
    __wires = None
    __gates = None

    def __init__(self):
        self.__inputpins = dict()
        self.__outputpins = dict()
        self.__wires = dict()
        self.__gates = dict()
        self.__inputpins["VDD"] = set()
        self.__inputpins["GND"] = set()

    def getWires(self):
        return self.__wires

    def getInputpins(self):
        return self.__inputpins

    def getOutputpins(self):
        return self.__outputpins

    def addInput(self,inp):
        self.__inputpins[inp] = set()

    def addOutput(self,outp):
        self.__outputpins[outp] = set()
        self.__wires[outp] = Wire(outp,self)

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

    def getgates(self):
        return self.__gates

    def createLogicArrays(self,module_outputPins):
        for gate in self.__gates.values():

            for inputpin in gate.getInputPins():
                inputpin.e_logic = dict()
                for moP in module_outputPins:
                    inputpin.e_logic[moP] = LOGIC.X

            for outputpin in gate.getOutputPins():
                outputpin.e_logic = dict()
                for moP in module_outputPins:
                    outputpin.e_logic[moP] = LOGIC.X


class TestPatternGenerator:
    InputPatternRules.LOGIC = LOGIC

    input_file = None
    m = None
    final_data = None

    orderedOutputs = None

    def __init__(self,input_file):
        self.input_file = input_file
        self.orderedOutputs = []
        self.m = Module()
        self.__build()

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
                o = self.__getIOArg(t)
                self.m.addOutput(o)
                self.orderedOutputs.append(o)

            else:
                rt = self.__getGateArg(t)
                self.m.addgate(rt[0],rt[1],rt[2])

        file.close()

    def generatePattern(self,output):
        if len(output) != len(self.m.getOutputpins()):
            raise Exception("No. of expected outputs don't match no. of output pins")

        self.m.createLogicArrays(list(self.m.getOutputpins().keys()))

        for i in range(len(output)):
            for oP in (self.m.getOutputpins()[self.orderedOutputs[i]]):
                logic = None
                if output[i] == '1':
                    logic = LOGIC.ONE
                elif output[i] == '0':
                    logic = LOGIC.ZERO
                elif output[i] == 'X':
                    logic = LOGIC.X
                oP.e_logic[self.orderedOutputs[i]] = logic

        for outputPin in self.m.getOutputpins().keys():
            uninvoked.clear()
            outputPinSet = self.m.getOutputpins()[outputPin]
            for output in outputPinSet:
                uninvoked.append(output.parent_gate)
            self.__invoke(outputPin)

    def __invoke(self,for_output):
        while len(uninvoked) > 0:
            gate = uninvoked.pop(0)
            self.__process(gate,for_output)

    def __process(self, gate,for_output):
        expected_output_logic = gate.getOutputPins()[0].e_logic[for_output]
        expected_input_logic = []
        for inputPin in gate.getInputPins():
            expected_input_logic.append(inputPin.e_logic[for_output])

        expected_input_logic, requiresChange = InputPatternRules.get_input_logic(expected_input_logic,expected_output_logic,gate.getType())

        if not requiresChange:
            return

        for inputPinIndex in range(len(gate.getInputPins())):
            inputPin = gate.getInputPins()[inputPinIndex]
            inputPin.setELogic(for_output,expected_input_logic[inputPinIndex])

    def getResult(self):
        data = dict()
        for key in self.m.getInputpins().keys():
            if key == 'VDD' or key == 'GND':
                continue
            data[key] = []
            for pin in self.m.getInputpins()[key]:
                data[key].append(pin.get_e_logic())

        return data

    def getFormalResult(self):
        data = self.getResult()
        newdata = dict()
        for op in data.keys():
            rset = set()
            for opk in data[op]:
                for value in opk.values():
                    if value == LOGIC.ONE:
                        rset.add('1')
                    if value == LOGIC.ZERO:
                        rset.add('0')
            newdata[op] = rset
        return newdata




