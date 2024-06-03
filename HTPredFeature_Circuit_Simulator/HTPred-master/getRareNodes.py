
def gr1(mighty_raju_list, super_list_gates):
    list_rare_nodes = []
    for i in super_list_gates:
        p0, p1 = super_list_gates[i]["P0"], super_list_gates[i]["P1"]
        rare_node_factor = p0-p1
        if(rare_node_factor<0):
            super_list_gates[i].update({"Rare_Node_Factor":abs(rare_node_factor), "Rare_towards":0})
        else:
            super_list_gates[i].update({"Rare_Node_Factor": abs(rare_node_factor), "Rare_towards": 1})

        if(abs(rare_node_factor))>0.9:
            list_rare_nodes.append(i)

    return list_rare_nodes