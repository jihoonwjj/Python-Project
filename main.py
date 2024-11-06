from tkinter import *
import pygame
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
ms = Frame(win, width=1550, height=1280, relief="solid", bd=0)

# 프레임 크기 고정
msf.grid_propagate(False)
ms.grid_propagate(False)

msf.place(x=0, y=0)
msf.tkraise()

# 리소스 로드
cat = Image.open("imgs/강고양.jpeg").resize((600,800))
yellowbox = ImageTk.PhotoImage(Image.open("imgs/yellowbox.jpg").resize((400, 400)))
pinkbox = ImageTk.PhotoImage(Image.open("imgs/pinkbox.jpg").resize((400, 400)))

mainImageAlpha = 0.0
faded_image = ImageTk.PhotoImage(cat)
mainImage = Label(msf, image=faded_image, bg="black")
mainImage.place(x=500,y=125)

# 로직

def fadein():
    global mainImageAlpha, faded_image

    if mainImageAlpha < 1:
        faded_image = ImageTk.PhotoImage(ImageEnhance.Brightness(cat).enhance(mainImageAlpha))
        mainImage.config(image=faded_image)
        mainImageAlpha += 0.05
        win.after(100, fadein)
    else:
        win.after(2000, fadeout)

def fadeout():
    global mainImageAlpha, faded_image

    if mainImageAlpha > 0:
        faded_image = ImageTk.PhotoImage(ImageEnhance.Brightness(cat).enhance(mainImageAlpha))
        mainImage.config(image=faded_image)
        mainImageAlpha -= 0.05
        win.after(100, fadeout)
    else:
        mainImage.config(image="")
        msf.destory()

fadein()

# 메인루프
win.mainloop()