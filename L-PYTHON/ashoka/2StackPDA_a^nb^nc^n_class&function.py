# 2-Stack PDA for the language a^nb^nc^n

# Input String
string = "aaabbbccc"

# Transition Function
transition_function = {
      ('q0', 'a', 'Z', 'X'): ('q0', 'aZ','X'),
      ('q0', 'a', 'a', 'X'): ('q0', 'aa', 'X'),
      ('q0', 'b', 'a','X'): ('q1','ε', 'bX'),
      ('q1', 'b', 'a','b'): ('q1','ε', 'bb'),
      ('q1', 'c', 'a','b'): ('q2', 'Z','ε'),
      ('q2', 'c', 'a','b'): ('q2', 'Z','ε'),
      ('q2', 'ε', 'Z','X'): ('q3:accepted', 'Z','X'),
    }

# Function that checks input
def DStackPDA(trf, input, state):
    head = 0
    state = str(state)
    stack1 = ['Z']
    stack2 = ['X']
    s1_top=stack1[0]
    s2_top=stack2[0]
    print('{}{:14s} [{:11s},{:11s}] {:6s}'.format("String  : ",input[head:], ''.join(stack1),''.join(stack2),state))
    try:
        while head < len(input):
            a = input[head]
            # add "a" on the stack first when you see a
            if a == "a":
                s1_top = stack1.pop()
                state, st1, st2 = trf.get((state, a, s1_top, s2_top))
                if st1 != 'ε':
                    for s1_top in st1[::-1]:
                        stack1.append(s1_top)
                state = state
                print('{:}   {:20s} [{:10s} , {:10s}]  {:5s}'.format(head, input[head:], ''.join(stack1), ''.join(stack2), state))
                head += 1
            # pop "a" from stack first and append "b" on stack second.
            if a == "b":
                s1_top = stack1.pop()
                s2_top = stack2.pop()
                # print(trf.get((state, a, s1_top,s2_top)))
                state, st1, st2 = trf.get((state, a, s1_top, s2_top))
                if st2 != 'ε':
                    for s2_top in st2[::-1]:
                        stack2.append(s2_top)
                state = state
                print('{:}   {:20s} [{:10s} , {:10s}]  {:5s}'.format(head, input[head:], ''.join(stack1), ''.join(stack2), state))
                head += 1
            # Pop "b" from stack second when you see "c"
            if a == "c":
                s2_top = stack2.pop()
                # print(trf.get((state, a, s1_top,s2_top)))
                state, st1, st2 = trf.get((state, a, s1_top, s2_top))
                if st2 != 'ε':
                    for s2_top in st2[::-1]:
                        stack2.append(s2_top)
                state = state
                print('{:}   {:20s} [{:10s} , {:10s}]  {:5s}'.format(head, input[head:], ''.join(stack1), ''.join(stack2), state))

                head += 1
        # String is accepted if both the stacks are empty (or top of the stack has value Z and X respectively) at the end
        s1_top = stack1.pop()
        s2_top = stack2.pop()
        # print(s1_top, s2_top)
        if trf.get((state, 'ε', s1_top, s2_top)):
            state, st1, st2 = trf.get((state, 'ε', s1_top, s2_top))
            state = state
            print('{}   {:14s} [{:23s}] {:5s}'.format('Final :','ε', ''.join(stack1), state))
            print("String is in the language")
        else:
            print("String is not accepted")
    except:
        print("String is not in the language")

DStackPDA(transition_function,string, 'q0')












print("===========================USING CLASS=====================")
# 2-Stack PDA for the language a^nb^nc^n

# Your Input String Goes Here
string = "aabbcc"

# Transition Function
transition_function = {
      ('q0', 'a', 'Z', 'X'): ('q0', 'aZ','X'),
      ('q0', 'a', 'a', 'X'): ('q0', 'aa', 'X'),
      ('q0', 'b', 'a','X'): ('q1','a', 'bX'),
      ('q1', 'b', 'a','b'): ('q1','a', 'bb'),
      ('q1', 'c', 'a','b'): ('q2', 'ε','ε'),
      ('q2', 'c', 'a','b'): ('q2', 'ε','ε'),
      ('q2', 'ε', 'Z','X'): ('q3', 'Z','X'),
    }

# Class for 2StackPDA
class DoubleStackDPDA:
    def __init__(self, trf, input, state):
        self.head = 0
        self.trf = {}
        self.trf = trf
        self.state = str(state)
        self.input = input
        self.stack1 = ['Z']
        self.stack2 = ['X']

    def run(self):
        print('{}{:14s} [{:11s},{:11s}] {:6s}'.format("String  : ", self.input[self.head:],
                                                      ''.join(self.stack1), ''.join(self.stack2), self.state))
        s1_top = self.stack1[0]
        s2_top = self.stack2[0]
        state = self.state

        try:
            while self.head < len(self.input):
                a = self.input[self.head]
                # add "a" on the stack first when you see a
                if a == "a":
                    s1_top = self.stack1.pop()
                    state, st1, st2 = self.trf.get((state, a, s1_top, s2_top))
                    if st1 != 'ε':
                        for s1_top in st1[::-1]:
                            self.stack1.append(s1_top)
                    state = state
                    print('{:}   {:20s} [{:10s} , {:10s}]  {:5s}'.format(self.head, self.input[self.head:],
                                                                         ''.join(self.stack1), ''.join(self.stack2),
                                                                         state))
                    self.head += 1
                # pop "a" from stack first and append "b" on stack second.
                if a == "b":
                    s1_top = self.stack1.pop()
                    s2_top = self.stack2.pop()
                    # print(self.trf.get((state, a, s1_top, s2_top)))
                    state, st1, st2 = self.trf.get((state, a, s1_top, s2_top))
                    if st2 != 'ε':
                        for s2_top in st2[::-1]:
                            self.stack2.append(s2_top)
                    state = state
                    print('{:}   {:20s} [{:10s} , {:10s}]  {:5s}'.format(self.head, self.input[self.head:],
                                                                         ''.join(self.stack1), ''.join(self.stack2),
                                                                         state))
                    self.head += 1
                # Pop "b" from stack second when you see "c"
                if a == "c":
                    s2_top = self.stack2.pop()
                    # print(trf.get((state, a, s1_top,s2_top)))
                    state, st1, st2 = self.trf.get((state, a, s1_top, s2_top))
                    if st2 != 'ε':
                        for s2_top in st2[::-1]:
                            self.stack2.append(s2_top)
                    state = state
                    print('{:}   {:20s} [{:10s} , {:10s}]  {:5s}'.format(self.head, self.input[self.head:],
                                                                         ''.join(self.stack1), ''.join(self.stack2),
                                                                         state))
                    self.head += 1

            # String is accepted if both the stacks are empty (or top of the stack has value Z and X respectively) at the end
            s1_top = self.stack1.pop()
            s2_top = self.stack2.pop()
            # print(s1_top, s2_top, state)
            if self.trf.get((state, 'ε', s1_top, s2_top)):
                state, st1, st2 = self.trf.get((state, 'ε', s1_top, s2_top))
                # state = state
                print('{}   {:14s} [{:23s}] {:5s}'.format('Final :', 'ε', ''.join(self.stack1), state))
                print("String {} is in the language".format(string))
            else:
                print("String {} is not in the language".format(string))
        except:
            print("Not Accepted")
# run DPDA to accept the input string a^nb^n
DoubleStackDPDA(transition_function, string, 'q0').run()