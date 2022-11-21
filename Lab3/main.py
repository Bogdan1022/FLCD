states = []
final_states = []
initial_state = []
transitions = []
alphabet = []
f = open("automation.txt", "r")
automation = f.read().split("\n")
for line in automation:
    split_line = line.split("->")
    a = split_line[0]
    b = split_line[1]
    tmpstate = a.split(",")[0][1:]
    alph = a.split(",")[1][0:-1]
    if alph not in alphabet:
        alphabet.append(alph)
    if tmpstate not in states:
        if tmpstate[0] == "{":
           tmpstate = tmpstate[1:-1]
           if tmpstate not in initial_state:
               initial_state.append(tmpstate)
        states.append(tmpstate)
    if b[0] == "[":
        if b[1:-1] not in final_states:
            final_states.append(b[1:-1])
    transitions.append([tmpstate, b[1:-1]])
print("Set of states: ")
print(states)
print("Alphabet: ")
print(alphabet)
print("Final states: ")
print(final_states)
print("Transition: ")
print(transitions)
print("Initial  state: ")
print(initial_state)