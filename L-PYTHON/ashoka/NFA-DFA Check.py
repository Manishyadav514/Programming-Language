from automata.fa.nfa import NFA


# NFA which matches strings beginning with 'a', ending with 'a', and containing no consecutive 'b's
nfa = NFA(
    states={'q0', 'q1', 'q2'},
    input_symbols={'a', 'b'},
    transitions={
        'q0': {'a': {'q1'}},
        'q1': {'a': {'q1'}, '': {'q2'}}, # Use '' as the key name for empty string (lambda/epsilon) transitions
        'q2': {'b': {'q0'}}
    },
    initial_state='q0',
    final_states={'q1'}
)
if nfa.accepts_input('abba'):
    print('accepted')
else:
    print('rejected')



# NEW APPROACH
#nfa simulation for (a|b)*abb
# NFA simulation for (a+b)*b(a+b) which is same as (a|b)*b(a|b)
#state 4 is a trap state

import sys
def main():
    transition = [[[0,1],[0]], [[4],[2]], [[4],[3]], [[4],[4]]]
    input = ["a","a","b","b"]
    input = list(input) #copy the input in list because python strings are immutable and thus can't be changed directly
    for index in range(len(input)): #parse the string of a,b in 0,1 for simplicity
        if input[index]=='a':
            input[index]='0'
        else:
            input[index]='1'
    final = "3" #set of final states = {3}
    start = 0
    i=0  #counter to remember the number of symbols read

    trans(transition, input, final, start, i)
    print("rejected")
def trans(transition, input, final, state, i):
    for j in range (len(input)):
        for each in transition[state][int(input[j])]: #check for each possibility
            if each < 4:                              #move further only if you are at non-hypothetical state
                state = each
                if j == len(input)-1 and (str(state) in final): #last symbol is read and current state lies in the set of final states
                    print("accepted")
                    sys.exit()
                trans(transition, input[i+1:], final, state, i) #input string for next transition is input[i+1:]
        i = i+1 #increment the counter
main()




# SECOND WAY -EASY PEASY
dfa = {0:{'0':0, '1':1},
       1:{'0':2, '1':0},
       2:{'0':1, '1':2}}
def accepts(transitions, initial, accepting, s):
    state = initial
    for c in s:
        state = transitions[state][c]
    return state in accepting
if accepts(dfa, 0, {0},'10111011'):
    print("accepted")
else:
    print('rejected')


