import tkinter as tk

# 색상 그라데이션 계산 함수
def color_gradient(ratio):
    red = int(255 * (1 - ratio))
    green = int(255 * ratio)
    return f"#{red:02x}{green:02x}00"

# 타이머 업데이트 함수
def update_timer():
    global remaining_time, timer_id

    if remaining_time > 0:
        remaining_time -= 0.01  # 10ms마다 감소
        ratio = remaining_time / total_time

        # 막대의 길이와 색상 업데이트
        current_length = int(timer_width * ratio)
        color = color_gradient(ratio)

        # 중앙 직사각형
        canvas.coords(timer_rect, timer_x + radius, timer_y, timer_x + radius + current_length, timer_y + timer_height)

        # 오른쪽 끝 원의 위치 조정
        canvas.coords(right_circle, timer_x + radius + current_length - radius, timer_y, 
                      timer_x + radius + current_length + radius, timer_y + timer_height)

        # 색상 변경
        canvas.itemconfig(timer_rect, fill=color)
        canvas.itemconfig(left_circle, fill=color)
        canvas.itemconfig(right_circle, fill=color)

        # 10ms 후 다시 호출
        timer_id = root.after(10, update_timer)
    else:
        # 시간이 다 되면 메시지 표시
        canvas.create_text(250, 150, text="Time's up!", font=("Arial", 24), fill="red")

# 타이머 초기화 함수
def start_timer():
    global remaining_time, timer_id

    # 이전 타이머 중지
    if timer_id is not None:
        root.after_cancel(timer_id)

    # 초기화
    remaining_time = total_time

    # 초기 모양 복원
    canvas.coords(timer_rect, timer_x + radius, timer_y, timer_x + timer_width - radius, timer_y + timer_height)
    canvas.coords(left_circle, timer_x, timer_y, timer_x + 2 * radius, timer_y + timer_height)
    canvas.coords(right_circle, timer_x + timer_width - 2 * radius, timer_y, timer_x + timer_width, timer_y + timer_height)

    # 색상 초기화
    initial_color = color_gradient(1)
    canvas.itemconfig(timer_rect, fill=initial_color)
    canvas.itemconfig(left_circle, fill=initial_color)
    canvas.itemconfig(right_circle, fill=initial_color)

    # 타이머 시작
    update_timer()

# Tkinter 초기화
root = tk.Tk()
root.title("둥근 양끝 타이머")
root.geometry("500x300")

# Canvas 설정
canvas = tk.Canvas(root, width=500, height=300, bg="white")
canvas.pack()

# 타이머 변수
total_time = 10  # 총 시간 (초)
remaining_time = total_time
timer_width = 400
timer_height = 30
radius = timer_height // 2
timer_x, timer_y = 50, 100
timer_id = None

# 둥근 타이머 바 생성
initial_color = color_gradient(1)
timer_rect = canvas.create_rectangle(timer_x + radius, timer_y, timer_x + timer_width - radius, timer_y + timer_height, fill=initial_color, outline="")
left_circle = canvas.create_oval(timer_x, timer_y, timer_x + 2 * radius, timer_y + timer_height, fill=initial_color, outline="")
right_circle = canvas.create_oval(timer_x + timer_width - 2 * radius, timer_y, timer_x + timer_width, timer_y + timer_height, fill=initial_color, outline="")

# 시작 버튼
start_button = tk.Button(root, text="Start Timer", command=start_timer)
start_button.pack(pady=20)

# 메인 루프
root.mainloop()
    