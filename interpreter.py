class BrainfuckInterpreter:
    def __init__(self, code):
        self.code = self.clean_code(code)
        self.tape = [0] * 30000
        self.ptr = 0  # data pointer
        self.pc = 0   # program counter
        self.bracket_map = self.build_bracket_map()

    def clean_code(self, code):
        return [c for c in code if c in "+-<>[],."]

    def build_bracket_map(self):
        stack = []
        bracket_map = {}
        for i, c in enumerate(self.code):
            if c == '[':
                stack.append(i)
            elif c == ']':
                start = stack.pop()
                bracket_map[start] = i
                bracket_map[i] = start
        return bracket_map

    def run(self):
        while self.pc < len(self.code):
            cmd = self.code[self.pc]

            if cmd == '>':
                self.ptr += 1
            elif cmd == '<':
                self.ptr -= 1
            elif cmd == '+':
                self.tape[self.ptr] = (self.tape[self.ptr] + 1) % 256
            elif cmd == '-':
                self.tape[self.ptr] = (self.tape[self.ptr] - 1) % 256
            elif cmd == '.':
                print(chr(self.tape[self.ptr]), end='')
            elif cmd == ',':
                self.tape[self.ptr] = ord(input("Input one char: ")[0])
            elif cmd == '[':
                if self.tape[self.ptr] == 0:
                    self.pc = self.bracket_map[self.pc]
            elif cmd == ']':
                if self.tape[self.ptr] != 0:
                    self.pc = self.bracket_map[self.pc]

            self.pc += 1

