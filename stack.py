import time
import os

# ── 스택 클래스 선언 ──────────────────────────
class Stack:
    def __init__(self):
        self.data = []

    def push(self, item):
        if len(self.data) >= 10:
            print(f"  ⚠️  스택이 가득 찼습니다! push 불가")
            time.sleep(1.5)
            return
        self.data.append(item)

    def pop(self):
        if self.is_empty():
            print("  ⚠️  스택이 비어있습니다! pop 불가")
            time.sleep(1.5)
            return None
        return self.data.pop()

    def top(self):
        if self.is_empty():
            return None
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)

# ── 스택 상태 출력 ────────────────────────────
def print_stack(stack, operation=""):
    os.system('clear' if os.name == 'posix' else 'cls')
    print("=" * 40)
    print(f"  연산: {operation}")
    print("=" * 40)
    print("         [ 스택 상태 ]")
    print("         ┌────────────┐")
    if stack.is_empty():
        print("         │  (비어있음) │")
    else:
        for item in reversed(stack.data):
            print(f"         │  {item:<10}│")
    print("         └────────────┘")
    print(f"  크기: {stack.size()} / 10")
    print("=" * 40)
    time.sleep(1.5)

# ── 메인 애니메이션 ───────────────────────────
s = Stack()
print_stack(s, "Stack 선언 (비어있음)")

s.push("산책")
print_stack(s, 'push("산책")  ← 안서영')

s.push("드립커피")
print_stack(s, 'push("드립커피")  ← 안서영')

s.push("우드")
print_stack(s, 'push("우드")  ← 안서영')

print_stack(s, f'top() → "{s.top()}"')

s.push("수플레")
print_stack(s, 'push("수플레")  ← 강예은')

s.push("라떼")
print_stack(s, 'push("라떼")  ← 강예은')

popped = s.pop()
print_stack(s, f'pop() → "{popped}" 제거')

s.push("가로수")
print_stack(s, 'push("가로수")  ← 강예은')

s.push("개나리")
print_stack(s, 'push("개나리")  ← 김예준')

print_stack(s, f'top() → "{s.top()}"')

popped = s.pop()
print_stack(s, f'pop() → "{popped}" 제거')

s.push("중간고사")
print_stack(s, 'push("중간고사")  ← 김예준')

s.push("스타벅스")
print_stack(s, 'push("스타벅스")  ← 김예준')

popped = s.pop()
print_stack(s, f'pop() → "{popped}" 제거')

s.push("나들이")
print_stack(s, 'push("나들이")  ← 김승현')

s.push("차")
print_stack(s, 'push("차")  ← 김승현')

popped = s.pop()
print_stack(s, f'pop() → "{popped}" 제거')

s.push("한강")
print_stack(s, 'push("한강")  ← 김승현')

s.push("핑크")
print_stack(s, 'push("핑크")  ← 오정현')

print_stack(s, f'top() → "{s.top()}"')

popped = s.pop()
print_stack(s, f'pop() → "{popped}" 제거')

s.push("개강")
print_stack(s, 'push("개강")  ← 오정현')

popped = s.pop()
print_stack(s, f'pop() → "{popped}" 제거')

s.push("꽃놀이")
print_stack(s, 'push("꽃놀이")  ← 오정현')

popped = s.pop()
print_stack(s, f'pop() → "{popped}" 제거')

s.push("커피")
print_stack(s, 'push("커피")  ← 정인선')

s.push("향기")
print_stack(s, 'push("향기")  ← 정인선')

popped = s.pop()
print_stack(s, f'pop() → "{popped}" 제거')

s.push("민들레")
print_stack(s, 'push("민들레")  ← 정인선')

print_stack(s, f'top() → "{s.top()}"')

print("  ✅ 애니메이션 종료!")
print(f"  최종 스택 크기: {s.size()}")
