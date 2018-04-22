class Stack:

    def __init__(self):
        self._stack = []
        self.skip_mode = False
        self.string_mode = False

    def push(self, val):
        assert isinstance(val, int), f"Can only push integers on the stack, not {val}"
        self._stack.append(val)

    def pop(self):
        if len(self._stack) == 0:
            return 0
        return self._stack.pop()
