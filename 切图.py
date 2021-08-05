# @Time:2021/7/16 10:05 上午
# @Author:liuyue
# @Email:liuyue@soyoung.com
# @coding:utf-8

from PIL import Image


def produceImage(file_in, width, height, file_out):
    image = Image.open(file_in, 'r')
    resized_image = image.resize((width, height), Image.ANTIALIAS)
    resized_image.save(file_out)


if __name__ == '__main__':
    file_in = '/Users/liuyue/Desktop/需求/开屏第三方配置/pic/模特图.jpg'  # 要切的图片
    print(file_in)
    width = 360  # 要切的宽度
    height = 450  # 要切的高度
    file_out = '/Users/liuyue/Desktop/需求/banner改版/pic/360*450.jpg'  # 切完后图片
    produceImage(file_in, width, height, file_out)
