
import json

def build_graph(target):

    nodes = [
        {"id":1,"label":target,"type":"target"},
        {"id":2,"label":"Email","type":"email"},
        {"id":3,"label":"IP Address","type":"ip"},
        {"id":4,"label":"Domain","type":"domain"},
        {"id":5,"label":"Username","type":"username"}
    ]

    edges = [
        {"from":1,"to":2},
        {"from":1,"to":3},
        {"from":1,"to":4},
        {"from":1,"to":5}
    ]

    graph = {
        "nodes":nodes,
        "edges":edges
    }

    return graph
