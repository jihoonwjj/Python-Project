from tkinter import Tk, Button

# 사용 가능한 색상 리스트
colors = ["red", "green", "blue", "yellow", "purple"]

# 버튼 상태 저장용 딕셔너리
button_state = {}

# 버튼 클릭 시 색상 변경 함수
def change_color(button):
    # 현재 색상 인덱스 가져오기
    current_index = button_state[button]
    # 다음 색상 인덱스 계산 (리스트 순환)
    next_index = (current_index + 1) % len(colors)
    # 버튼 색상 변경
    button.config(bg=colors[next_index])
    # 상태 업데이트
    button_state[button] = next_index

# Tkinter UI 설정
if __name__ == "__main__":
    root = Tk()
    root.title("버튼 색상 순환")

    # 버튼 생성 및 초기화
    for i in range(5):  # 버튼 5개 생성
        btn = Button(root, text=f"버튼 {i+1}", bg=colors[0], width=15, height=2)
        btn.grid(row=i, column=0, pady=5)
        # 초기 색상 인덱스는 0
        button_state[btn] = 0
        # 버튼 클릭 시 change_color 호출
        btn.config(command=lambda b=btn: change_color(b))

    root.mainloop()
