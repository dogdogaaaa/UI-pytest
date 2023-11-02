from PIL import Image
"""
验证图片是否被损坏
"""

def check_image_file(filepath):
    try:
        with Image.open(filepath) as img:
            img.verify()
    except OSError:
        return False
    return True


print(check_image_file("crop_pic.png"))
print(check_image_file("1.png"))



