import time
import os


class Stack:
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)


def print_stack(stack, operation=""):
    os.system('clear' if os.name == 'posix' else 'cls')
    print("=" * 30)
    print(f"  연산: {operation}")
    print("=" * 30)
    print("       [ 스택 상태 ]")
    print("       ┌──────────┐")
    if stack.is_empty():
        print("       │  (비어있음) │")
    else:
        for item in reversed(stack.data):
            print(f"       │  {item:<8}│")
    print("       └──────────┘")
    print(f"  크기: {stack.size()}")
    print("=" * 30)
    time.sleep(1.5)


s = Stack()
print_stack(s, "stack 선언")

s.push("벚꽃")
print_stack(s, 'push("벚꽃")')

s.push("커피")
print_stack(s, 'push("커피")')

s.push("향기")
print_stack(s, 'push("향기")')

print(f"  top = {s.top()}")
print_stack(s, f'top() → "{s.top()}"')

popped = s.pop()
print_stack(s, f'pop() → "{popped}" 제거')

s.push("봄바람")
print_stack(s, 'push("봄바람")')

s.push("라떼")
print_stack(s, 'push("라떼")')

popped2 = s.pop()
print_stack(s, f'pop() → "{popped2}" 제거')

print("애니메이션 종료!")
