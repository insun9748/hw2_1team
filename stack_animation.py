import time

# 3) stack 선언부터 시작
stack = []

def display_stack(action):
    """스택의 현재 상태를 에니메이션처럼 출력하는 함수"""
    print(f"\n[ {action} ]")
    print("------- TOP -------")
    for item in reversed(stack):
        print(f"  {item}")
    print("----- BOTTOM -----")
    print(f"현재 크기: {len(stack)}/10")
    time.sleep(0.8) # 5) 에니메이션 효과를 위한 지연

# 2) push, pop, top 연산 함수 정의
def push(item):
    # 4) stack의 크기를 10 이하로 유지
    if len(stack) < 10:
        stack.append(item)
        display_stack(f"Push: {item}")
    else:
        print(f"⚠️ 스택이 가득 찼습니다! '{item}'을(를) 넣을 수 없어요.")

def pop():
    if stack:
        item = stack.pop()
        display_stack(f"Pop: {item}")
        return item

def top():
    if stack:
        t = stack[-1]
        print(f"\n🔍 현재 Top 확인: {t}")
        return t 

# --- 시나리오 시작 (1번의 모든 단어 사용) ---

# 1. 학기 시작과 봄의 기운
push("개강")
push("중간고사")
push("개나리")
push("민들레")
push("가로수")

# 중간고사는 빨리 없애버립시다! (LIFO 구조 활용)
pop() # 가로수 Pop
pop() # 민들레 Pop
pop() # 개나리 Pop
pop() # 중간고사 Pop (드디어 해방!)

# 2. 핑크빛 꽃놀이와 산책
push("핑크")
push("꽃놀이")
push("산책")
push("나들이")
push("한강")

# 현재 가장 위에 있는 것이 무엇인지 확인
top() # 한강 확인

# 3. 카페에서의 여유 (10 이하 유지를 위해 적절히 Pop)
pop() # 한강 Pop
pop() # 나들이 Pop

push("스타벅스")
push("커피")
push("라떼")
push("드립커피")
push("수플레")

# 공간 확보를 위해 잠시 정리
pop() # 수플레 Pop
pop() # 드립커피 Pop

push("향기")
push("우드")
push("차")

print("\n✨ 모든 단어를 사용하여 스택 나들이를 마쳤습니다!")
