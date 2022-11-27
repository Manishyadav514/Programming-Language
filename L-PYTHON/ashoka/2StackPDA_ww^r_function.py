# 2-Stack PDA for the language a^nb^nc^n
string = "0101001010"
transition_function = {
        ('q0', '0', 'Z'): ('q0', '0Z'),
        ('q0', '0', '0'): ('q0', '00'),
        ('q0', '1', 'Z'): ('q0', '1Z'),
        ('q0', '1', '1'): ('q0', '11'),
        ('q0', '1', '0'): ('q0', '10'),
        ('q0', '0', '1'): ('q0', '01'),
        ('q0', '0', '0'): ('q1', 'ε'),
        ('q0', '1', '1'): ('q1', 'ε'),
        ('q1', '0', '0'): ('q1', 'ε'),
        ('q1', '1', '1'): ('q1', 'ε'),
        ('q1', 'ε', 'Z'): ('q2:accepted', 'Z'),
    }
def DStackPDA(trf, input, state):
    head = 0
    state = str(state)
    stack = ['Z']
    print('{:20s} [{:10s}] {:5s}'.format(input[head:], ''.join(stack),state))
    try:
        while head < len(input):
            # self.step()
            a = input[head]
            s = stack.pop()
            # print(trf.get((state, a, s)), state, a, s)
            state, ss = trf.get((state, a, s))
            if ss != 'ε':
                for s in ss[::-1]:
                    stack.append(s)
            state = state
            print('{:20s} [{:10s}] {:5s}'.format(input[head:], ''.join(stack), state))
            head += 1
        s = stack.pop()
        if trf.get((state, 'ε', s)):
            state, ss = trf.get((state, 'ε', s))
            state = state
            print('{:20s} [{:10s}] {:5s}'.format('ε', ''.join(stack), state))
            print("String is accepted")
    except:
        print("String is not accepted")

DStackPDA(transition_function,string, 'q0')

