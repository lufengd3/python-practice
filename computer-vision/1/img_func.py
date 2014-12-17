#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Try PIL.Image function
"""

import os

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

IMG_DIR = '/home/keith/github/python-practice/computer-vision/img/'

def get_img_list(path = None, img_format = None):
    """
    get all img file from a directory
    """

    if not path:
        path = IMG_DIR

    if img_format:
        img_arr = [os.path.join(path, f) for f in os.listdir(path) if f.endswith(img_format)]
    else:
        img_arr = [os.path.join(path, f) for f in os.listdir(path)]

    return img_arr

def conver_img_format(dest_format, src_format = None):
    """
    convert img from src_format to dest_format
    @param dest_format, string, '.jpg', '.png' ...
    @param src_format, string, '.jpg', '.png' ...
    """

    print "Converting image format from %s to %s ..." % (src_format if src_format else '*', dest_format)

    for infile in get_img_list(IMG_DIR, src_format):
        outfile = os.path.splitext(infile)[0] + dest_format
        if infile != outfile:
            try:
                Image.open(infile).save(outfile)
                print '%s done!' % outfile
            except IOError, e:
                print 'Convert error: ', e

def create_thumbnail():
    """
    生成缩略图
    """
    hw = (96, 96)

    for f in get_img_list(img_format = '.png'):
        print "Generating %s thumbnail file" % f
        outfile = os.path.splitext(f)[0] + '.thumbnail'
        img = Image.open(f)
        img.thumbnail(hw)
        img.save(outfile, 'PNG')

def crop_img(area = None, file_path = IMG_DIR + 'raphael.png'):
    img = Image.open(file_path)

    if not area:
        w = img.size[0]
        h = img.size[1]
        area = (0, 0, w / 2, h / 2)
    
    region = img.crop(area)
    region = region.transpose(Image.ROTATE_180)
    img.paste(region, area)
    img.show()

def draw_img_num(number = 1, file_path = IMG_DIR + 'raphael.png'):
    """
    在图片右上角添加数字
    """

    img = Image.open(file_path)
    font_size = img.size[1] if img.size[0] > img.size[1] else img.size[0] 
    font_size /= 5
    text = str(number) if number < 1000 else '999+'
    font = ImageFont.truetype('./freesans.ttf', size = font_size)
    left = img.size[0] - font.getsize(text)[0]
    ImageDraw.Draw(img).text((left, 0), text, (255, 0, 0), font)
    img.show()

            
if __name__ == '__main__':
    # conver_img_format('.gif', '.png')
    # create_thumbnail()
    # crop_img()
    draw_img_num(3)
