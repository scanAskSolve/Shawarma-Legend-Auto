from image_contorller import get_windows, get_location
from click import single_click,long_press


def start_day():
    rect = get_windows()
    found, center = get_location("image/startADayA.png")

    if found:
        print(f"中心坐标：{center}")
        long_press(rect.x() + center[0], rect.y() + center[1],duration=1)
        single_click(rect.x() + center[0], rect.y() + center[1])
    else:
        print("未找到匹配图案")


# start_day()

def restock_shawaema():
    rect = get_windows()
    found, center = get_location("image/knife.png")

    if found:
        print(f"中心坐标：{center}")
        long_press(rect.x() + center[0], rect.y() + center[1],duration=20)
        # single_click(rect.x() + center[0], rect.y() + center[1])
    else:
        print("未找到匹配图案")

restock_shawaema()


