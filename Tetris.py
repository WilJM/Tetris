from enum import Enum

class Num(Enum):
    first =0; second =1; third=2; forth =3

enumerate
class Shape:
    def __init__(self, point, now) -> None:
        self.point = point
        self.now = now

    def set_shape(self, num, x, y) -> None:
        self.point[num][0] = x
        self.point[num][1] = y

    def get_shape(self, num):
        return {self.point[num][0], self.point[num][1]}

'''
(x,y)

(0,0) (1,0) (2,0) (3,0)
(0,1) (1,1) (2,1) (3,1)
(0,2) (1,2) (2,2) (3,2)
(0,3) (1,3) (2,3) (3,3)

<t_shape>
.0.. 0... 000. .0.. 1. (1,0) (0,1) (1,1) (2,1)
000. 00.. .0.. 00.. 2. (0,0) (0,1) (1,1) (1,2)
.... 0... .... .0.. 3. (0,0) (1,0) (2,0) (1,1)
.... .... .... .... 4. (1,0) (0,1) (1,1) (1,2)

<l_shape>
0... 0000 0... 0000 1. (0,0) (0,1) (0,2) (0,3)
0... .... 0... .... 2. (0,0) (1,0) (2,0) (3,0)
0... .... 0... .... 3. (0,0) (0,1) (0,2) (0,3)
0... .... 0... .... 4. (0,0) (1,0) (2,0) (3,0)

<o_shape>
00.. 00.. 00.. 00.. 1. (0,0) (1,0) (0,1) (1,1)
00.. 00.. 00.. 00.. 2. (0,0) (1,0) (0,1) (1,1)
.... .... .... .... 3. (0,0) (1,0) (0,1) (1,1)
.... .... .... .... 4. (0,0) (1,0) (0,1) (1,1)

<z_shape>
00.. .0.. 00.. .0.. 1. (0,0) (1,0) (1,1) (2,1)
.00. 00.. .00. 00.. 2. (1,0) (0,1) (1,1) (0,2)
.... 0... .... 0... 3. (0,0) (1,0) (1,1) (2,1)
.... .... .... .... 4. (1,0) (0,1) (1,1) (0,2)

<i_shape>
0... ..0. 00.. 000. 1. (0,0) (0,1) (0,2) (1,2)
0... 000. .0.. 0... 2. (0,1) (1,1) (2,1) (2,0) 
00.. .... .0.. .... 3. (0,0) (1,0) (0,1) (0,2) 
.... .... .... .... 4. (0,0) (1,0) (2,0) (0,1) 

<h_shape>
.00. 0... .00. 0... 1. (0,1) (1,1) (1,0) (2,0)
00.. 00.. 00.. 00.. 2. (0,0) (0,1) (1,1) (1,2)
.... .0.. .... .0.. 3. (0,1) (1,1) (1,0) (2,0)
.... .... .... .... 4. (0,0) (0,1) (1,1) (1,2)

'''
def init_shape():
    t_shape = [Shape(), Shape(), Shape(), Shape()]
    l_shape = [Shape(), Shape(), Shape(), Shape()]
    o_shape = [Shape(), Shape(), Shape(), Shape()]
    z_shape = [Shape(), Shape(), Shape(), Shape()]
    i_shape = [Shape(), Shape(), Shape(), Shape()]
    h_shape = [Shape(), Shape(), Shape(), Shape()]

    t_shape[Num.first].set_shape(Num.first, 1, 0); t_shape[Num.first].set_shape(Num.second, 0,1); t_shape[Num.first].set_shape(Num.thrid, 1, 1); t_shape[Num.first].set_shape(Num.forth, 2, 1)
    t_shape[Num.second].set_shape(Num.first, 0, 0); t_shape[Num.second].set_shape(Num.second, 0, 1); t_shape[Num.second].set_shape(Num.thrid, 1, 1); t_shape[Num.second].set_shape(Num.forth, 1, 2) 
    t_shape[Num.third].set_shape(Num.first, 0, 0); t_shape[Num.third].set_shape(Num.second, 1, 0); t_shape[Num.third].set_shape(Num.thrid, 2, 0); t_shape[Num.third].set_shape(Num.forth, 1, 1) 
    t_shape[Num.forth].set_shape(Num.first, 1, 0); t_shape[Num.forth].set_shape(Num.second, 0, 1); t_shape[Num.forth].set_shape(Num.thrid, 1, 1); t_shape[Num.forth].set_shape(Num.forth, 1, 2)  

    l_shape[Num.first].set_shape(Num.first, 0, 0); l_shape[Num.first].set_shape(Num.second, 0, 1); l_shape[Num.first].set_shape(Num.thrid, 0, 2); l_shape[Num.first].set_shape(Num.forth, 0, 3)
    l_shape[Num.second].set_shape(Num.first, 0, 0); l_shape[Num.second].set_shape(Num.second, 1, 0); l_shape[Num.second].set_shape(Num.thrid, 2, 0); l_shape[Num.second].set_shape(Num.forth, 3, 0)
    l_shape[Num.third].set_shape(Num.first, 0, 0); l_shape[Num.third].set_shape(Num.second, 0, 1); l_shape[Num.third].set_shape(Num.thrid, 0, 2); l_shape[Num.third].set_shape(Num.forth, 0, 3)
    l_shape[Num.forth].set_shape(Num.first, 0, 0); l_shape[Num.forth].set_shape(Num.second, 1, 0); l_shape[Num.forth].set_shape(Num.thrid, 2, 0); l_shape[Num.forth].set_shape(Num.forth, 3, 0)

    o_shape[Num.first].set_shape(Num.first, 0, 0); o_shape[Num.first].set_shape(Num.second, 1, 0); o_shape[Num.first].set_shape(Num.thrid, 0, 1); o_shape[Num.first].set_shape(Num.forth, 1, 1)
    o_shape[Num.second].set_shape(Num.first, 0, 0); o_shape[Num.second].set_shape(Num.second,1, 0); o_shape[Num.second].set_shape(Num.thrid, 0, 1); o_shape[Num.second].set_shape(Num.forth, 1, 1)
    o_shape[Num.third].set_shape(Num.first, 0, 0); o_shape[Num.third].set_shape(Num.second, 1, 0); o_shape[Num.third].set_shape(Num.thrid, 0, 1); o_shape[Num.third].set_shape(Num.forth, 1, 1)
    o_shape[Num.forth].set_shape(Num.first, 0, 0); o_shape[Num.forth].set_shape(Num.second, 1, 0); o_shape[Num.forth].set_shape(Num.thrid, 0, 1); o_shape[Num.forth].set_shape(Num.forth, 1, 1)

    z_shape[Num.first].set_shape(Num.first, 0, 0); z_shape[Num.first].set_shape(Num.second, 1, 0); z_shape[Num.first].set_shape(Num.thrid, 1, 1); z_shape[Num.first].set_shape(Num.forth, 2, 1)
    z_shape[Num.second].set_shape(Num.first, 1, 0); z_shape[Num.second].set_shape(Num.second, 0, 1); z_shape[Num.second].set_shape(Num.thrid, 1, 1); z_shape[Num.second].set_shape(Num.forth, 0, 2)
    z_shape[Num.third].set_shape(Num.first, 0, 0); z_shape[Num.third].set_shape(Num.second, 1, 0); z_shape[Num.third].set_shape(Num.thrid, 1, 1); z_shape[Num.third].set_shape(Num.forth, 2, 1)
    z_shape[Num.forth].set_shape(Num.first, 1, 0); z_shape[Num.forth].set_shape(Num.second, 0, 1); z_shape[Num.forth].set_shape(Num.thrid, 1, 1); z_shape[Num.forth].set_shape(Num.forth, 0, 2)

    i_shape[Num.first].set_shape(Num.first, 0, 0); i_shape[Num.first].set_shape(Num.second, 0, 1); i_shape[Num.first].set_shape(Num.thrid, 0, 2); i_shape[Num.first].set_shape(Num.forth, 1, 2)
    i_shape[Num.second].set_shape(Num.first, 0, 1); i_shape[Num.second].set_shape(Num.second, 1, 1); i_shape[Num.second].set_shape(Num.thrid, 2, 1); i_shape[Num.second].set_shape(Num.forth, 2, 0)
    i_shape[Num.third].set_shape(Num.first, 0, 0); i_shape[Num.third].set_shape(Num.second, 1, 0); i_shape[Num.third].set_shape(Num.thrid, 0, 1); i_shape[Num.third].set_shape(Num.forth, 0, 2)
    i_shape[Num.forth].set_shape(Num.first, 0, 0); i_shape[Num.forth].set_shape(Num.second, 1, 0); i_shape[Num.forth].set_shape(Num.thrid, 2, 0); i_shape[Num.forth].set_shape(Num.forth, 0, 1)

    h_shape[Num.first].set_shape(Num.first, 0, 1); h_shape[Num.first].set_shape(Num.second, 1, 1); h_shape[Num.first].set_shape(Num.thrid, 1, 0); h_shape[Num.first].set_shape(Num.forth, 2, 0)
    h_shape[Num.second].set_shape(Num.first, 0, 0); h_shape[Num.second].set_shape(Num.second, 0, 1); h_shape[Num.second].set_shape(Num.thrid, 1, 1); h_shape[Num.second].set_shape(Num.forth, 1, 2)
    h_shape[Num.third].set_shape(Num.first, 0, 1); h_shape[Num.third].set_shape(Num.second, 1, 1); h_shape[Num.third].set_shape(Num.thrid, 1, 0); h_shape[Num.third].set_shape(Num.forth, 2, 0)
    h_shape[Num.forth].set_shape(Num.first, 0, 0); h_shape[Num.forth].set_shape(Num.second, 0, 1); h_shape[Num.forth].set_shape(Num.thrid, 1, 1); h_shape[Num.forth].set_shape(Num.forth, 1, 2)

def left_click(num):
    return num-1
'''
왼쪽 방향키 클릭시 shape 왼쪽 한칸 이동
'''

def right_click(num):
    return num+1
'''
오른쪽 방향키 클릭시 shape 오른쪽 한칸 이동
'''

def down_click(num):
    return num+1
'''
아랫 방향키 클릭시 shape 아랫쪽 한칸 이동
'''

def space_click(num):
    return (num+1)%4
'''
스페이스 바 버튼 클릭시 시계방향으로 shape 90도 회전
'''


