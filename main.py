import pyautogui
import time
import ctypes
import random

SendInput = ctypes.windll.user32.SendInput

from locations import *

def legitClick(pos, delay=.025, endDelay=.025):
    print("legitClick (" + str(pos[0]) + ", " + str(pos[1]) + ")")
    ctypes.windll.user32.SetCursorPos(pos[0], pos[1])
    time.sleep(.035)
    pyautogui.mouseDown()
    if delay != 0:
        time.sleep(delay)
    pyautogui.mouseUp()
    if endDelay != 0:
        time.sleep(endDelay)

def clickNow(pos, delay=None):
    print("ClickNow (" + str(pos[0]) + ", " + str(pos[1]) + ")")
    ctypes.windll.user32.SetCursorPos(pos[0], pos[1])
    time.sleep(.035)
    if delay is not None:
        pyautogui.click(interval=delay)
    else:
        pyautogui.click()

# ==========================

input("게임 표시 영역의 좌상단을 " + str(globalLocationOffset[0]) + ", " + str(globalLocationOffset[1]) +
      "에 둔 뒤 Enter/Return을 누르세요.") # 더미 input

# 게임 시작 버튼
pyautogui.click(x=gameStart[0], y=gameStart[1])
time.sleep(.1)

# 의상 버튼을 전부 한번씩 누름 → 목표치를 70으로 설정
for loc in sueDressUp:
    clickNow(loc, delay=0)

# 게임 시작
legitClick(gameReallyStart)
time.sleep(.1)

for tries in range(3):
    print("Round " + str(tries))
    print("왼쪽 밀크초코")
    # 초코시럽을 가져옴
    clickNow(syrupChoco, delay=0.1)
    for loc1 in workspaceL:
        clickNow(loc1)
        legitClick(loc1, delay=.24, endDelay=0)
    # 딸기시럽을 가져옴
    print("왼쪽 딸기초코")
    clickNow(syrupBerry, delay=0.15)
    for loc1 in workspaceL:
        # 1번 뿌린다
        legitClick(loc1, delay=.1, endDelay=0)
    print("오른쪽 밀크초코")
    # 초코시럽을 가져옴
    clickNow(syrupChoco, delay=0.1)
    for loc1 in workspaceR:
        clickNow(loc1)
        legitClick(loc1, delay=.24, endDelay=0)
    print("오른쪽 딸기초코")
    # 딸기시럽을 가져옴
    clickNow(syrupBerry, delay=0.1)
    for loc1 in workspaceR:
        # 1번 뿌린다
        legitClick(loc1, delay=.1, endDelay=0)
    # 스틱 꽂기
    print("왼쪽 스틱")
    clickNow(cookieStick, delay=0.1)
    for loc1 in workspaceL:
        clickNow(loc1)
    # 냉동버튼 누르기
    print("왼쪽 냉동 시작")
    clickNow(freezeButtonL, delay=0.1)
    # 스틱 꽂기
    print("오른쪽 스틱")
    clickNow(cookieStick, delay=0.12)
    for loc1 in workspaceR:
        clickNow(loc1)
    # 냉동버튼 누르기
    print("오른쪽 냉동 시작")
    legitClick(freezeButtonR)
    # 갖다놓기(왼쪽)
    print("왼쪽 갖다놓기")
    time.sleep(1.8)
    for loc1 in workspaceL:
        clickNow(loc1, delay=0)
        clickNow((tableLocation[0] + random.randint(0, 36), tableLocation[1] - random.randint(0, 60)), delay=0)
        pyautogui.mouseUp()
        pyautogui.click()
    print("오른쪽 갖다놓기")
    for loc1 in workspaceR:
        clickNow(loc1, delay=0)
        clickNow((tableLocation[0] + random.randint(0, 36), tableLocation[1] - random.randint(0, 60)), delay=0)
        pyautogui.mouseUp()
        pyautogui.click()

print("Final Round")
# 초코시럽을 가져옴
print("왼쪽 밀크초코")
clickNow(syrupChoco, delay=0.1)
for loc1 in workspaceL:
    clickNow(loc1)
    legitClick(loc1, delay=.24, endDelay=0)
# 딸기시럽을 가져옴
print("왼쪽 딸기초코")
clickNow(syrupBerry, delay=0.15)
for loc1 in workspaceL:
    # 1번 뿌린다
    legitClick(loc1, delay=.1, endDelay=0)
# 스틱 꽂기
print("왼쪽 스틱")
clickNow(cookieStick, delay=0.1)
for loc1 in workspaceL:
    clickNow(loc1)
# 냉동버튼 누르기
print("왼쪽 냉동 시작")
clickNow(freezeButtonL, delay=0.1)
# 갖다놓기(왼쪽)
time.sleep(4)
print("왼쪽 갖다놓기")
for loc1 in workspaceL:
    clickNow(loc1, delay=0)
    clickNow((tableLocation[0] + random.randint(0, 36), tableLocation[1] - random.randint(0, 60)), delay=0)
    pyautogui.click()

print("클리어")
