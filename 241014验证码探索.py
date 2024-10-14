from PIL import Image, ImageDraw, ImageFont, ImageFilter

import random

# 随机字母:
def rndChar():
    choice = random.randint(1, 3)
    if choice == 1:
        return chr(random.randint(65, 90))  # 大写字母A-Z
    elif choice == 2:
        return chr(random.randint(97, 122))  # 小写字母a-z
    else:
        return chr(random.randint(48, 57))  # 数字0-9

# 随机字体大小
def rndSize():
    return random.randint(28, 45)

# 生成随机旋转角度
def rndAngle():
    return random.randint(-90, 90)

# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# 批量生成验证码图片的数量
num_images = 10

for n in range(num_images):
    # 240 x 60:
    width = 60 * 4
    height = 60
    image = Image.new('RGB', (width, height), (255, 255, 255))

    # 创建Draw对象:
    draw = ImageDraw.Draw(image)
    # 填充每个像素:
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=rndColor())
    # 输出文字并旋转每个字母:
    for i in range(4):
        # 随机生成字体大小
        font = ImageFont.truetype('Arial.ttf', rndSize())
        
        # 使用 getbbox 获取文字的边界框
        char = rndChar()
        bbox = font.getbbox(char)
        char_width, char_height = bbox[2], bbox[3]  # 边界框的宽度和高度

        # 生成一个单独的文字图像
        char_image = Image.new('RGBA', (char_width, char_height), (255, 255, 255, 0))
        char_draw = ImageDraw.Draw(char_image)
        char_draw.text((0, 0), char, font=font, fill=rndColor2())

        # 随机旋转字符图像
        rotated_char_image = char_image.rotate(rndAngle(), expand=True)

        # 将旋转后的字符图像粘贴到主图像上
        image.paste(rotated_char_image, (60 * i + 10, 10), rotated_char_image)

    # 模糊:
    image = image.filter(ImageFilter.BLUR)
    image.save('code.jpg', 'jpeg')

    # 保存图片，使用不同的文件名
    image.save(f'code_{n}.jpg', 'jpeg')
