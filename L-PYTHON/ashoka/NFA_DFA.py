# REGULAR EXPRESSION (a+b)*b(a+b) can be written as as (a|b)*b(a|b)
string = 'babb'

# NFA transition state
nfa_state_transition = {
    0 : {'a': 0, 'b': 0, 'b': 1},
    1 : {'a': 2, 'b':2}
    }

# DFA transition state
dfa_state_transition = {
    0 : {'a': 0, 'b': 1},
    1 : {'a': 2, 'b': 3},
    2 : {'a': 0, 'b': 1},
    3 : {'a': 2, 'b': 3}
    }

def accepts(transitions, initial, accepting, s):
    state = initial
    acceptable_status = True
    try:
        for c in s:
            print(state, c)
            state = transitions[state][c]
        if state not in accepting:
            acceptable_status = False
    except:
        acceptable_status = False
    return acceptable_status

if accepts(nfa_state_transition, 0, {2},string):
    print("accepted in NFA transition")
else:
    print('rejected')

if accepts(dfa_state_transition, 0, {2,3},string):
    print("accepted in DFA transition")
else:
    print('rejected')

