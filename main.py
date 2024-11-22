from tkinter import *
import pygame
import random
from PIL import Image, ImageTk, ImageEnhance

# 기본 설정
win = Tk()
pygame.init()
win.attributes('-fullscreen', True)
win.title("Brain Test")
win.option_add("*Font", "함초롬바탕확장")
win.bind("<Escape>", lambda event: win.attributes("-fullscreen", False))
win.geometry("1530x1280")

# 앱 크기 설정 불가
win.resizable(False, False)

# 프레임 생성
msf = Frame(win, width=1550, height=1280, relief="solid", bd=0, bg="black")
ms = Frame(win, width=1550, height=1280, relief="flat", bd=5, bg="white")
mg = Frame(win, width=1550, height=1280, relief="flat", bd=5, bg="white")
htp = Frame(win, width=1000, height=800, relief="solid", bd=2, bg="gray")
boxes = Frame(mg, width=1200, height=800, relief="solid", bd=3, bg="white")
choosedifficulties = Frame(win, width=1550, height=1280, relief="solid", bg="white", bd=2)

# 프레임 크기 고정
choosedifficulties.grid_propagate(False)
msf.grid_propagate(False)
ms.grid_propagate(False)
mg.grid_propagate(False)
htp.grid_propagate(False)
boxes.grid_propagate(False)
htp.place(x=300,y=40)
htp.place_forget()

# 캔버스
canvas = Canvas(mg, width=400,height=100,bg="white")
canvas.place(x=500,y=700)

total_time = 15
remaining_time = total_time
timer_width = 350
timer_height = 30
radius = timer_height // 2
timer_x, timer_y = 0, 35
timer_id = None

def color_gradient(ratio):
    red = int(255 * (1 - ratio))
    green = int(255 * ratio)
    return f"#{red:02x}{green:02x}00"

def update_timer():
    
    global remaining_time, timer_id

    if remaining_time > 0:
        remaining_time -= 0.01
        ratio = remaining_time / total_time

        current_length = int(timer_width * ratio)
        color = color_gradient(ratio)

        canvas.coords(timer_rect, timer_x + radius, timer_y, timer_x + radius + current_length, timer_y + timer_height)

        canvas.coords(right_circle, timer_x + radius + current_length - radius, timer_y, 
                        timer_x + radius + current_length + radius, timer_y + timer_height)

        canvas.itemconfig(timer_rect, fill=color)
        canvas.itemconfig(left_circle, fill=color)
        canvas.itemconfig(right_circle, fill=color)

        timer_id = win.after(10, update_timer)
    else:
        exitProject()

def start_timer():
    global remaining_time, timer_id

    if timer_id is not None:
        win.after_cancel(timer_id)

    remaining_time = total_time

    canvas.coords(timer_rect, timer_x + radius, timer_y, timer_x + timer_width - radius, timer_y + timer_height)
    canvas.coords(left_circle, timer_x, timer_y, timer_x + 2 * radius, timer_y + timer_height)
    canvas.coords(right_circle, timer_x + timer_width - 2 * radius, timer_y, timer_x + timer_width, timer_y + timer_height)

    initial_color = color_gradient(1)
    canvas.itemconfig(timer_rect, fill=initial_color)
    canvas.itemconfig(left_circle, fill=initial_color)
    canvas.itemconfig(right_circle, fill=initial_color)

    update_timer()

initial_color = color_gradient(1)
timer_rect = canvas.create_rectangle(timer_x + radius, timer_y, timer_x + timer_width - radius, timer_y + timer_height, fill=initial_color, outline="")
left_circle = canvas.create_oval(timer_x, timer_y, timer_x + 2 * radius, timer_y + timer_height, fill=initial_color, outline="")
right_circle = canvas.create_oval(timer_x + timer_width - 2 * radius, timer_y, timer_x + timer_width, timer_y + timer_height, fill=initial_color, outline="")

# wav 로드
ramenBgm = pygame.mixer.Sound("bgms/슈의 라면가게 브금.wav")
meownga = pygame.mixer.Sound("bgms/meow-meow-n-gga.wav")
kang = pygame.mixer.Sound("bgms/[뉴진스] 언니들만 계속 쳐다보는 강해rrr륀.wav")
nintendo = pygame.mixer.Sound("bgms/nintendo.wav")
countdownbgm = pygame.mixer.Sound("bgms/Countdown 3 seconds timer.wav")

# 이미지 로드

cat = Image.open("imgs/강고양.jpeg").resize((600,800))
blackcat = ImageTk.PhotoImage(Image.open("imgs/black cat.jpg").resize((600,800)))
yellowbox = Image.open("imgs/yellowbox.jpg")
pinkbox = Image.open("imgs/pinkbox.jpg")
purplebox = Image.open("imgs/purplebox.png")
lightpinkbox = Image.open("imgs/lightpinkbox.png")
redbox = Image.open("imgs/redbox.png")
blackbox = Image.open("imgs/blackbox.png")
emptybox = Image.open("imgs/emptybox.png")
cancelbutton = ImageTk.PhotoImage(Image.open("imgs/cancelbutton.png").resize((100,100)))
easy = ImageTk.PhotoImage(Image.open("imgs/easy.jpeg").resize((400,300)))
normal = ImageTk.PhotoImage(Image.open("imgs/normal.jpeg").resize((400,300)))
hard = ImageTk.PhotoImage(Image.open("imgs/hard.jpeg").resize((400,300)))
settingbutton = ImageTk.PhotoImage(Image.open("imgs/setting.png").resize((100,100)))

# 페이드 이미지

mainImageAlpha = 0.0
faded_image = ImageTk.PhotoImage(cat)
mainImage = Label(msf, image=faded_image, bg="black")
mainImage.place(x=500,y=125)

boxcolors = ["black", "lightpink", "pink", "red", "purple", "yellow"]
pattern = list()

# 로직

# 이지 모드

c = ImageTk.PhotoImage(Image.open("imgs/timer.png").resize((100,100)))

def easygame():

    global boxcolors, p, b, r, lp, y, pur, pattern, timer_remaining_time, c
    start_timer()
    timer_remaining_time = 30
    countdownbgm.play()
    boxes.config(width=505, height=505)
    clock = Label(mg, image=c)
    clock.place(x=900,y=700)

    chamjo = boxcolors
    choosedifficulties.place_forget()
    mg.place(x=0,y=0)
    boxes.grid(row=0, column=1, padx=500, pady=150)
    usedcolors = list()
    p = ImageTk.PhotoImage(pinkbox.resize((150,150)))
    b = ImageTk.PhotoImage(blackbox.resize((150,150)))
    r = ImageTk.PhotoImage(redbox.resize((150,150)))
    lp = ImageTk.PhotoImage(lightpinkbox.resize((150,150)))
    y = ImageTk.PhotoImage(yellowbox.resize((150,150)))
    pur = ImageTk.PhotoImage(purplebox.resize((150,150)))

    for _ in range(3):
        chosencolor = random.choice(chamjo)
        usedcolors.append(chosencolor)
        chamjo.remove(chosencolor)
    
    for i in range(3):  
        for j in range(3):
            tmp = random.choice(usedcolors)
            if tmp == "pink":
                Label(boxes, image=p, borderwidth=3, relief="solid").grid(row=i, column=j, padx=5, pady=5)
            elif tmp == "black":
                Label(boxes, image=b, borderwidth=3, relief="solid").grid(row=i, column=j, padx=5, pady=5)
            elif tmp == "lightpink":
                Label(boxes, image=lp, borderwidth=3, relief="solid").grid(row=i, column=j, padx=5, pady=5)
            elif tmp == "red":
                Label(boxes, image=r, borderwidth=3, relief="solid").grid(row=i, column=j, padx=5, pady=5)
            elif tmp == "purple":
                Label(boxes, image=pur, borderwidth=3, relief="solid").grid(row=i, column=j, padx=5, pady=5)
            elif tmp == "yellow":
                Label(boxes, image=y, borderwidth=3, relief="solid").grid(row=i, column=j, padx=5, pady=5)

# 노멀 모드

def normalgame():
    global boxcolors
    chamjo = boxcolors
    choosedifficulties.place_forget()
    mg.tkraise()
    boxes.tkraise()
    usedcolors = list()

    for i in range(5):
        chosencolor = random.choice(chamjo)
        usedcolors.append(chosencolor)
        chamjo.remove(chosencolor)

# 하드 모드

def hardgame():

    global boxcolors
    chamjo = boxcolors
    usedcolors = list()
    choosedifficulties.place_forget()
    mg.tkraise()
    boxes.tkraise()

    for _ in range(7):
        chosencolor = random.choice(chamjo)
        usedcolors.append(chosencolor)
        chamjo.remove(chosencolor)

# 난이도 선택 창

def choosingdifficulty():
    ramenBgm.stop()
    nintendo.play(-1)
    ms.place_forget()
    choosedifficulties.place(x=0,y=0)
    choosedifficulties.tkraise()
    
    Label(choosedifficulties, text="난이도를 선택해주세요", bg="white").place(x=600,y=20)
    easy_label = Button(choosedifficulties, image=easy, cursor="dot", command=easygame)
    easy_label.place(x=100, y=150)
    
    normal_label = Button(choosedifficulties, image=normal, cursor="dot", command=normalgame)
    normal_label.place(x=550, y=150)
    
    hard_label = Button(choosedifficulties, image=hard, cursor="dot", command=hardgame)
    hard_label.place(x=1000, y=150)
    Label(choosedifficulties, text="이지", font=("함초롬바탕확장", 35), bg="white").place(x=220, y=500)
    Label(choosedifficulties, text="노멀", font=("함초롬바탕확장", 35), bg="white").place(x=700, y=500)
    Label(choosedifficulties, text="하드", font=("함초롬바탕확장", 35), bg="white").place(x=1180, y=500)
    Label(choosedifficulties, text="쉬운모드입니다. 시간이 넉넉하고 3x3타일로\n 게임을 진행합니다.", bg="white").place(x=90, y=600)
    Label(choosedifficulties, text="보통의 난이도, 5x5타일로 게임을 진행합니다.", bg="white").place(x=550, y=600)
    Label(choosedifficulties, text="어렵습니ㅏㄷ. 7x7타일로 게임을 진행합니다.\n 천재가 되.", bg="white").place(x=1000, y=600)

# 설명창

def tutorial():
    htp.place(x=300,y=40)
    htp.tkraise()
    Button(htp, image=cancelbutton, bg="gray", command=lambda: htp.place_forget(), cursor="dot").place(x=880, y=30)

# 나가기

def exitProject():
    global blackcat
    
    ramenBgm.stop()
    meownga.play()
    label = Label(win, image=blackcat)
    label.place(x=500,y=0)
    win.after(1205, exit)

# 인트로 페이드인

def fadein():
    global mainImageAlpha, faded_image
    
    msf.place(x=0,y=0)
    msf.tkraise()
    if mainImageAlpha < 1:
        faded_image = ImageTk.PhotoImage(ImageEnhance.Brightness(cat).enhance(mainImageAlpha))
        mainImage.config(image=faded_image)
        mainImageAlpha += 0.1
        win.after(100, fadein)
    else:
        win.after(2000, fadeout)

# 인트로 페이드 아웃

def fadeout():
    
    global mainImageAlpha, faded_image

    if mainImageAlpha > 0:
        faded_image = ImageTk.PhotoImage(ImageEnhance.Brightness(cat).enhance(mainImageAlpha))
        mainImage.config(image=faded_image)
        mainImageAlpha -= 0.1
        win.after(100, fadeout)
    else:
        mainImage.config(image="")
        mainScreen()

# 메인창
    
def mainScreen():
    msf.place_forget()
    ms.tkraise()
    ms.place(x=0,y=0)
    ramenBgm.play(-1)
    Label(ms, text="Brain Test", font=("궁서체", 70), bg="white").place(x=100,y=200)
    Button(ms, text="play", font=("함초롬바탕확장", 30), bg="gray", command=choosingdifficulty, cursor="dot").place(x=100, y=500, width=100, height=70)
    Button(ms, text="exit", font=("함초롬바탕확장", 30), bg="gray", command=exitProject, cursor="dot").place(x=100, y=600, width=100, height=70)
    Button(ms, text="how to play", font=("함초롬바탕확장", 30), bg="gray", command=tutorial, cursor="dot").place(x=100, y=700, width=260, height=70)

win.after(1000, kang.play)
win.after(3700, kang.stop)

## juseok for test
# fadein()

fadeout()

# 메인루프
win.mainloop()