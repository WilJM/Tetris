from enum import Enum

class Num(Enum):
    first =0; second =1; third=2; forth =3

enumerate
class Shape:
    def __init__(self) -> None:
        self.point = [[0,0], [0,0], [0,0], [0,0]]
        self.now = 0

    def set_shape(self, num, x, y) -> None:
        self.point[num][0] = x*10
        self.point[num][1] = y*10

    def get_shape_x(self, num):
        return self.point[num][0]

    def get_shape_y(self, num):
        return self.point[num][1]

t_shape = [Shape(), Shape(), Shape(), Shape()]
l_shape = [Shape(), Shape(), Shape(), Shape()]
o_shape = [Shape(), Shape(), Shape(), Shape()]
z_shape = [Shape(), Shape(), Shape(), Shape()]
i_shape = [Shape(), Shape(), Shape(), Shape()]
h_shape = [Shape(), Shape(), Shape(), Shape()]
def init_shape():
    #t_shape = [Shape(), Shape(), Shape(), Shape()]

    
    t_shape[Num.first.value].set_shape(Num.first.value, 1, 0); t_shape[Num.first.value].set_shape(Num.second.value, 0,1); t_shape[Num.first.value].set_shape(Num.third.value, 1, 1); t_shape[Num.first.value].set_shape(Num.forth.value, 2, 1)
    t_shape[Num.second.value].set_shape(Num.first.value, 0, 0); t_shape[Num.second.value].set_shape(Num.second.value, 0, 1); t_shape[Num.second.value].set_shape(Num.third.value, 1, 1); t_shape[Num.second.value].set_shape(Num.forth.value, 0, 2) 
    t_shape[Num.third.value].set_shape(Num.first.value, 0, 0); t_shape[Num.third.value].set_shape(Num.second.value, 1, 0); t_shape[Num.third.value].set_shape(Num.third.value, 2, 0); t_shape[Num.third.value].set_shape(Num.forth.value, 1, 1) 
    t_shape[Num.forth.value].set_shape(Num.first.value, 1, 0); t_shape[Num.forth.value].set_shape(Num.second.value, 0, 1); t_shape[Num.forth.value].set_shape(Num.third.value, 1, 1); t_shape[Num.forth.value].set_shape(Num.forth.value, 1, 2)  

    l_shape[Num.first.value].set_shape(Num.first.value, 0, 0); l_shape[Num.first.value].set_shape(Num.second.value, 0, 1); l_shape[Num.first.value].set_shape(Num.third.value, 0, 2); l_shape[Num.first.value].set_shape(Num.forth.value, 0, 3)
    l_shape[Num.second.value].set_shape(Num.first.value, 0, 0); l_shape[Num.second.value].set_shape(Num.second.value, 1, 0); l_shape[Num.second.value].set_shape(Num.third.value, 2, 0); l_shape[Num.second.value].set_shape(Num.forth.value, 3, 0)
    l_shape[Num.third.value].set_shape(Num.first.value, 0, 0); l_shape[Num.third.value].set_shape(Num.second.value, 0, 1); l_shape[Num.third.value].set_shape(Num.third.value, 0, 2); l_shape[Num.third.value].set_shape(Num.forth.value, 0, 3)
    l_shape[Num.forth.value].set_shape(Num.first.value, 0, 0); l_shape[Num.forth.value].set_shape(Num.second.value, 1, 0); l_shape[Num.forth.value].set_shape(Num.third.value, 2, 0); l_shape[Num.forth.value].set_shape(Num.forth.value, 3, 0)

    o_shape[Num.first.value].set_shape(Num.first.value, 0, 0); o_shape[Num.first.value].set_shape(Num.second.value, 1, 0); o_shape[Num.first.value].set_shape(Num.third.value, 0, 1); o_shape[Num.first.value].set_shape(Num.forth.value, 1, 1)
    o_shape[Num.second.value].set_shape(Num.first.value, 0, 0); o_shape[Num.second.value].set_shape(Num.second.value,1, 0); o_shape[Num.second.value].set_shape(Num.third.value, 0, 1); o_shape[Num.second.value].set_shape(Num.forth.value, 1, 1)
    o_shape[Num.third.value].set_shape(Num.first.value, 0, 0); o_shape[Num.third.value].set_shape(Num.second.value, 1, 0); o_shape[Num.third.value].set_shape(Num.third.value, 0, 1); o_shape[Num.third.value].set_shape(Num.forth.value, 1, 1)
    o_shape[Num.forth.value].set_shape(Num.first.value, 0, 0); o_shape[Num.forth.value].set_shape(Num.second.value, 1, 0); o_shape[Num.forth.value].set_shape(Num.third.value, 0, 1); o_shape[Num.forth.value].set_shape(Num.forth.value, 1, 1)

    z_shape[Num.first.value].set_shape(Num.first.value, 0, 0); z_shape[Num.first.value].set_shape(Num.second.value, 1, 0); z_shape[Num.first.value].set_shape(Num.third.value, 1, 1); z_shape[Num.first.value].set_shape(Num.forth.value, 2, 1)
    z_shape[Num.second.value].set_shape(Num.first.value, 1, 0); z_shape[Num.second.value].set_shape(Num.second.value, 0, 1); z_shape[Num.second.value].set_shape(Num.third.value, 1, 1); z_shape[Num.second.value].set_shape(Num.forth.value, 0, 2)
    z_shape[Num.third.value].set_shape(Num.first.value, 0, 0); z_shape[Num.third.value].set_shape(Num.second.value, 1, 0); z_shape[Num.third.value].set_shape(Num.third.value, 1, 1); z_shape[Num.third.value].set_shape(Num.forth.value, 2, 1)
    z_shape[Num.forth.value].set_shape(Num.first.value, 1, 0); z_shape[Num.forth.value].set_shape(Num.second.value, 0, 1); z_shape[Num.forth.value].set_shape(Num.third.value, 1, 1); z_shape[Num.forth.value].set_shape(Num.forth.value, 0, 2)

    i_shape[Num.first.value].set_shape(Num.first.value, 0, 0); i_shape[Num.first.value].set_shape(Num.second.value, 0, 1); i_shape[Num.first.value].set_shape(Num.third.value, 0, 2); i_shape[Num.first.value].set_shape(Num.forth.value, 1, 2)
    i_shape[Num.second.value].set_shape(Num.first.value, 0, 1); i_shape[Num.second.value].set_shape(Num.second.value, 1, 1); i_shape[Num.second.value].set_shape(Num.third.value, 2, 1); i_shape[Num.second.value].set_shape(Num.forth.value, 2, 0)
    i_shape[Num.third.value].set_shape(Num.first.value, 0, 0); i_shape[Num.third.value].set_shape(Num.second.value, 1, 0); i_shape[Num.third.value].set_shape(Num.third.value, 0, 1); i_shape[Num.third.value].set_shape(Num.forth.value, 0, 2)
    i_shape[Num.forth.value].set_shape(Num.first.value, 0, 0); i_shape[Num.forth.value].set_shape(Num.second.value, 1, 0); i_shape[Num.forth.value].set_shape(Num.third.value, 2, 0); i_shape[Num.forth.value].set_shape(Num.forth.value, 0, 1)

    h_shape[Num.first.value].set_shape(Num.first.value, 0, 1); h_shape[Num.first.value].set_shape(Num.second.value, 1, 1); h_shape[Num.first.value].set_shape(Num.third.value, 1, 0); h_shape[Num.first.value].set_shape(Num.forth.value, 2, 0)
    h_shape[Num.second.value].set_shape(Num.first.value, 0, 0); h_shape[Num.second.value].set_shape(Num.second.value, 0, 1); h_shape[Num.second.value].set_shape(Num.third.value, 1, 1); h_shape[Num.second.value].set_shape(Num.forth.value, 1, 2)
    h_shape[Num.third.value].set_shape(Num.first.value, 0, 1); h_shape[Num.third.value].set_shape(Num.second.value, 1, 1); h_shape[Num.third.value].set_shape(Num.third.value, 1, 0); h_shape[Num.third.value].set_shape(Num.forth.value, 2, 0)
    h_shape[Num.forth.value].set_shape(Num.first.value, 0, 0); h_shape[Num.forth.value].set_shape(Num.second.value, 0, 1); h_shape[Num.forth.value].set_shape(Num.third.value, 1, 1); h_shape[Num.forth.value].set_shape(Num.forth.value, 1, 2)
    
'''
(x,y)

(0,0) (1,0) (2,0) (3,0)
(0,1) (1,1) (2,1) (3,1)
(0,2) (1,2) (2,2) (3,2)
(0,3) (1,3) (2,3) (3,3)

<t_shape>
.0.. 0... 000. .0.. 1. (1,0) (0,1) (1,1) (2,1)
000. 00.. .0.. 00.. 2. (0,0) (0,1) (1,1) (0,2)
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

class block:
    def __init__(self) -> None:
        self.left = 100
        self.right = 300
        self.down = 400
    


