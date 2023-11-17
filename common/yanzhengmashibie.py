import pytesseract
from PIL import Image

# 打开验证码图片
captcha_image = Image.open('captcha.png')

# 使用 OCR 对验证码图片进行识别
captcha_text = pytesseract.image_to_string(captcha_image)

# 输出识别结果
print(captcha_text)