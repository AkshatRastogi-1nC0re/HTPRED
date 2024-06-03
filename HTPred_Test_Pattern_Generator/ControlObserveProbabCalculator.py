import COFormula
import csv
import ProbFormula
import enum
import uuid

FLIPFLOP = {"DFF"}
uninvoked = set()

RATIO_VERSION_BY_CIRCUIT_SIZE = 1
MAX_VERSION = 5
INF = 999999999


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

    def pushCC0CC1(self, valueCC0, valueCC1):
        for pin in self.outputsidePins:
            pin.setCC0CC1(valueCC0,valueCC1)
            if pin.parent_gate not in self.parent_module.gates_to_invoke_exclusion:
                self.parent_module.gates_to_invoke.append(pin.parent_gate)

    def pushSC0SC1(self, valueSC0, valueSC1):
        for pin in self.outputsidePins:
            pin.setSC0SC1(valueSC0,valueSC1)
            if pin.parent_gate not in self.parent_module.gates_to_invoke_exclusion:
                self.parent_module.gates_to_invoke.append(pin.parent_gate)

    def pushCO(self,valueCO):
        for pin in self.inputsidePins:
            pin.setCO(valueCO)
            if pin.parent_gate not in self.parent_module.gates_to_invoke_exclusion:
                self.parent_module.gates_to_invoke.append(pin.parent_gate)

    def pushSO(self,valueSO):
        for pin in self.inputsidePins:
            pin.setSO(valueSO)
            if pin.parent_gate not in self.parent_module.gates_to_invoke_exclusion:
                self.parent_module.gates_to_invoke.append(pin.parent_gate)

    def pushProb(self, value_prob1):
        for pin in self.outputsidePins:
            pin.setProb(value_prob1)
            if pin.parent_gate not in self.parent_module.gates_to_invoke_exclusion:
                self.parent_module.gates_to_invoke.append(pin.parent_gate)


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

    def invokeInput_to_Output(self, circuit_type):
        cc0 = []
        cc1 = []
        sc0 = []
        sc1 = []

        if circuit_type == CIRCUIT_TYPE.COMBINATIONAL:
            for t in self.__inputpins:
                if t.CC0 is None or t.CC1 is None:
                    return
                cc0.append(t.CC0)
                cc1.append(t.CC1)

            oV = COFormula.CC0CC1Functions[self.__g_type](cc0, cc1)
            for m in self.__outputpins:
                m.setCC0CC1(oV[0], oV[1])

        elif circuit_type == CIRCUIT_TYPE.SEQUENTIAL:
            for t in self.__inputpins:
                if t.SC0 is None or t.SC1 is None:
                    return
                sc0.append(t.SC0)
                sc1.append(t.SC1)

            oV = COFormula.SC0SC1Functions[self.__g_type](sc0, sc1)
            for m in self.__outputpins:
                if m.changed_SC0_SC1 > (self.parent_module.max_version if MAX_VERSION is None else min(self.parent_module.max_version, MAX_VERSION)):
                    self.parent_module.gates_to_invoke_exclusion.add(self)
                else:
                    m.setSC0SC1(oV[0], oV[1])

        self.removeFromUninvoked()

    def invokeOutput_to_Input(self, circuit_type):
        cc0 = []
        cc1 = []
        sc0 = []
        sc1 = []

        co = []
        so = []

        if circuit_type == CIRCUIT_TYPE.COMBINATIONAL:
            for t in self.__inputpins:
                if t.CC0 is None or t.CC1 is None:
                    return
                cc0.append(t.CC0)
                cc1.append(t.CC1)

            for t in self.__outputpins:
                if t.CO is None:
                    return
                co.append(t.CO)

            oV = COFormula.COFunctions[self.__g_type](cc0, cc1, co)
            for m in range(len(self.__inputpins)):
                self.__inputpins[m].setCO(oV[m])

        elif circuit_type == CIRCUIT_TYPE.SEQUENTIAL:
            for t in self.__inputpins:
                if t.SC0 is None or t.SC1 is None:
                    return
                sc0.append(t.SC0)
                sc1.append(t.SC1)

            for t in self.__outputpins:
                if t.SO is None:
                    return
                so.append(t.SO)

            oV = COFormula.SOFunctions[self.__g_type](sc0, sc1, so)
            for m in range(len(self.__inputpins)):
                p = self.__inputpins[m]
                if p.changed_SO > (self.parent_module.max_version if MAX_VERSION is None else min(self.parent_module.max_version, MAX_VERSION)):
                    self.parent_module.gates_to_invoke_exclusion.add(self)
                else:
                    p.setSO(oV[m])

        self.removeFromUninvoked()

    def invokeProbInput_to_Output(self):
        prob1 = []

        for t in self.__inputpins:
            if t.PROB_1 is None:
                return
            prob1.append(t.PROB_1)

        oV = ProbFormula.ProbFunctions[self.__g_type](prob1)
        for m in self.__outputpins:
            if m.PROB_1 is not None and self.__g_type in FLIPFLOP:
                continue
            m.setProb(oV)

        self.removeFromUninvoked()

    # def correctUninvoked(self):
    #     cc0 = []
    #     cc1 = []
    #
    #     for p in self.__inputpins:
    #         if p.CC0 is None:
    #             p.CC0 = 1
    #         if p.CC1 is None:
    #             p.CC1 = 1
    #         cc0.append(p.CC0)
    #         cc1.append(p.CC1)
    #
    #     oV = COFormula.CCOCC1Functions[self.__g_type](cc0, cc1)
    #     for m in self.__outputpins:
    #         m.CC0 = oV[0]
    #         m.CC1 = oV[1]

    def removeFromUninvoked(self):
        if self in uninvoked:
            uninvoked.remove(self)

    def setOutputCC0CC1(self,cc0Value,cc1Value):
        for m in self.__outputpins:
            m.setCC0CC1(cc0Value,cc1Value)

    def setOutputSC0SC1(self, sc0Value, sc1Value):
        for m in self.__outputpins:
            m.setSC0SC1(sc0Value, sc1Value)

    def setInputCO(self,coValue):
        for m in self.__inputpins:
            m.setCO(coValue)

    def setInputSO(self,soValue):
        for m in self.__inputpins:
            m.setSO(soValue)

    def setOutputProb(self,prob1Value):
        for m in self.__outputpins:
            m.setProb(prob1Value)


class Pin:
    type = None
    parent_gate = None
    connected_wires = None

    CC0 = None
    CC1 = None
    CO = None
    SC0 = None
    SC1 = None
    SO = None
    PROB_1 = None

    changed_SC0_SC1 = None
    changed_SO = None

    def __init__(self,type: FAN,parent_gate: Gate):
        self.type = type
        self.parent_gate = parent_gate
        self.connected_wires = dict()

        self.CC0 = None
        self.CC1 = None
        self.CO = None
        self.SC0 = None
        self.SC1 = None
        self.SO = None
        self.PROB_1 = None

        self.changed_SC0_SC1 = 0
        self.changed_SO = 0

    def connect_wire(self,wire: Wire):
        if self.type == FAN.IN:
            wire.outputsidePins.append(self)
        elif self.type == FAN.OUT:
            wire.inputsidePins.append(self)
        self.connected_wires[wire.id] = wire

    def setCC0CC1(self, valueCC0, valueCC1):
        if self.CC0 == valueCC0 and self.CC1 == valueCC1:
            return
        self.CC0 = valueCC0
        self.CC1 = valueCC1
        if self.type == FAN.OUT:
            for r in self.connected_wires.keys():
                self.connected_wires[r].pushCC0CC1(valueCC0,valueCC1)

    def setSC0SC1(self, valueSC0, valueSC1):
        if self.SC0 == valueSC0 and self.SC1 == valueSC1:
            return
        self.changed_SC0_SC1 += 1
        self.SC0 = valueSC0
        self.SC1 = valueSC1
        if self.type == FAN.OUT:
            for r in self.connected_wires.keys():
                self.connected_wires[r].pushSC0SC1(valueSC0,valueSC1)

    def setCO(self, valueCO):
        if self.CO == valueCO:
            return
        self.CO = valueCO
        if self.type == FAN.IN:
            for r in self.connected_wires.keys():
                self.connected_wires[r].pushCO(valueCO)

    def setSO(self, valueSO):
        if self.SO == valueSO:
            return
        self.changed_SO += 1
        self.SO = valueSO
        if self.type == FAN.IN:
            for r in self.connected_wires.keys():
                self.connected_wires[r].pushSO(valueSO)

    def setProb(self, value_prob1):
        if self.PROB_1 == value_prob1:
            return
        self.PROB_1 = value_prob1
        if self.type == FAN.OUT:
            for r in self.connected_wires.keys():
                self.connected_wires[r].pushProb(value_prob1)


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

        self.flipflops = set()
        self.gates_to_invoke = []
        self.max_version = 99999999999
        self.gates_to_invoke_exclusion = set()

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
        if agate.getType() in FLIPFLOP:
            self.flipflops.add(agate)
        uninvoked.add(agate)

    def getgates(self):
        return self.__gates


class COPCalculator:
    input_file = None
    m = None
    final_data = None

    def __init__(self,input_file):
        self.input_file = input_file
        self.m = Module()
        self.__build()
        self.m.max_version = RATIO_VERSION_BY_CIRCUIT_SIZE * len(self.m.getgates())
        self.__startCalculation()

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

    def __assign_co_non_connected_pin(self):
        # Wires which doesnt connect to input or output, assigning default values to associated pins
        for i in self.m.getWires():
            w = self.m.getWires()[i]
            if len(w.inputsidePins) == 0:
                if self.m.circuit_type == CIRCUIT_TYPE.COMBINATIONAL:
                    w.pushCC0CC1(1, 1)
                elif self.m.circuit_type == CIRCUIT_TYPE.SEQUENTIAL:
                    w.pushSC0SC1(0, 0)
            if len(w.outputsidePins) == 0:
                if self.m.circuit_type == CIRCUIT_TYPE.COMBINATIONAL:
                    w.pushCO(0)
                elif self.m.circuit_type == CIRCUIT_TYPE.SEQUENTIAL:
                    w.pushSO(0)

    def __assign_co_pseudo_io(self):
        # Assigning values to pseudo input and pseudo outout for flipflops
        for flipflop in self.m.flipflops:
            if self.m.circuit_type == CIRCUIT_TYPE.COMBINATIONAL:
                flipflop.setOutputCC0CC1(1, 1)
                flipflop.setInputCO(0)
            elif self.m.circuit_type == CIRCUIT_TYPE.SEQUENTIAL:
                flipflop.setOutputSC0SC1(0, 0)
                flipflop.setInputSO(0)

    def __assign_c_input_pin(self):
        for i in self.m.getInputpins().keys():
            for pin in self.m.getInputpins()[i]:
                if self.m.circuit_type == CIRCUIT_TYPE.COMBINATIONAL:
                    pin.setCC0CC1(1,1)
                elif self.m.circuit_type == CIRCUIT_TYPE.SEQUENTIAL:
                    pin.setSC0SC1(0,0)
                pin.parent_gate.invokeInput_to_Output(self.m.circuit_type)

    def __clear_invoke_gates(self):
        self.m.gates_to_invoke.clear()
        self.m.gates_to_invoke_exclusion.clear()

    def __assign_o_output_pin(self):
        for i in self.m.getOutputpins().keys():
            for pin in self.m.getOutputpins()[i]:
                if self.m.circuit_type == CIRCUIT_TYPE.COMBINATIONAL:
                    pin.setCO(0)
                elif self.m.circuit_type == CIRCUIT_TYPE.SEQUENTIAL:
                    pin.setSO(0)
                pin.parent_gate.invokeOutput_to_Input(self.m.circuit_type)

    def __assign_prob_input_pin(self):
        for i in self.m.getInputpins().keys():
            for pin in self.m.getInputpins()[i]:
                pin.setProb(0.5)
                pin.parent_gate.invokeProbInput_to_Output()

    def __assign_prob_non_connected_pin(self):
        for i in self.m.getWires():
            w = self.m.getWires()[i]
            if len(w.inputsidePins) == 0:
                w.pushProb(0.5)

    def __assign_prob_pseudo_in(self):
        for flipflop in self.m.flipflops:
            flipflop.setOutputProb(0.5)

    def __startCalculation(self):

        self.__assign_co_non_connected_pin()
        self.__assign_co_pseudo_io()

        self.__assign_c_input_pin()
        while len(self.m.gates_to_invoke) != 0:
            gate = self.m.gates_to_invoke.pop(0)
            gate.invokeInput_to_Output(self.m.circuit_type)
        self.__clear_invoke_gates()

        # print("Unresolved CC0 CC1: ", len(uninvoked), '/', len(self.m.getgates()))

        self.__assign_o_output_pin()
        while len(self.m.gates_to_invoke) != 0:
            gate = self.m.gates_to_invoke.pop(0)
            gate.invokeOutput_to_Input(self.m.circuit_type)
        self.__clear_invoke_gates()

        self.__assign_prob_non_connected_pin()
        self.__assign_prob_pseudo_in()

        self.__assign_prob_input_pin()
        while len(self.m.gates_to_invoke) != 0:
            gate = self.m.gates_to_invoke.pop(0)
            gate.invokeProbInput_to_Output()
        self.__clear_invoke_gates()

        # print("LOOPING GATES: ",len(self.m.gates_to_invoke_exclusion))


        # for i in uninvoked:
        #     i.correctUninvoked()

        uninvoked.clear()

    def solveNone(self, val):
        if val is None:
            return INF
        else:
            return val

    def export(self,export_file):

        data = dict()

        for gate in self.m.getgates():
            gate = self.m.getgates()[gate]
            for input_pin in gate.getInputPins():
                for wire in input_pin.connected_wires.keys():
                    wire = input_pin.connected_wires[wire]
                    if wire.id not in data:
                        data[wire.id] = []
                        if self.m.circuit_type == CIRCUIT_TYPE.COMBINATIONAL:
                            data[wire.id].append(self.solveNone(input_pin.CC0))
                            data[wire.id].append(self.solveNone(input_pin.CC1))
                            data[wire.id].append(self.solveNone(input_pin.CO))
                        elif self.m.circuit_type == CIRCUIT_TYPE.SEQUENTIAL:
                            data[wire.id].append(self.solveNone(input_pin.SC0))
                            data[wire.id].append(self.solveNone(input_pin.SC1))
                            data[wire.id].append(self.solveNone(input_pin.SO))
                        data[wire.id].extend([(1-input_pin.PROB_1) if input_pin.PROB_1 is not None else 0.5, input_pin.PROB_1 if input_pin.PROB_1 is not None else 0.5])

            for output_pin in gate.getOutputPins():
                for wire in output_pin.connected_wires.keys():
                    wire = output_pin.connected_wires[wire]
                    if wire.id not in data:
                        data[wire.id] = []
                        if self.m.circuit_type == CIRCUIT_TYPE.COMBINATIONAL:
                            data[wire.id].append(self.solveNone(output_pin.CC0))
                            data[wire.id].append(self.solveNone(output_pin.CC1))
                            data[wire.id].append(self.solveNone(output_pin.CO))
                        elif self.m.circuit_type == CIRCUIT_TYPE.SEQUENTIAL:
                            data[wire.id].append(self.solveNone(output_pin.SC0))
                            data[wire.id].append(self.solveNone(output_pin.SC1))
                            data[wire.id].append(self.solveNone(output_pin.SO))
                        data[wire.id].extend([(1-output_pin.PROB_1) if output_pin.PROB_1 is not None else 0.5, output_pin.PROB_1 if output_pin.PROB_1 is not None else 0.5])

        file = open(export_file, 'w', newline='')
        writer = csv.writer(file)
        writer.writerow(['Wire', 'Controllability0', "Controllability1", "Observability", "Prob0", "Prob1"])

        for d in data.keys():
            l = [d] + data[d]
            writer.writerow(l)
        file.close()