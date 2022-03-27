# -*- encoding=utf8 -*-
__author__ = "AUSU"

import sys
from airtest.core.api import *
from airtest.cli.parser import cli_setup
from airtest.core.settings import Settings as ST
import calendar;
import time;
import traceback

auto_setup(__file__)
init_device("Android", ime_method="ADBIME")

def shipei():
    # 获取设备的宽度和高度
    w, h = device().get_current_resolution()
    return w, h

# 高级进化
def drawCard1(i):
    if i == 1:
        if exists(Template(r"tpl1648394013976.png", record_pos=(0.088, -0.011), resolution=(2280, 1080))):
            recruitmentOrderBuy()
            touch(Template(r"tpl1648396772199.png", record_pos=(-0.062, 0.176), resolution=(2280, 1080)))
        sleep(5)
        if exists(Template(r"tpl1648394193774.png", record_pos=(0.421, -0.204), resolution=(2280, 1080))):
            sleep(2)
            touch(Template(r"tpl1648394310371.png", record_pos=(0.421, -0.206), resolution=(2280, 1080)))
            if exists(Template(r"tpl1648397154532.png", record_pos=(-0.002, -0.105), resolution=(2280, 1080))):
                touch([0.505*w, 0.858*h])
        # 继续进化
        wait(Template(r"tpl1648392882435.png", record_pos=(0.12, 0.187), resolution=(2280, 1080)), timeout=30)
        touch(Template(r"tpl1648392924209.png", record_pos=(0.119, 0.189), resolution=(2280, 1080)))
        if exists(Template(r"tpl1648394013976.png", record_pos=(0.088, -0.011), resolution=(2280, 1080))):
            recruitmentOrderBuy()
            touch(Template(r"tpl1648392924209.png", record_pos=(0.119, 0.189), resolution=(2280, 1080)))
        if exists(Template(r"tpl1648394193774.png", record_pos=(0.421, -0.204), resolution=(2280, 1080))):
            sleep(2)
            touch(Template(r"tpl1648394310371.png", record_pos=(0.421, -0.206), resolution=(2280, 1080)))
            if exists(Template(r"tpl1648397154532.png", record_pos=(-0.002, -0.105), resolution=(2280, 1080))):
                touch([0.505*w, 0.858*h])
        wait(Template(r"tpl1648394326715.png", record_pos=(-0.122, 0.186), resolution=(2280, 1080)))
        touch(Template(r"tpl1648394380065.png", record_pos=(-0.125, 0.185), resolution=(2280, 1080)))
    elif i == 10:
        if exists(Template(r"tpl1648394013976.png", record_pos=(0.088, -0.011), resolution=(2280, 1080))):
            recruitmentOrderBuy()
            touch(Template(r"tpl1648396785377.png", record_pos=(0.105, 0.175), resolution=(2280, 1080)))
        sleep(5)
        for i in range(5):
            if exists(Template(r"tpl1648394193774.png", record_pos=(0.421, -0.204), resolution=(2280, 1080))):
                sleep(2)
                touch(Template(r"tpl1648394310371.png", record_pos=(0.421, -0.206), resolution=(2280, 1080)))
        if exists(Template(r"tpl1648397154532.png", record_pos=(-0.002, -0.105), resolution=(2280, 1080))):
                touch([0.505*w, 0.858*h])
        # 继续进化
        wait(Template(r"tpl1648392882435.png", record_pos=(0.12, 0.187), resolution=(2280, 1080)), timeout=30)
        touch(Template(r"tpl1648392924209.png", record_pos=(0.119, 0.189), resolution=(2280, 1080)))
        if exists(Template(r"tpl1648394013976.png", record_pos=(0.088, -0.011), resolution=(2280, 1080))):
            recruitmentOrderBuy()
            touch(Template(r"tpl1648392924209.png", record_pos=(0.119, 0.189), resolution=(2280, 1080)))
        for i in range(10):
            if exists(Template(r"tpl1648394193774.png", record_pos=(0.421, -0.204), resolution=(2280, 1080))):
                sleep(2)
                touch(Template(r"tpl1648394310371.png", record_pos=(0.421, -0.206), resolution=(2280, 1080)))
        if exists(Template(r"tpl1648397154532.png", record_pos=(-0.002, -0.105), resolution=(2280, 1080))):
                touch([0.505*w, 0.858*h])
        wait(Template(r"tpl1648394326715.png", record_pos=(-0.122, 0.186), resolution=(2280, 1080)))
        touch(Template(r"tpl1648394380065.png", record_pos=(-0.125, 0.185), resolution=(2280, 1080)))

        



# 购买高级进化之果
def recruitmentOrderBuy():
        if exists(Template(r"tpl1648395773716.png", threshold=0.8500000000000001, record_pos=(0.021, 0.067), resolution=(2280, 1080))):
            touch(Template(r"tpl1648393742638.png", record_pos=(-0.006, 0.068), resolution=(2280, 1080)))
            wait(Template(r"tpl1648393808015.png", record_pos=(0.0, -0.035), resolution=(2280, 1080)), timeout=30)
            touch(Template(r"tpl1648393832591.png", record_pos=(0.075, 0.08), resolution=(2280, 1080)))
        if exists(Template(r"tpl1648393850962.png", record_pos=(-0.005, 0.069), resolution=(2280, 1080))):
            touch(Template(r"tpl1648393864299.png", record_pos=(-0.004, 0.071), resolution=(2280, 1080)))
            wait(Template(r"tpl1648393872879.png", record_pos=(0.004, -0.039), resolution=(2280, 1080)), timeout=30)
            touch(Template(r"tpl1648393832591.png", record_pos=(0.075, 0.08), resolution=(2280, 1080)))
        if exists(Template(r"tpl1648393907565.png", record_pos=(0.181, 0.07), resolution=(2280, 1080))):
            touch(Template(r"tpl1648393931730.png", record_pos=(0.183, 0.07), resolution=(2280, 1080)))
            wait(Template(r"tpl1648393945807.png", record_pos=(0.002, -0.034), resolution=(2280, 1080)), timeout=30)
            touch(Template(r"tpl1648393832591.png", record_pos=(0.075, 0.08), resolution=(2280, 1080)))
        sleep(2)
        touch(Template(r"tpl1648394087364.png", record_pos=(0.277, -0.157), resolution=(2280, 1080)))

            

# 普通进化            
def drawCard2(i):
    if i == 1:
        sleep(5)
        if exists(Template(r"tpl1648394193774.png", record_pos=(0.421, -0.204), resolution=(2280, 1080))):
                sleep(2)
                touch(Template(r"tpl1648394310371.png", record_pos=(0.421, -0.206), resolution=(2280, 1080)))
        if exists(Template(r"tpl1648397656594.png", record_pos=(0.119, 0.187), resolution=(2280, 1080))):
            touch(Template(r"tpl1648397742757.png", record_pos=(-0.123, 0.187), resolution=(2280, 1080)))
        else:
            pass
    if i == 10:
        sleep(5)
        if exists(Template(r"tpl1648394193774.png", record_pos=(0.421, -0.204), resolution=(2280, 1080))):
                sleep(2)
                touch(Template(r"tpl1648394310371.png", record_pos=(0.421, -0.206), resolution=(2280, 1080)))
        if exists(Template(r"tpl1648397656594.png", record_pos=(0.119, 0.187), resolution=(2280, 1080))):
            touch(Template(r"tpl1648397742757.png", record_pos=(-0.123, 0.187), resolution=(2280, 1080)))


# 特级进化            
def drawCard3(i):
    if i == 1:
        sleep(5)
        if exists(Template(r"tpl1648394193774.png", record_pos=(0.421, -0.204), resolution=(2280, 1080))):
                sleep(2)
                touch(Template(r"tpl1648394310371.png", record_pos=(0.421, -0.206), resolution=(2280, 1080)))
        if exists(Template(r"tpl1648397656594.png", record_pos=(0.119, 0.187), resolution=(2280, 1080))):
            touch(Template(r"tpl1648397742757.png", record_pos=(-0.123, 0.187), resolution=(2280, 1080)))
        else:
            pass
    if i == 10:
        sleep(5)
        if exists(Template(r"tpl1648394193774.png", record_pos=(0.421, -0.204), resolution=(2280, 1080))):
                sleep(2)
                touch(Template(r"tpl1648394310371.png", record_pos=(0.421, -0.206), resolution=(2280, 1080)))
        if exists(Template(r"tpl1648397656594.png", record_pos=(0.119, 0.187), resolution=(2280, 1080))):
            touch(Template(r"tpl1648397742757.png", record_pos=(-0.123, 0.187), resolution=(2280, 1080)))




    


# 英雄抽卡脚本
w, h = shipei()
print("----------执行英雄抽卡脚本----------")
touch(Template(r"tpl1648392493570.png", record_pos=(-0.016, 0.199), resolution=(2280, 1080)))
print("----------高级进化----------")
if exists(Template(r"tpl1648392571320.png", record_pos=(-0.059, 0.177), resolution=(2280, 1080))) or exists(Template(r"tpl1648394434331.png", record_pos=(-0.061, 0.177), resolution=(2280, 1080))):
    touch([0.433*w, 0.869*h])
    drawCard1(1)

if exists(Template(r"tpl1648394479912.png", record_pos=(0.105, 0.176), resolution=(2280, 1080))):
    touch(Template(r"tpl1648394492434.png", record_pos=(0.103, 0.173), resolution=(2280, 1080)))
    drawCard1(10)

print("----------普通进化----------")
touch(Template(r"tpl1648398330292.png", record_pos=(-0.394, -0.046), resolution=(2280, 1080)))
if exists(Template(r"tpl1648397348804.png", record_pos=(-0.062, 0.176), resolution=(2280, 1080))) or exists(Template(r"tpl1648398891214.png", record_pos=(-0.061, 0.175), resolution=(2280, 1080))):
    touch([0.443*w, 0.867*h])
    drawCard2(1)

if exists(Template(r"tpl1648397376823.png", record_pos=(0.107, 0.172), resolution=(2280, 1080))) or exists(Template(r"tpl1648398832077.png", record_pos=(0.106, 0.171), resolution=(2280, 1080))):
    touch([0.593*w, 0.858*h])
    drawCard2(10)

print("----------特级进化----------")
touch(Template(r"tpl1648399062042.png", record_pos=(-0.394, 0.035), resolution=(2280, 1080)))
if exists(Template(r"tpl1648399275513.png", record_pos=(-0.059, 0.176), resolution=(2280, 1080))) or exists(Template(r"tpl1648399082630.png", record_pos=(-0.06, 0.174), resolution=(2280, 1080))):
    touch([0.443*w, 0.867*h])
    drawCard2(1)

if exists(Template(r"tpl1648399096064.png", record_pos=(0.107, 0.176), resolution=(2280, 1080))) or exists(Template(r"tpl1648399288204.png", record_pos=(0.105, 0.174), resolution=(2280, 1080))):
    touch([0.593*w, 0.858*h])
    drawCard2(10)