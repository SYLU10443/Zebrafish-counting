import cv2
import numpy as np

# 加载两张图像
image1 = cv2.imread(r'')  # path to image 1
image2 = cv2.imread(r'')  # path to image 2

# 确保两张图像大小一致
image1 = cv2.resize(image1, (image2.shape[1], image2.shape[0]))

# 将图像转换为浮动类型，便于计算
image1_float = image1.astype(np.float32) / 255.0
image2_float = image2.astype(np.float32) / 255.0

# 应用“屏幕”合成模式
# 屏幕模式公式: Result = 1 - (1 - A) * (1 - B)
result = 1 - (1 - image1_float) * (1 - image2_float)

# 将结果转换回标准的图像格式（0到255之间的整数）
result = (result * 255).astype(np.uint8)

# 显示结果
# cv2.imshow('Screen Blend Result', result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# saving result
cv2.imwrite(r'', result)#result saving path
