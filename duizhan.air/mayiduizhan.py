# -*- encoding=utf8 -*-
__author__ = "梁杨华"

from airtest.core.api import *

auto_setup(__file__)
touch(Template(r"tpl1647238706646.png", record_pos=(0.366, 0.218), resolution=(1600, 900)))
sleep(1.0)

# 扫荡
touch(Template(r"tpl1647397738841.png", record_pos=(0.101, 0.187), resolution=(1600, 900)))

sleep(1.0)
if exists(Template(r"tpl1647242504215.png", record_pos=(0.244, 0.123), resolution=(1600, 900))):

    touch(Template(r"tpl1647242504215.png", record_pos=(0.244, 0.123), resolution=(1600, 900)))
sleep(1.0)
if exists(Template(r"tpl1647399454167.png", record_pos=(-0.004, -0.146), resolution=(1600, 900))):
    touch(Template(r"tpl1647399467861.png", record_pos=(0.191, -0.128), resolution=(1600, 900)))
sleep(1.0)


if exists(Template(r"tpl1647242550138.png", record_pos=(0.089, 0.094), resolution=(1600, 900))):
    touch(Template(r"tpl1647242562568.png", record_pos=(0.091, 0.092), resolution=(1600, 900)))
sleep(1.0)

if exists(Template(r"tpl1647243364291.png", record_pos=(0.187, -0.128), resolution=(1600, 900))):
    touch(Template(r"tpl1647243364291.png", record_pos=(0.187, -0.128), resolution=(1600, 900)))

sleep(2.0)
if exists(Template(r"tpl1647242664907.png", record_pos=(0.33, -0.184), resolution=(1600, 900))):
    touch(Template(r"tpl1647242664907.png", record_pos=(0.33, -0.184), resolution=(1600, 900)))

sleep(1.0)



# 搜索对手
touch(Template(r"tpl1647397764081.png", record_pos=(0.332, 0.179), resolution=(1600, 900)))

sleep(1.0)
touch(Template(r"tpl1647397777279.png", record_pos=(0.179, 0.169), resolution=(1600, 900)))

sleep(1.0)

if exists(Template(r"tpl1647238747945.png", record_pos=(0.089, 0.092), resolution=(1600, 900))):
    sleep(1.0)
    touch(Template(r"tpl1647238842641.png", record_pos=(0.089, 0.092), resolution=(1600, 900)))
    
# 重伤情况
if exists(Template(r"tpl1647398356111.png", record_pos=(0.026, 0.212), resolution=(1600, 900))):
    touch(Template(r"tpl1647398367564.png", record_pos=(0.024, 0.212), resolution=(1600, 900)))
# 资源已满
if exists(Template(r"tpl1647399544470.png", record_pos=(-0.001, -0.144), resolution=(1600, 900))):
    touch(Template(r"tpl1647399557761.png", record_pos=(0.088, 0.096), resolution=(1600, 900)))
if exists(Template(r"tpl1647398389074.png", record_pos=(-0.001, -0.145), resolution=(1600, 900))):
    touch(Template(r"tpl1647398401919.png", record_pos=(0.09, 0.094), resolution=(1600, 900)))






sleep(10.0)
touch(Template(r"tpl1647397801607.png", record_pos=(0.426, 0.152), resolution=(1600, 900)))

sleep(10.0)
touch(Template(r"tpl1647238979336.png", record_pos=(-0.456, 0.149), resolution=(1600, 900)))
sleep(4.0)

# 800星奖励
touch(Template(r"tpl1647239141155.png", record_pos=(-0.136, 0.217), resolution=(1600, 900)))
sleep(2.0)
touch(Template(r"tpl1647239169157.png", record_pos=(-0.466, -0.251), resolution=(1600, 900)))
sleep(2.0)

# 官职赛季奖励
touch(Template(r"tpl1647239178173.png", record_pos=(0.402, -0.163), resolution=(1600, 900)))
sleep(1.0)

swipe(Template(r"tpl1647239208644.png", record_pos=(-0.003, -0.022), resolution=(1600, 900)), vector=[0.0499, -0.1617])
sleep(4.0)
touch(Template(r"tpl1647239229170.png", record_pos=(0.328, -0.186), resolution=(1600, 900)))
sleep(1.0)

# 星星阶段奖励
swipe(Template(r"tpl1647239261672.png", record_pos=(0.228, 0.016), resolution=(1600, 900)), vector=[-0.4039, 0.0083])
sleep(1.0)
touch(Template(r"tpl1647240415414.png", record_pos=(0.317, 0.007), resolution=(1600, 900)))
sleep(2.0)
touch(Template(r"tpl1647241385799.png", record_pos=(0.191, -0.125), resolution=(1600, 900)))

sleep(2.0)

if exists(Template(r"tpl1647412816983.png", record_pos=(0.026, -0.102), resolution=(1600, 900))):


    # 联赛
    touch(Template(r"tpl1647240445245.png", record_pos=(-0.434, -0.072), resolution=(1600, 900)))
    wait(Template(r"tpl1647240451090.png", record_pos=(-0.434, -0.074), resolution=(1600, 900)))
    sleep(2.0)

    # 挑战用例
    if exists(Template(r"tpl1647240521668.png", record_pos=(0.334, 0.098), resolution=(1600, 900))):
        touch(Template(r"tpl1647240540661.png", record_pos=(0.338, 0.1), resolution=(1600, 900)))
        sleep(1.0)
    if exists(Template(r"tpl1647240551898.png", record_pos=(-0.274, -0.051), resolution=(1600, 900))):   
        touch(Template(r"tpl1647240551898.png", record_pos=(-0.274, -0.051), resolution=(1600, 900)))
        wait(Template(r"tpl1647240555926.png", record_pos=(-0.273, -0.051), resolution=(1600, 900)))
        sleep(1.0)
    if exists(Template(r"tpl1647240757856.png", record_pos=(-0.27, -0.109), resolution=(1600, 900))):    
        touch(Template(r"tpl1647240757856.png", record_pos=(-0.27, -0.109), resolution=(1600, 900)))
        sleep(1.0)

    if exists(Template(r"tpl1647240774271.png", record_pos=(0.278, -0.068), resolution=(1600, 900))):
        touch(Template(r"tpl1647240774271.png", record_pos=(0.278, -0.068), resolution=(1600, 900)))
    if exists(Template(r"tpl1647397655212.png", record_pos=(0.088, 0.095), resolution=(1600, 900))):
        touch(Template(r"tpl1647397671278.png", record_pos=(0.087, 0.092), resolution=(1600, 900)))   

    # 重伤情况
    if exists(Template(r"tpl1647398356111.png", record_pos=(0.026, 0.212), resolution=(1600, 900))):
        touch(Template(r"tpl1647398367564.png", record_pos=(0.024, 0.212), resolution=(1600, 900)))
    # 资源已满
    if exists(Template(r"tpl1647399544470.png", record_pos=(-0.001, -0.144), resolution=(1600, 900))):
        touch(Template(r"tpl1647399557761.png", record_pos=(0.088, 0.096), resolution=(1600, 900)))
    if exists(Template(r"tpl1647398389074.png", record_pos=(-0.001, -0.145), resolution=(1600, 900))):
        touch(Template(r"tpl1647398401919.png", record_pos=(0.09, 0.094), resolution=(1600, 900)))

    sleep(10.0)
    if exists(Template(r"tpl1647240805759.png", record_pos=(-0.453, 0.148), resolution=(1600, 900))):
        touch(Template(r"tpl1647240805759.png", record_pos=(-0.453, 0.148), resolution=(1600, 900)))
    sleep(2.0)

    if exists(Template(r"tpl1647397947182.png", record_pos=(0.089, 0.096), resolution=(1600, 900))):
        touch(Template(r"tpl1647397970218.png", record_pos=(0.086, 0.095), resolution=(1600, 900)))
    sleep(6.0)
    if exists(Template(r"tpl1647398983612.png", record_pos=(-0.453, 0.239), resolution=(1600, 900))):
        touch(Template(r"tpl1647399004339.png", record_pos=(-0.005, 0.237), resolution=(1600, 900)))
    sleep(2.0)


    if exists(Template(r"tpl1647398131854.png", record_pos=(0.329, -0.177), resolution=(1600, 900))):
        touch(Template(r"tpl1647398143138.png", record_pos=(0.331, -0.177), resolution=(1600, 900)))


    sleep(1.0)
    touch(Template(r"tpl1647240955342.png", record_pos=(-0.359, -0.251), resolution=(1600, 900)))
    sleep(1.0)

    touch(Template(r"tpl1647398156837.png", record_pos=(0.191, -0.128), resolution=(1600, 900)))
    sleep(1.0)

    # 联赛相关页签
    touch(Template(r"tpl1647241129456.png", record_pos=(0.24, 0.228), resolution=(1600, 900)))
    sleep(1.0)

    touch(Template(r"tpl1647398180001.png", record_pos=(0.394, -0.206), resolution=(1600, 900)))

    sleep(1.0)
    touch(Template(r"tpl1647241154628.png", record_pos=(0.307, 0.227), resolution=(1600, 900)))
    sleep(1.0)
    touch(Template(r"tpl1647398194812.png", record_pos=(0.396, -0.205), resolution=(1600, 900)))

    sleep(1.0)
    touch(Template(r"tpl1647241172222.png", record_pos=(0.369, 0.224), resolution=(1600, 900)))
    sleep(1.0)
    touch(Template(r"tpl1647398211211.png", record_pos=(0.333, -0.183), resolution=(1600, 900)))

    sleep(1.0)
    touch(Template(r"tpl1647241189667.png", record_pos=(0.436, 0.229), resolution=(1600, 900)))
    sleep(1.0)
    touch(Template(r"tpl1647241221592.png", record_pos=(0.38, 0.223), resolution=(1600, 900)))
    sleep(1.0)
    touch(Template(r"tpl1647241236570.png", record_pos=(-0.269, -0.052), resolution=(1600, 900)))
    wait(Template(r"tpl1647241249446.png", record_pos=(-0.271, -0.054), resolution=(1600, 900)))
    sleep(1.0)
    touch(Template(r"tpl1647398237350.png", record_pos=(0.333, -0.182), resolution=(1600, 900)))

    sleep(1.0)
    touch(Template(r"tpl1647398245861.png", record_pos=(0.394, -0.205), resolution=(1600, 900)))

    sleep(1.0)
touch(Template(r"tpl1647398262689.png", record_pos=(-0.464, -0.253), resolution=(1600, 900)))










    
