import time

class MyClass:
    def __init__(self):
        # d-3: stack 선언부터 시작
        self.stack = []
        self.max_size = 10  # d-4: 스택 크기 10 이하 유지

    def render(self, command):
        # 온라인 컴파일러에서는 화면을 지우는 대신 구분선을 출력합니다.
        print("\n" + "="*40)
        print(f" [연산 실행]: {command}")
        print("="*40)

        # 스택 시각화 (위가 TOP이 되도록 역순 출력)
        for i in range(self.max_size - 1, -1, -1):
            if i < len(self.stack):
                is_top = " <--- TOP" if i == len(self.stack) - 1 else ""
                # f-string 정렬을 사용하여 박스 모양 유지
                print(f"  | {self.stack[i]:^12} | {is_top}")
            else:
                print("  |              |")
        
        print("  └--------------┘ (Stack Bottom)")
        time.sleep(0.8)  # 애니메이션 속도 조절

    def push(self, item):
        if len(self.stack) < self.max_size:
            self.stack.append(item)
            self.render(f"stack.push('{item}')")

    def pop(self):
        if self.stack:
            val = self.stack.pop()
            self.render(f"stack.pop() -> '{val}' 제거")

    def top(self):
        if self.stack:
            self.render(f"stack.top() 확인: '{self.stack[-1]}'")

def main():
    # Hello world 출력 (요구사항 반영)
    print("Hello world! Stack Animation Start...")
    
    app = MyClass()

    # a, b: 팀원들이 공유한 단어 데이터 (예시)
    team_words = ["꽃놀이", "핑크", "개강", "개나리", "중간고사", "스타벅스","수플레","라떼","가로수","나들이","한강","차","산책","드립커피","우드", "커피", "향기","민들레" ]

    # d-1: 모든 단어를 한번 이상 사용
    for word in team_words:
        app.push(word)

    # d-2: push, pop, top 연산 모두 사용
    app.top()
    app.pop()
    app.top()
    app.push("새로운봄날")
    
    print("\n[결과] 애니메이션이 성공적으로 종료되었습니다.")

# myCompiler 환경을 고려하여 직접 호출
main()