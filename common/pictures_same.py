from PIL import Image
import io


def compare_images(image1, image2):
    
    with open(image1, 'rb') as file:
        image1_data = file.read()

    with open(image2, 'rb') as file:
        image2_data = file.read()
    img1 = Image.open(io.BytesIO(image1_data))
    img2 = Image.open(io.BytesIO(image2_data))
    print("这里可以输出图片的相关属性，如大小、格式等", img1)
    if img1.size != img2.size:
        return False

    pairs = zip(img1.getdata(), img2.getdata())
    print(img1.getdata())
    if len(img1.getbands()) == 1:
        # for grayscale images
        dif = sum(abs(p1 - p2) for p1, p2 in pairs)
    else:
        # for RGB images
        dif = sum(abs(c1 - c2) for p1, p2 in pairs for c1, c2 in zip(p1, p2))

    ncomponents = img1.size[0] * img1.size[1] * 3
    similarity = (ncomponents - dif) / ncomponents

    # 设置阈值，即两张图片相似度严格达到99%才认为它们完全一样
    return similarity > 0.99


compare_images("crop_pic.png", "crop_pic.png")
