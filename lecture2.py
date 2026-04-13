# Environment, Location A, B
''' Lesson 2: Table Driven, Reflex and Simple Reflex Agents '''
A = (1, 0)
B = (0, 1)

# perceptin history
history = []

table = {
    ((A, "Clean"),) : "Right",
    ((A, "Dirty"),) : "Clean",
    ((B, "Clean"),) : "Left",
    ((B, "Dirty"),) : "Clean",

    ((A, "Dirty"), (A, "Clean")) : "Right",
    ((B, "Dirty"), (B, "Clean")) : "Left",

    ((A, "Dirty"), (A, "Clean"), (B, "Dirty")) : "Clean",
}

def lookup_table(history):
    action = table.get(tuple(history))
    return action

def table_driven_agent(percept):
    history.append(percept)
    action = lookup_table(history)
    return action

def run():
    print( table_driven_agent((A, "Dirty")),  )
    print( table_driven_agent((A, "Clean")),  )
    print( table_driven_agent((B, "Dirty")),  )

run()



A = 'A'
B = 'B'

def reflex_vacuum_agent(percept):
    location, status = percept

    if status == "Dirty":
        return 'Clean'
    elif location == A:
        return 'Right'
    elif location == B:
        return 'Left'

def run():
    print("A Dirty:", reflex_vacuum_agent((A, 'Dirty')), )
    print("A Clean:", reflex_vacuum_agent((A, 'Clean')), )
    print("B Dirty:", reflex_vacuum_agent((B, 'Dirty')), )
    print("B Clean:", reflex_vacuum_agent((B, 'Clean')), )



A = (0,0)
B = (0,1)

rules = {
    (A, "Dirty") : "Clean",
    (A, "Clean") : "Right",
    (B, "Dirty") : "Clean",
    (B, "Clean") : "Left",
}
def interpret_input(percept):
    # later can be real input/complex perception
    return percept

def rule_match(state, rules):
    return rules.get(state)

def simple_reflex_agent(percept):
    state = interpret_input(percept)
    action = rule_match(state, rules)
    return action

def run():
    print( simple_reflex_agent((A, "Dirty")),  )
    print( simple_reflex_agent((A, "Clean")),  )
    print( simple_reflex_agent((B, "Dirty")),  )
    print( simple_reflex_agent((B, "Clean")),  )

run()

