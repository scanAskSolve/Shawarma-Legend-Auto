import sys
from image_contorller import get_windows
import cv2

def is_template_in_image(image_path, template_path, threshold=0.8):
    # 读取大图和模板图案
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    template = cv2.imread(template_path, cv2.IMREAD_COLOR)

    # 检查是否加载成功
    if image is None:
        print(f"无法读取图像文件：{image_path}")
        return False, None
    if template is None:
        print(f"无法读取模板文件：{template_path}")
        return False, None

    # 获取模板尺寸
    h, w = template.shape[:2]

    # 执行模板匹配
    result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # 判断是否找到匹配图案
    if max_val >= threshold:
        print(f"模板图案已找到，匹配度：{max_val}")

        # 获取匹配的左上和右下坐标
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)

        # 计算中心坐标
        center_x = top_left[0] + w // 2
        center_y = top_left[1] + h // 2
        center = (center_x, center_y)

        # 可视化匹配结果（在大图上绘制匹配区域）
        cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)
        cv2.circle(image, center, 5, (0, 0, 255), -1)  # 绘制中心点
        cv2.imshow("Detected Template", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        return True, center
    else:
        return False, None


get_windows()
# 使用示例

image_path = 'shawarma_legend_screenshot.png'       # 大图路径
template_path = 'image/shawarma .png'  # 模板图案路径
found, center = is_template_in_image(image_path, template_path, threshold=0.8)
if found:
    print(f"中心坐标：{center}")
else:
    print("未找到匹配图案")

