import math
import random
import matplotlib.pyplot as plt
import ballinbox.validate as vv

__all__ = ['ball_in_box']

def area_sum(circles):
    area = 0.0
    for circle in circles:
        area += circle[2]**2 * math.pi

    return area

def ball_in_box(m=5, blockers=[(0.5, 0.5), (0.5, -0.5), (0.5, 0.3)]):
    """
    m is the number circles.
    n is the list of coordinates of tiny blocks.
    
    This returns a list of tuple, composed of x,y of the circle and r of the circle.
    """

    # The following is an example implementation.
    print('请输入气球的数量：')
    m=int(input())
    print("是否自定应点（1：是，0：否）：")
    choose=int(input())
    if choose:
        blockers=[]
        conti=1
        while conti:
            print('输入点的坐标(形式：x,y)：')
            n=tuple(input())
            blockers.append((int(n[0]),int(n[2])))
            print("是否继续输入(1:是，0：否)：")
            conti=int(input())
    print(blockers)
    circles=[]
    circle_index=0
    raw_circle=[(0,0,0)]
    while circle_index<m:
        x=-0.98
        y=-0.98
        r=0.015
        circles.append((0,0,0))
        while x<1:
            while y<1:
                while r<1:
                     circles[circle_index]=(x, y, r)
                     if  not vv.validate(circles,blockers):
                         if raw_circle[0][2]<r-0.005:
                             raw_circle[0]=(x,y,r-0.005)
                         break
                     r=r+0.005
                y=y+0.01
                r=0.015
            x=x+0.01
            y=-0.98
        circles[circle_index]=raw_circle[0]
        print('找到了第',circle_index+1,'个圆',raw_circle)
        raw_circle=[(0,0,0)]
        circle_index=circle_index+1
    area = area_sum(circles)
    print("Total area: {}".format(area))
    fig=plt.figure()
    ax = fig.add_subplot(111)
    plt.xlim((-1,1))
    plt.ylim((-1,1))
    for i in blockers:
        plt.scatter(i[0],i[1],s=20,edgecolors='',marker='o' )
    for i in circles:
        cir1=plt.Circle((i[0],i[1]),i[2],color='b',fill=False)
        ax.add_patch(cir1)
    plt.show()
    return circles