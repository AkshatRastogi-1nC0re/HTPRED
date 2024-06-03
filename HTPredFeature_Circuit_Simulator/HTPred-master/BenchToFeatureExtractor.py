import uuid
import enum
import csv

FLIPFLOP = {"DFF"}
NEAREST_HARD_LIMIT = 100


class FAN(enum.Enum):
    IN = 0
    OUT = 1


class Wire:
    id = None
    inputsidePins = None
    outputsidePins = None

    def __init__(self,id):
        self.id = id
        self.inputsidePins = []
        self.outputsidePins = []

    def getInputPins(self):
        return self.inputsidePins

    def getOutputPins(self):
        return self.outputsidePins


class Gate:
    __id = None
    __g_type = None
    __inputpins = None
    __outputpins = None

    def __init__(self,inputwires, outputwires, parentmodule, type):
        self.__id = type+"_"+str(uuid.uuid4())
        self.__g_type = type
        self.__inputpins = []
        self.__outputpins = []

        for i in inputwires:
            apin = Pin(FAN.IN,self)
            self.__inputpins.append(apin)
            if isinstance(i,str):
                parentmodule.setPin(i,apin)
            elif isinstance(i,Wire):
                apin.connect_wire(i)

        for i in outputwires:
            apin = Pin(FAN.OUT,self)
            self.__outputpins.append(apin)
            if isinstance(i,str):
                parentmodule.setPin(i,apin)
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
        print(self.__id)
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
        self.__wires[outp] = Wire(outp)

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
                    self.__wires[s] = Wire(s)
                inputWireObjects.append(self.__wires[s])

        for s in outputWires:
            if s in self.__inputpins.keys() or s in self.__outputpins.keys():
                outputWireObjects.append(s)
            else:
                if s not in self.__wires.keys():
                    self.__wires[s] = Wire(s)
                outputWireObjects.append(self.__wires[s])

        agate = Gate(inputWireObjects,outputWireObjects,self,gatetype)
        self.__gates[agate.getID()] = agate

    def printModule(self):
        print("INPUTS :")
        for i in self.__inputpins:
            print(i,self.__inputpins[i])

        print("\n","OUTPUTS :")
        for i in self.__outputpins:
            print(i,self.__outputpins[i])

        print("\n","GATES :")
        for i in self.__gates.keys():
            self.__gates[i].printGate()

        print("\n","WIRES")
        for i in self.__wires.keys():
            print("WIRE: ",self.__wires[i])
            print("\tINPUT: ",self.__wires[i].inputsidePins)
            print("\tOUTPUT: ",self.__wires[i].outputsidePins)


class BenchToFeature:
    input_file = None
    m = None
    final_data = None

    def __init__(self,input_file):
        self.input_file = input_file
        self.m = Module()

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

    def calculatefeatures(self):
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

        final_data = dict()
        final_data["fan_in_x"] = self.__get_fan_in_x()
        final_data["loop_in_x"] = self.__get_loop_in_x()
        final_data["loop_out_x"] = self.__get_loop_out_x()
        final_data["in_nearest_pin"] = self.__get_nearest_pin()
        final_data["out_nearest_pout"] = self.__get_nearest_pout()
        final_data["in_ff_x"] = self.__get_in_ff_x()
        final_data["out_ff_x"] = self.__get_out_ff_x()
        final_data["in_nearest_ff"] = self.__in_nearest_ff()
        final_data["out_nearest_ff"] = self.__out_nearest_ff()
        final_data["in_const_x"] = self.__in_const_x()
        final_data["out_const_x"] = self.__out_const_x()

        self.final_data = final_data

    def __recfanin(self,wire:Wire,vector,i,max_n):
        if i == max_n:
            return 0

        for t in wire.inputsidePins:
            gate = t.parent_gate

            vector[i] += len(gate.getInputPins())

            for gp in gate.getInputPins():
                for s in gp.connected_wires.keys():
                    actwire = gp.connected_wires[s]
                    self.__recfanin(actwire,vector,i+1,max_n)

    def __recloopin(self,currentWire:Wire, targetWire:Wire, vector,i,max_n):
        if i == max_n:
            return

        if currentWire is targetWire and i >= 0:
            vector[i] += 1

        for t in currentWire.inputsidePins:
            gate = t.parent_gate

            for gp in gate.getInputPins():
                for s in gp.connected_wires.keys():
                    actwire = gp.connected_wires[s]
                    self.__recloopin(actwire,targetWire,vector,i+1,max_n)

    def __recloopout(self,currentWire:Wire, targetWire:Wire, vector,i,max_n):
        if i == max_n:
            return

        if currentWire is targetWire and i >= 0:
            vector[i] += 1

        for t in currentWire.outputsidePins:
            gate = t.parent_gate

            for gp in gate.getOutputPins():
                for s in gp.connected_wires.keys():
                    actwire = gp.connected_wires[s]
                    self.__recloopout(actwire,targetWire,vector,i+1,max_n)

    def __get_fan_in_x(self):
        data = dict()

        for net in self.m.getWires().keys():
            data[net] = [0,0,0,0,0]
            self.__recfanin(self.m.getWires()[net],data[net],0,5)

        return data

    def __get_loop_in_x(self):
        data = dict()

        for net in self.m.getWires().keys():
            data[net] = [0,0,0,0,0]
            self.__recloopin(self.m.getWires()[net], self.m.getWires()[net], data[net], -1, 5)

        return data

    def __get_loop_out_x(self):
        data = dict()

        for net in self.m.getWires().keys():
            data[net] = [0,0,0,0,0]
            self.__recloopout(self.m.getWires()[net], self.m.getWires()[net], data[net], -1, 5)

        return data

    def __distance_pin_net(self, pin,data):
        parent_gate = pin.parent_gate
        wireStack = []

        for gate_outp_pins in parent_gate.getOutputPins():
            for conn_wire in gate_outp_pins.connected_wires.keys():
                wireStack.append((gate_outp_pins.connected_wires[conn_wire],1))

        addedwires = set()
        while len(wireStack) > 0:
            temp = wireStack.pop(0)
            currentwire = temp[0]
            it = temp[1]

            if data[currentwire.id] is None or it <= data[currentwire.id]:
                data[currentwire.id] = it
            elif data[currentwire.id] is not None and it > data[currentwire.id]:
                continue

            for pin in currentwire.outputsidePins:
                pg = pin.parent_gate

                for gate_outp_pins in pg.getOutputPins():
                    for conn_wire in gate_outp_pins.connected_wires.keys():
                        newWire = gate_outp_pins.connected_wires[conn_wire]
                        if newWire in addedwires:
                            continue
                        addedwires.add(newWire)
                        wireStack.append((newWire, it + 1))

    def __get_nearest_pin(self):
        data = dict()
        input_gates_processed = set()

        for net in self.m.getWires().keys():
            data[net] = None

        for inputpinsets in self.m.getInputpins().keys():
            for inputpin in self.m.getInputpins()[inputpinsets]:
                if inputpin.parent_gate not in input_gates_processed:
                    self.__distance_pin_net(inputpin,data)
                    input_gates_processed.add(inputpin.parent_gate)

        return data

    def __distance_pout_net(self, pin, data):
        parent_gate = pin.parent_gate
        wireStack = []

        for gate_inp_pins in parent_gate.getInputPins():
            for conn_wire in gate_inp_pins.connected_wires.keys():
                wireStack.append((gate_inp_pins.connected_wires[conn_wire], 1))

        addedwires = set()
        while len(wireStack) > 0:
            temp = wireStack.pop(0)
            currentwire = temp[0]
            it = temp[1]

            if data[currentwire.id] is None or it <= data[currentwire.id]:
                data[currentwire.id] = it
            elif data[currentwire.id] is not None and it > data[currentwire.id]:
                continue

            for pin in currentwire.inputsidePins:
                pg = pin.parent_gate

                for gate_inp_pins in pg.getInputPins():
                    for conn_wire in gate_inp_pins.connected_wires.keys():
                        newWire = gate_inp_pins.connected_wires[conn_wire]
                        if newWire in addedwires:
                            continue
                        addedwires.add(newWire)
                        wireStack.append((newWire, it + 1))

    def __get_nearest_pout(self):
        data = dict()
        output_gates_processed = set()

        for net in self.m.getWires().keys():
            data[net] = None

        for outputpinsets in self.m.getOutputpins().keys():
            for outputpin in self.m.getOutputpins()[outputpinsets]:
                if outputpin.parent_gate not in output_gates_processed:
                    self.__distance_pout_net(outputpin, data)
                    output_gates_processed.add(outputpin.parent_gate)
        return data

    def __recffin(self,wire:Wire,vector, i, max_n):
        if i == max_n:
            return

        for t in wire.inputsidePins:
            gate = t.parent_gate
            if gate.getType() in FLIPFLOP:
                vector[i] += 1

            for gp in gate.getInputPins():
                for s in gp.connected_wires.keys():
                    actwire = gp.connected_wires[s]
                    self.__recffin(actwire, vector, i + 1, max_n)

    def __get_in_ff_x(self):
        data = dict()

        for net in self.m.getWires().keys():
            data[net] = [0,0,0,0,0]
            self.__recffin(self.m.getWires()[net], data[net], 0, 5)

        return data

    def __recffout(self, wire: Wire, vector, i, max_n):
        if i == max_n:
            return

        for t in wire.outputsidePins:
            gate = t.parent_gate
            if gate.getType() in FLIPFLOP:
                vector[i] += 1

            for gp in gate.getOutputPins():
                for s in gp.connected_wires.keys():
                    actwire = gp.connected_wires[s]
                    self.__recffout(actwire, vector, i + 1, max_n)

    def __get_out_ff_x(self):
        data = dict()

        for net in self.m.getWires().keys():
            data[net] = [0, 0, 0, 0, 0]
            self.__recffout(self.m.getWires()[net], data[net], 0, 5)

        return data

    def __recinnearff(self, wire: Wire):

        wireStack = [(wire,0)]
        addedwires = {wire}

        while len(wireStack) > 0:
            temp = wireStack.pop(0)
            currentwire = temp[0]
            it = temp[1]

            if it > NEAREST_HARD_LIMIT:
                return None

            for pin in currentwire.inputsidePins:
                pg = pin.parent_gate

                if pg.getType() in FLIPFLOP:
                    return it

                for gate_inp_pins in pg.getInputPins():
                    for conn_wire in gate_inp_pins.connected_wires.keys():
                        newWire = gate_inp_pins.connected_wires[conn_wire]
                        if newWire in addedwires:
                            continue
                        addedwires.add(newWire)
                        wireStack.append((newWire, it + 1))

        return None

    def __in_nearest_ff(self):
        data = dict()

        for net in self.m.getWires().keys():
            data[net] = self.__recinnearff(self.m.getWires()[net])

        return data

    def __recoutnearff(self, wire: Wire):

        wireStack = [(wire, 0)]
        addedwires = {wire}

        while len(wireStack) > 0:
            temp = wireStack.pop(0)
            currentwire = temp[0]
            it = temp[1]

            if it > NEAREST_HARD_LIMIT:
                return None

            for pin in currentwire.outputsidePins:
                pg = pin.parent_gate

                if pg.getType() in FLIPFLOP:
                    return it

                for gate_outp_pins in pg.getOutputPins():
                    for conn_wire in gate_outp_pins.connected_wires.keys():
                        newWire = gate_outp_pins.connected_wires[conn_wire]
                        if newWire in addedwires:
                            continue
                        addedwires.add(newWire)
                        wireStack.append((newWire, it + 1))

        return None

    def __out_nearest_ff(self):
        data = dict()

        for net in self.m.getWires().keys():
            data[net] = self.__recoutnearff(self.m.getWires()[net])
        return data

    def __recconstin(self,wire:Wire, vector, i, max_n):
        if i == max_n:
            return

        for t in wire.inputsidePins:
            gate = t.parent_gate

            for gp in gate.getInputPins():
                if gp in self.m.getInputpins()["VDD"] or gp in self.m.getInputpins()["GND"]:
                    vector[i] += 1

            for gp in gate.getInputPins():
                for s in gp.connected_wires.keys():
                    actwire = gp.connected_wires[s]
                    self.__recconstin(actwire, vector, i + 1, max_n)

    def __in_const_x(self):
        data = dict()

        for net in self.m.getWires().keys():
            data[net] = [0, 0, 0, 0, 0]
            self.__recconstin(self.m.getWires()[net], data[net], 0, 5)

        return data

    def __recconstout(self,wire:Wire, vector, i, max_n):
        if i == max_n:
            return

        for t in wire.outputsidePins:
            gate = t.parent_gate

            for gp in gate.getInputPins():
                if gp in self.m.getInputpins()["VDD"] or gp in self.m.getInputpins()["GND"]:
                    vector[i] += 1

            for gp in gate.getOutputPins():
                for s in gp.connected_wires.keys():
                    actwire = gp.connected_wires[s]
                    self.__recconstout(actwire, vector, i + 1, max_n)

    def __out_const_x(self):
        data = dict()

        for net in self.m.getWires().keys():
            data[net] = [0, 0, 0, 0, 0]
            self.__recconstout(self.m.getWires()[net], data[net], 0, 5)

        return data

    def export_to_file(self,export_file):
        data = self.final_data

        order = list(data.keys())
        file = open(export_file,'w',newline='')
        writer = csv.writer(file)
        writer.writerow(self.__get_header(order))

        for wire in self.m.getWires():
            arow = [wire]
            for m in order:
                if data[m][arow[0]] is None:
                    arow.append("None")
                elif isinstance(data[m][arow[0]],list):
                    arow.extend(data[m][arow[0]])
                else:
                    arow.append(data[m][arow[0]])
            writer.writerow(arow)
        file.close()

    def get_final_data(self):
        return self.final_data

    def __get_header(self,columns):
        header = ["wire"]

        for t in columns:
            if t[-1] == 'x':
                for i in range(1,6):
                    header.append(t[0:-1]+str(i))
            else:
                header.append(t)
        return header
