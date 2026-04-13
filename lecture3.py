A = (0,0)
B = (1,0)

state = {
    A: "Unknown",
    B: "Unknown",
    "location": None
}

def match_rule(memory, location):
    if memory[A] == "Clean" and memory[B] == "Clean":
        return "NoOp"
    if memory[location] == "Dirty":
        return "Clean"
    if location == A:
        return "Right"
    return "Left" 