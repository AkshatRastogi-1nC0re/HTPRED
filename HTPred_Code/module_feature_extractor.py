import bench_session

FLIP_FLOP = ['DFF']
MUX = ['MUX']


class feature_extractor:
    __module = None
    __map = None

    def __init__(self, module):
        self.__module = module
        self.__map = bench_session.bench_session(self.__module, 'I', 'U', 'W').get_map()

    def lgfi(self):
        output = list()
        output.extend([[],[],[],[],[],[]])
        for i in self.__module.getWires():
            w = self.__module.getWires()[i]
            if len(w.get_in())>0:
                output[0].append(self.__map[self.__get_pin_from_wire(w)])
                output[1].append(self.__fan_in_n_level(w, 1))

        for i in self.__module.getWires():
            w = self.__module.getWires()[i]
            if len(w.get_in())>0:
                output[2].append(self.__fan_in_n_level(w, 2))

        for i in self.__module.getWires():
            w = self.__module.getWires()[i]
            if len(w.get_in())>0:
                output[3].append(self.__fan_in_n_level(w, 3))

        for i in self.__module.getWires():
            w = self.__module.getWires()[i]
            if len(w.get_in())>0:
                output[4].append(self.__fan_in_n_level(w, 4))

        for i in self.__module.getWires():
            w = self.__module.getWires()[i]
            if len(w.get_in())>0:
                output[5].append(self.__fan_in_n_level(w, 5))

        return output

    def __fan_in_n_level(self, wire, iter):
        if iter == 0:
            return 1

        if wire is None:
            return 0

        count = 0
        for t in wire.get_in():
            parent_gate = t.get_parent_gate()

            for inputpins in parent_gate.get_inputs():
                pin_set = parent_gate.get_inputs()[inputpins]

                for pin in pin_set:
                    if pin.get_connected_wire() is not None:
                        count += self.__fan_in_n_level(pin.get_connected_wire(),iter-1)
                    elif pin in self.__map and iter == 1:
                        count += 1
        return count

    def mux_in(self):
        output = list()
        output.extend([[], [], [], [], [], []])

        for i in self.__module.getWires():
            w = self.__module.getWires()[i]
            if len(w.get_in())>0:
                output[0].append(self.__map[self.__get_pin_from_wire(w)])
                output[1].append(self.__in_mux_ff_n_level(w, 1,MUX))

        for i in self.__module.getWires():
            w = self.__module.getWires()[i]
            if len(w.get_in())>0:
                output[2].append(self.__in_mux_ff_n_level(w, 2,MUX))

        for i in self.__module.getWires():
            w = self.__module.getWires()[i]
            if len(w.get_in())>0:
                output[3].append(self.__in_mux_ff_n_level(w, 3,MUX))

        for i in self.__module.getWires():
            w = self.__module.getWires()[i]
            if len(w.get_in())>0:
                output[4].append(self.__in_mux_ff_n_level(w, 4,MUX))

        for i in self.__module.getWires():
            w = self.__module.getWires()[i]
            if len(w.get_in())>0:
                output[5].append(self.__in_mux_ff_n_level(w, 5, MUX))

        return output

    def ff_in(self):
        output = list()
        output.extend([[], [], [], [], [], []])

        for i in self.__module.getWires():
            w = self.__module.getWires()[i]
            if len(w.get_in())>0:
                output[0].append(self.__map[self.__get_pin_from_wire(w)])
                output[1].append(self.__in_mux_ff_n_level(w, 1,FLIP_FLOP))

        for i in self.__module.getWires():
            w = self.__module.getWires()[i]
            if len(w.get_in())>0:
                output[2].append(self.__in_mux_ff_n_level(w, 2,FLIP_FLOP))

        for i in self.__module.getWires():
            w = self.__module.getWires()[i]
            if len(w.get_in())>0:
                output[3].append(self.__in_mux_ff_n_level(w, 3,FLIP_FLOP))

        for i in self.__module.getWires():
            w = self.__module.getWires()[i]
            if len(w.get_in())>0:
                output[4].append(self.__in_mux_ff_n_level(w, 4,FLIP_FLOP))

        for i in self.__module.getWires():
            w = self.__module.getWires()[i]
            if len(w.get_in())>0:
                output[5].append(self.__in_mux_ff_n_level(w, 5, FLIP_FLOP))

        return output

    def __in_mux_ff_n_level(self,wire,iter,g_type):
        if iter == 0:
            count = 0
            for s in wire.get_in():
                if s.get_parent_gate().get_type() in g_type:
                    count += 1
            return count

        count = 0
        for t in wire.get_in():
            parent_gate = t.get_parent_gate()

            for inputpins in parent_gate.get_inputs():
                pin_set = parent_gate.get_inputs()[inputpins]

                for pin in pin_set:
                    if pin.get_connected_wire() is not None:
                        count += self.__in_mux_ff_n_level(pin.get_connected_wire(),iter-1,g_type)
        return count

    def __out_mux_ff_n_level(self,wire,iter,g_type):
        if iter == 0:
            count = 0
            for s in wire.get_out():
                if s.get_parent_gate().get_type() in g_type:
                    count += 1
            return count

        count = 0
        for t in wire.get_out():
            parent_gate = t.get_parent_gate()

            for outputpins in parent_gate.get_outputs():
                pin_set = parent_gate.get_outputs()[outputpins]

                for pin in pin_set:
                    if pin.get_connected_wire() is not None:
                        count += self.__out_mux_ff_n_level(pin.get_connected_wire(),iter-1,g_type)
        return count

    def mux_out(self):
        output = list()
        output.extend([[], [], [], [], [], []])

        for i in self.__module.getWires():
            w = self.__module.getWires()[i]
            if len(w.get_out())>0:
                output[0].append(self.__map[self.__get_pin_from_wire(w)])
                output[1].append(self.__out_mux_ff_n_level(w, 1,MUX))

        for i in self.__module.getWires():
            w = self.__module.getWires()[i]
            if len(w.get_out())>0:
                output[2].append(self.__out_mux_ff_n_level(w, 2,MUX))

        for i in self.__module.getWires():
            w = self.__module.getWires()[i]
            if len(w.get_out())>0:
                output[3].append(self.__out_mux_ff_n_level(w, 3,MUX))

        for i in self.__module.getWires():
            w = self.__module.getWires()[i]
            if len(w.get_out())>0:
                output[4].append(self.__out_mux_ff_n_level(w, 4,MUX))

        for i in self.__module.getWires():
            w = self.__module.getWires()[i]
            if len(w.get_out())>0:
                output[5].append(self.__out_mux_ff_n_level(w, 5, MUX))

        return output

    def ff_out(self):
        output = list()
        output.extend([[], [], [], [], [], []])

        for i in self.__module.getWires():
            w = self.__module.getWires()[i]
            if len(w.get_out())>0:
                output[0].append(self.__map[self.__get_pin_from_wire(w)])
                output[1].append(self.__out_mux_ff_n_level(w, 1, FLIP_FLOP))

        for i in self.__module.getWires():
            w = self.__module.getWires()[i]
            if len(w.get_out())>0:
                output[2].append(self.__out_mux_ff_n_level(w, 2, FLIP_FLOP))

        for i in self.__module.getWires():
            w = self.__module.getWires()[i]
            if len(w.get_out())>0:
                output[3].append(self.__out_mux_ff_n_level(w, 3, FLIP_FLOP))

        for i in self.__module.getWires():
            w = self.__module.getWires()[i]
            if len(w.get_out())>0:
                output[4].append(self.__out_mux_ff_n_level(w, 4, FLIP_FLOP))

        for i in self.__module.getWires():
            w = self.__module.getWires()[i]
            if len(w.get_out())>0:
                output[5].append(self.__out_mux_ff_n_level(w, 5, FLIP_FLOP))

        return output

    def loop_in(self):
        output = list()
        output.extend([[], [], [], [], [], []])

        for i in self.__module.getWires():
            w = self.__module.getWires()[i]
            if len(w.get_in()) > 0:
                output[0].append(self.__map[self.__get_pin_from_wire(w)])
                output[1].append(self.__in_loop_n_level(w, w, 1))

        for i in self.__module.getWires():
            w = self.__module.getWires()[i]
            if len(w.get_in()) > 0:
                output[2].append(self.__in_loop_n_level(w, w, 2))

        for i in self.__module.getWires():
            w = self.__module.getWires()[i]
            if len(w.get_in()) > 0:
                output[3].append(self.__in_loop_n_level(w, w, 3))

        for i in self.__module.getWires():
            w = self.__module.getWires()[i]
            if len(w.get_in()) > 0:
                output[4].append(self.__in_loop_n_level(w, w, 4))

        for i in self.__module.getWires():
            w = self.__module.getWires()[i]
            if len(w.get_in()) > 0:
                output[5].append(self.__in_loop_n_level(w, w, 5))

        return output

    def __in_loop_n_level(self, current, starting, iter):
        if iter == 0:
            if current is starting:
                return 1
            else:
                return 0

        count = 0
        for t in current.get_in():
            parent_gate = t.get_parent_gate()

            for inputpins in parent_gate.get_inputs():
                pin_set = parent_gate.get_inputs()[inputpins]

                for pin in pin_set:
                    if pin.get_connected_wire() is not None:
                        count += self.__in_loop_n_level(pin.get_connected_wire(), starting, iter - 1)
        return count

    def loop_out(self):
        output = list()
        output.extend([[], [], [], [], [], []])

        for i in self.__module.getWires():
            w = self.__module.getWires()[i]
            if len(w.get_out()) > 0:
                output[0].append(self.__map[self.__get_pin_from_wire(w)])
                output[1].append(self.__out_loop_n_level(w, w, 1))

        for i in self.__module.getWires():
            w = self.__module.getWires()[i]
            if len(w.get_out()) > 0:
                output[2].append(self.__out_loop_n_level(w, w, 2))

        for i in self.__module.getWires():
            w = self.__module.getWires()[i]
            if len(w.get_out()) > 0:
                output[3].append(self.__out_loop_n_level(w, w, 3))

        for i in self.__module.getWires():
            w = self.__module.getWires()[i]
            if len(w.get_out()) > 0:
                output[4].append(self.__out_loop_n_level(w, w, 4))

        for i in self.__module.getWires():
            w = self.__module.getWires()[i]
            if len(w.get_out()) > 0:
                output[5].append(self.__out_loop_n_level(w, w, 5))

        return output

    def __out_loop_n_level(self, current, starting, iter):
        if iter == 0:
            if current is starting:
                return 1
            else:
                return 0

        count = 0
        for t in current.get_out():
            parent_gate = t.get_parent_gate()

            for outputpins in parent_gate.get_outputs():
                pin_set = parent_gate.get_outputs()[outputpins]

                for pin in pin_set:
                    if pin.get_connected_wire() is not None:
                        count += self.__out_loop_n_level(pin.get_connected_wire(), starting, iter - 1)
        return count

    def in_nearest_pin(self):
        labels = set()
        input_pins = set()
        for i in self.__module.getInputs():
            for j in self.__module.getInputs()[i]:
                if self.__map[j] not in labels:
                    labels.add(self.__map[j])
                    input_pins.add(j)
        del labels

        data = dict()
        for i in input_pins:
            nets_w_dist = self.__get_dist_of_net_from_input(i,data)
            for i in nets_w_dist.keys():
                if i in data:
                    if nets_w_dist[i] < data[i]:
                        data[i] = nets_w_dist[i]
                else:
                    data[i] = nets_w_dist[i]

        output = list()
        output.extend([[], []])

        for i in data.keys():
            output[0].append(self.__map[self.__get_pin_from_wire(i)])
            output[1].append(data[i])
        return output

    def __get_dist_of_net_from_input(self,input_pin,nearest_dict):
        return_dict = dict()

        parent_gate = input_pin.get_parent_gate()
        starting_nets = []
        for outppin in parent_gate.get_outputs():
            for pin in parent_gate.get_outputs()[outppin]:
                starting_nets.append(pin.get_connected_wire())
        visited = set()

        q = []
        for net in starting_nets:
            if net is not None:
                visited.add(net)
                q.append([net,1])

        while len(q) != 0:
            popped_net = q.pop(0)

            for t in popped_net[0].get_out():
                parent_gate = t.get_parent_gate()
                for outppins in parent_gate.get_outputs():
                    pin_set = parent_gate.get_outputs()[outppins]
                    for pin in pin_set:
                        if pin.get_connected_wire() is not None:
                            new_wire = pin.get_connected_wire()
                            if new_wire not in visited:
                                visited.add(new_wire)
                                if new_wire in nearest_dict.keys() and nearest_dict[new_wire] < popped_net[1]+1:
                                    continue
                                q.append([new_wire,popped_net[1]+1])

            return_dict[popped_net[0]] = popped_net[1]
        return return_dict

    def out_nearest_pin(self):
        labels = set()
        output_pins = set()
        for i in self.__module.getOutputs():
            for j in self.__module.getOutputs()[i]:
                if self.__map[j] not in labels:
                    labels.add(self.__map[j])
                    output_pins.add(j)
        del labels

        data = dict()
        for i in output_pins:
            nets_w_dist = self.__get_dist_of_net_from_output(i, data)
            for i in nets_w_dist.keys():
                if i in data:
                    if nets_w_dist[i] < data[i]:
                        data[i] = nets_w_dist[i]
                else:
                    data[i] = nets_w_dist[i]

        output = list()
        output.extend([[], []])

        for i in data.keys():
            output[0].append(self.__map[self.__get_pin_from_wire(i)])
            output[1].append(data[i])
        return output

    def __get_dist_of_net_from_output(self, output_pin, nearest_dict):
        return_dict = dict()

        parent_gate = output_pin.get_parent_gate()
        starting_nets = []
        for inppin in parent_gate.get_inputs():
            for pin in parent_gate.get_inputs()[inppin]:
                starting_nets.append(pin.get_connected_wire())
        visited = set()

        q = []
        for net in starting_nets:
            if net is not None:
                visited.add(net)
                q.append([net, 1])

        while len(q) != 0:
            popped_net = q.pop(0)

            for t in popped_net[0].get_in():
                parent_gate = t.get_parent_gate()
                for inppins in parent_gate.get_inputs():
                    pin_set = parent_gate.get_inputs()[inppins]
                    for pin in pin_set:
                        if pin.get_connected_wire() is not None:
                            new_wire = pin.get_connected_wire()
                            if new_wire not in visited:
                                visited.add(new_wire)
                                if new_wire in nearest_dict.keys() and nearest_dict[new_wire] < popped_net[1] + 1:
                                    continue
                                q.append([new_wire, popped_net[1] + 1])

            return_dict[popped_net[0]] = popped_net[1]
        return return_dict

    def in_nearest_flipflop(self,limit=5):
        output = list()
        output.extend([[], []])

        for i in self.__module.getWires():
            w = self.__module.getWires()[i]
            if len(w.get_in()) > 0:
                output[0].append(self.__map[self.__get_pin_from_wire(w)])
                output[1].append(self.__in_mux_ff_nearest(w, 0, limit, FLIP_FLOP))

        return output

    def in_nearest_mux(self, limit=5):
        output = list()
        output.extend([[], []])

        for i in self.__module.getWires():
            w = self.__module.getWires()[i]
            if len(w.get_in()) > 0:
                output[0].append(self.__map[self.__get_pin_from_wire(w)])
                output[1].append(self.__in_mux_ff_nearest(w, 0, limit, MUX))

        return output

    def __in_mux_ff_nearest(self, wire, iter, limit, g_type):
        if iter > limit:
            return None

        minC = None
        for t in wire.get_in():
            parent_gate = t.get_parent_gate()
            if parent_gate.get_type() in g_type:
                return iter

            for inputpins in parent_gate.get_inputs():
                pin_set = parent_gate.get_inputs()[inputpins]

                for pin in pin_set:
                    if pin.get_connected_wire() is not None:
                        c = self.__in_mux_ff_nearest(pin.get_connected_wire(), iter + 1, limit, g_type)
                        if minC is None or (c is not None and c < minC):
                            minC = c

        return minC

    def out_nearest_flipflop(self,limit=5):
        output = list()
        output.extend([[], []])

        for i in self.__module.getWires():
            w = self.__module.getWires()[i]
            if len(w.get_out()) > 0:
                output[0].append(self.__map[self.__get_pin_from_wire(w)])
                output[1].append(self.__out_mux_ff_nearest(w, 0, limit, FLIP_FLOP))

        return output

    def out_nearest_mux(self, limit=5):
        output = list()
        output.extend([[], []])

        for i in self.__module.getWires():
            w = self.__module.getWires()[i]
            if len(w.get_out()) > 0:

                output[0].append(self.__map[self.__get_pin_from_wire(w)])
                output[1].append(self.__out_mux_ff_nearest(w, 0, limit, MUX))

        return output

    def __out_mux_ff_nearest(self, wire, iter, limit, g_type):
        if iter > limit:
            return None

        minC = None
        for t in wire.get_out():
            parent_gate = t.get_parent_gate()
            if parent_gate.get_type() in g_type:
                return iter

            for outputpins in parent_gate.get_outputs():
                pin_set = parent_gate.get_outputs()[outputpins]

                for pin in pin_set:
                    if pin.get_connected_wire() is not None:
                        c = self.__out_mux_ff_nearest(pin.get_connected_wire(), iter + 1, limit, g_type)
                        if minC is None or (c is not None and c < minC):
                            minC = c

        return minC

    def __get_pin_from_wire(self,wire):
        if len(wire.get_in()) !=0:
            return wire.get_in()[0]
        elif len(wire.get_out()) !=0:
            return wire.get_out()[0]
        else:
            return None

