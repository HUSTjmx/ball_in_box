import math
import random
import numpy as np

#import matplotlib.pyplot as plt
E=1e-12
__all__ = ['ball_in_box']

step1=0.005
step2=0.0001

def area_sum(circles):
    area = 0.0
    for circle in circles:
        area += circle[2]**2 * math.pi

    return area

def getmin(aim,circles,blocks):
    dis=2

    for circle in circles:
        dis2=math.sqrt((aim[0]-circle[0])**2+(aim[1]-circle[1])**2)-circle[2]
        if dis>dis2:
            dis=dis2
    for block in blocks:
        dis2 = math.sqrt((aim[0] - block[0]) ** 2 + (aim[1] - block[1]) ** 2)
        if dis>dis2:
            dis=dis2
    for x in [-1,1]:
        dis2 = math.sqrt((aim[0] - x) ** 2 )
        if dis>dis2 :
            dis = dis2
    for y in [-1,1]:
        dis2 = math.sqrt((aim[1] -y) ** 2 )
        if dis>dis2 :
            dis = dis2
    return dis

def getarround(raw_circle,circle_index,circles,blocks):
    x_old=raw_circle[0]
    y_old=raw_circle[1]
    x=raw_circle[0]-step1
    y=raw_circle[1]-step1
    middle_circle=[(0,0,0)]
    while x<x_old+step1:
        while y<y_old+step1:
            r = getmin((x, y), circles, blocks)
            if (middle_circle[0][2] < r):
                middle_circle[0] = (x, y, r)
            y=y+step2
        x=x+step2
        y=raw_circle[1]-step1
    if middle_circle[0][2]<raw_circle[2]:
        middle_circle[0]=raw_circle
    return middle_circle[0]


def ball_in_box(m=5, blockers=[(0.5, 0.5), (0.5, -0.5), (0.5, 0.3)]):
    """
    m is the number circles.
    n is the list of coordinates of tiny blocks.
    
    This returns a list of tuple, composed of x,y of the circle and r of the circle.
    """
 # The following is an example implementation.
    n=int(input('请输入气球的数量（输入非正数则取默认气球数5）：'))
    if m>0:
        m=n
    choose=int(input("是否自定应点（1：是，0：否）："))
    if choose:
        blockers=[]
        conti=1
        while conti:
            n=input('请输入点的坐标(形式：x,y)：')
            xlist = n.split(",")
            x=float(xlist[0])
            y=float(xlist[1])
            blockers.append((x,y))
            conti=int(input("是否继续输入(1:是，0：否)："))
    print("障碍点：",blockers)
    circles=[]
    circle_index=0
    raw_circle=[(0,0,0)]
    while circle_index<m:
        x=-1
        y=-1
        while x<1:
            while y<1:
                r=getmin((x,y),circles,blockers)
                if(raw_circle[0][2]<r):
                    raw_circle[0]=(x,y,r)
                y=y+step1
            x=x+step1
            y=-0.995
        raw_circle[0] = getarround(raw_circle[0], circle_index, circles, blockers)
        circles.append(raw_circle[0])
        print('终于找到了第',circle_index+1,'个圆',raw_circle)
        raw_circle=[(0,0,0)]
        circle_index=circle_index+1
    area = area_sum(circles)
    print("Total area: {}".format(area))

    return circles
