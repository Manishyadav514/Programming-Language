print("===========================USING CLASS=====================")
String = "aabb"
transition_function = {
      ('q', 'a', 'Z'): ('q', 'XZ'),
      ('q', 'a', 'X'): ('q', 'XX'),
      ('q', 'b', 'X'): ('p', 'ε'),
      ('p', 'b', 'X'): ('p', 'ε'),
      ('p', 'ε', 'Z'): ('acc', 'Z'),
    }
class DoubleStackDPDA:

    def __init__(self, trf, input, state):
        self.head = 0
        self.trf = {}
        self.trf = trf
        self.state = str(state)
        self.input = input
        self.stack = ['Z']

    def step(self):
        a = self.input[self.head]
        s = self.stack.pop()
        state, ss = self.trf.get((self.state, a, s))
        if ss != 'ε':
            for s in ss[::-1]:
                self.stack.append(s)
        self.state = state
        print('{:20s} [{:10s}] {:5s}'.format(self.input[self.head:],
                                             ''.join(self.stack), self.state))
        self.head += 1

    def run(self):

        print('{:20s} [{:10s}] {:5s}'.format(self.input[self.head:],
                                             ''.join(self.stack), self.state))
        while self.head < len(self.input):
            self.step()

        s = self.stack.pop()
        if self.trf.get((self.state, 'ε', s)):
            state, ss = self.trf.get((self.state, 'ε', s))
            self.state = state
            print('{:20s} [{:10s}] {:5s}'.format('ε',
                                                 ''.join(self.stack), self.state))


# run DPDA to accept the input string a^nb^n
DoubleStackDPDA(
    transition_function,
    String, 'q').run()





print("===========================USING FUNCTION=====================")
string = "aabb"
transition_function = {
      ('q', 'a', 'Z'): ('q', 'XZ'),
      ('q', 'a', 'X'): ('q', 'XX'),
      ('q', 'b', 'X'): ('p', 'ε'),
      ('p', 'b', 'X'): ('p', 'ε'),
      ('p', 'ε', 'Z'): ('acc', 'Z'),
    }
def DStackPDA(trf, input, state):
    head = 0
    state = str(state)
    stack = ['Z']
    print('{:20s} [{:10s}] {:5s}'.format(input[head:], ''.join(stack),state))
    while head < len(input):
        # self.step()
        a = input[head]
        s = stack.pop()
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

DStackPDA(transition_function,string, 'q')




