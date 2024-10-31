import pyautogui
import time

# 1. 单击操作
def single_click(x, y):
    pyautogui.click(x, y)

# 2. 长按操作
def long_press(x, y, duration=2):
    pyautogui.mouseDown(x, y)  # 按下鼠标
    time.sleep(duration)       # 保持按住指定秒数
    pyautogui.mouseUp()        # 松开鼠标

# 3. 按住并移动
def click_and_drag(start_x, start_y, end_x, end_y, duration=1):
    pyautogui.mouseDown(start_x, start_y)   # 按下鼠标
    pyautogui.moveTo(end_x, end_y, duration) # 移动到目标位置
    pyautogui.mouseUp()                     # 松开鼠标

# # 使用示例
# # 单击坐标 (100, 100)
# single_click(100, 100)
#
# # 长按坐标 (200, 200) 2 秒
# long_press(200, 200, duration=2)
#
# # 从 (300, 300) 按住并拖动到 (400, 400) 持续 1 秒
# click_and_drag(300, 300, 400, 400, duration=1)
