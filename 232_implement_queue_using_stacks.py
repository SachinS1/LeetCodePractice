

class MyQueue:

    def __init__(self):
        self.input = []

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        a = self.input[0]
        self.input = self.input[1:]
        return a

    def peek(self) -> int:
        return self.input[0] if self.input[0] else None

    def empty(self) -> bool:
        return True if len(self.input) == 0 else False