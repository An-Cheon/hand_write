# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-06-03 오전 8:29
# @Author  : An Cheon
# @File    : hand_write.py

from PIL import Image, ImageFont
from handright import Template, handwrite
import os

def read_txt(txt_path):
    if not os.path.exists(txt_path):
        print(txt_path + " 文件不存在")
        return None
    else:
        f = open(txt_path, "r",encoding="utf-8")
        lines = f.read()
        return lines

def blend_two_images(background,words_photo,aim_path):
    img1 = Image.open(words_photo)
    img1 = img1.convert('RGBA')

    img2 = Image.open(background)
    img2 = img2.convert('RGBA')

    img = Image.blend(img1, img2,0.4)
    img.save(aim_path)

def reduce_resolution(path,rate):
    infile = path  # 输入的图片
    outfile = path  # 要保存的地址
    im = Image.open(infile)
    (x, y) = im.size  # read image size
    pic_resize = rate  # 想要缩放/扩大的倍数
    x_s = int(x / pic_resize)  #
    y_s = int(y / pic_resize)  #
    out = im.resize((x_s, y_s), Image.ANTIALIAS)  # resize image with high-quality
    out.save(outfile)

def clear_cache():
    ls = os.listdir("cache")
    if len(ls) == 0:
        return None
    else:
        for i in ls:
            c_path = os.path.join("cache", i)
            os.remove(c_path)

def function(txt_path,font_path,prefix):
    path_0 = os.path.split(os.path.realpath(__file__))[0]
    path_0 = path.replace("\\", "/") + "/"
    strs = read_txt(txt_path).replace("。"," ").\
        replace("，"," ").replace("；"," ").replace("：",":").\
        replace(";"," ").replace("• ","").replace("➢"," ").replace("◼","")
    template = Template(
        background=Image.new(mode="1", size=(9060, 12793), color=1),
        #font_size=280,
        font=ImageFont.truetype(font_path,size=280),
        line_spacing=385,
        fill=0,  # 字体“颜色”
        left_margin=0,
        top_margin=850,
        right_margin=0,
        bottom_margin=500,
        word_spacing=15,
        line_spacing_sigma=0,  # 行间距随机扰动
        end_chars="，。",  # 防止特定字符因排版算法的自动换行而出现在行首
        font_size_sigma=10,  # 字体大小随机扰动
        word_spacing_sigma=30,  # 字间距随机扰动
    )
    images = handwrite(strs, template)
    for i, im in enumerate(images):
        assert isinstance(im, Image.Image)
        # im.show()
        im.save("cache/{}.png".format(i))
        temp = prefix + "({}).png".format(i + 1)
        blend_two_images(path_0 + "cache/{}.png".format(i), path_0 + "backgrounds/background.png", path_0 + "png_outcome/" + temp)
        reduce_resolution(path_0 + "png_outcome/" + temp,4.152153987167736)
    clear_cache()

path = os.path.split(os.path.realpath(__file__))[0]
path = path.replace("\\","/") + "/"
print("meow 手写字体模拟1.0")
print("请勿更改各文件夹位置")
print()
while True:
    break_flag_0 = 0
    break_flag_1 = 0
    break_flag_2 = 0
    while True:
        if break_flag_0 == 1:
            break
        else:
            print("请输入字体文件名 e.g. 老槐树.ttf")
            given_words_0 = input("")
            #print(path + "fonts/" + given_words_0)
            if not os.path.exists(path + "fonts/" + given_words_0):
                print("该文件不存在，请输入存在的文件")
            else:
                break_flag_0 = 1
    while True:
        if break_flag_1 == 1:
            break
        else:
            print("请输入需要手写的txt文件名 e.g. 0.txt")
            given_words_1 = input("")
            if not os.path.exists(path + "txts/" + given_words_1):
                print("该文件不存在，请输入存在的文件")
            else:
                break_flag_1 = 1
    while True:
        if break_flag_2 == 1:
            break
        else:
            print("请输入生成的手写文件的文件名 e.g. homework (无需文件名后缀!!!)")
            given_words_2 = input("")
            if len(given_words_2) == 0:
                print("输入为空")
            else:
                break_flag_2 = 1
    print("处理中...")
    print("请勿在意warning")
    function(path + "txts/" + given_words_1, path + "fonts/" + given_words_0, given_words_2)
    print("处理完毕，结果位于" + path + "png_outcome " + "文件夹")
    temp = input("press any key to continue...")

