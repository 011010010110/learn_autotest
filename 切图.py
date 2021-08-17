# @Time:2021/8/17 5:22 下午
# @Author:liuyue
# @Email:liuyue@soyoung.com
# @coding:utf-8
from PIL import Image


def produceImage(file_in, width, height, file_out):
    image = Image.open(file_in, 'r')
    resized_image = image.resize((width, height), Image.ANTIALIAS)
    resized_image.save(file_out)


if __name__ == '__main__':
    file_in = '/Users/liuyue/Desktop/需求/开屏第三方配置/pic/模特图.jpg'#要切的图片
    print(file_in)
    width = 1124#要切的宽度
    height = 2000#要切的高度
    file_out = '/Users/liuyue/Desktop/需求/开屏第三方配置/pic/1124*2000.jpg'#切完后图片
    produceImage(file_in, width, height, file_out)