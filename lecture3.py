A = (0, 0)
B = (1, 0)

state = {
    A: "Unknown",
    B: "Unknown",
    "location": None    
}
def match_rule(memory, location):
    if memory[A] == "Clean" and memory[B] == "Clean":
        return "NoOp" # no operation
    if memory[location] == "Dirty":
        return "Clean"
    if location == A:
        return "Right"
    return "Left"

def update_state(state, location, status):
    state["location"] = location
    state[location] = status
    return state

def model_based_agent(percept):
    global state
    location, status = percept
    state = update_state(state, location, status)
    action = match_rule(state, location)
    return action

def run():
    print( model_based_agent((A, "Dirty")), state )
    print( model_based_agent((A, "Clean")), state )
    print( model_based_agent((B, "Dirty")), state )
    print( model_based_agent((B, "Clean")), state )

run()