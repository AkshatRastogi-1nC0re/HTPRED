class bench_session:
    __module = None
    __map = None

    __input_label = None
    __output_label = None
    __wire_label = None

    __input_marker = None
    __output_marker = None
    __wire_marker = None

    def __init__(self, module, input_label, output_label, wire_label):
        self.__module = module
        self.__input_label = input_label
        self.__output_label = output_label
        self.__wire_label = wire_label
        self.__input_marker = 0
        self.__output_marker = 0
        self.__wire_marker = 0
        self.__map = dict()

    def get_map(self):
        for i in self.__module.getWires().keys():
            for inP in self.__module.getWires()[i].get_in():
                self.__map[inP] = self.__wire_label + str(self.__wire_marker)
            for outP in self.__module.getWires()[i].get_out():
                self.__map[outP] = self.__wire_label + str(self.__wire_marker)
            self.__wire_marker += 1

        for i in self.__module.getInputs().keys():
            if i == 'VDD' or i == 'GND':
                for j in self.__module.getInputs()[i]:
                    self.__map[j] = i
            else:
                if len(self.__module.getInputs()[i]) == 0:
                    self.__map['!UNCONNECTED'+i] = self.__input_label + str(self.__input_marker)
                else:
                    for j in self.__module.getInputs()[i]:
                        self.__map[j] = self.__input_label + str(self.__input_marker)
                self.__input_marker += 1

        for i in self.__module.getOutputs().keys():
            if len(self.__module.getOutputs()[i]) == 0:
                self.__map['!UNCONNECTED' + i] = self.__output_label + str(self.__output_marker)
            else:
                for j in self.__module.getOutputs()[i]:
                    self.__map[j] = self.__output_label + str(self.__output_marker)
            self.__output_marker += 1

        return self.__map
