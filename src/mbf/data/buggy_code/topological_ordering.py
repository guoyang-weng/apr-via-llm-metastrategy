###Buggy code###
def topological_ordering(nodes):
    ordered_nodes = [node for node in nodes if not node.incoming_nodes]
    for node in ordered_nodes:
        for nextnode in node.outgoing_nodes:
            if set(ordered_nodes).issuperset(nextnode.outgoing_nodes) and nextnode not in ordered_nodes:
                ordered_nodes.append(nextnode)
    return ordered_nodes
###Input###
    # five = Node(5)
    # seven = Node(7)
    # three = Node(3)
    # eleven = Node(11)
    # eight = Node(8)
    # two = Node(2)
    # nine = Node(9)
    # ten = Node(10)
    # five.outgoing_nodes = [eleven]
    # seven.outgoing_nodes = [eleven, eight]
    # three.outgoing_nodes = [eight, ten]
    # eleven.incoming_nodes = [five, seven]
    # eleven.outgoing_nodes = [two, nine, ten]
    # eight.incoming_nodes = [seven, three]
    # eight.outgoing_nodes = [nine]
    # two.incoming_nodes = [eleven]
    # nine.incoming_nodes = [eleven, eight]
    # ten.incoming_nodes = [eleven, three]
	# nodes = [five, seven, three, eleven, eight, two, nine, ten]
###Actual output###
#	nodes = [five, seven, three, ten]
###Expected output###
#	nodes = [five, seven, three, eleven, eight, ten, two, nine]
