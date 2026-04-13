A= (0,0)
B = (0,1)   
C= (1,1)
history = []

table = {

    (B, "Dirty") : "Clean",
    (B, "Dirty" , "Clean") : "Left",
    ((B, "Dirty"), (A, "Dirty")) : "Clean",
    }

def lookuptable(history):
    action = table.get(tuple(history))
    return action

def table_driven_Agent(percept):
    history.append(percept)
    action = lookuptable(history)
    return action

def run():
    print(table_driven_Agent((B, "Dirty")), )
    print(table_driven_Agent((B, "Clean")), )
    print(table_driven_Agent((A, "Dirty")), )
    print(table_driven_Agent((A, "Clean")), )
    print(table_driven_Agent((B, "Clean")), )
    print(table_driven_Agent((C, "Dirty")), )
    print(table_driven_Agent((C, "Clean")), )
run()


