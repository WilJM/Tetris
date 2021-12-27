'''
블록을 관리하기 위한 라이브러리

    사각형  : 정사각형 1개
    블록    : 사각형이 4개가 모여 형성되는 테트리스의 기본적인 도형 
    ex )     
            0000  <--- 블록,  0 <- 사각형
'''
from enum import Enum

class Num(Enum):
    '''
    first, second, thrid, forth를 1, 2, 3, 4로 표현하기 위한 Enum 열거 클래스
    '''
    first =0; second =1; third=2; forth =3

class Shape:
    '''
    블록의 각 모양을 x좌표, y좌표로 표현하기 위한 클래스
    사각형 4개를 합쳐 하나의 블록을 만들기 위함
    
    Attributes:
        point       : 4개의 사각형의 [y,x] 좌표 (list)
        rect_size   : point에서 1을 한칸으로 기준했기 때문에 원하는 사각형의 크기를 맞추기 위한 상수 (int)
    Methods:
        set_shape   : num을 통해 원하는 사각형의 x, y좌표를 지정할 수 있음
        get_shape_x : num번째 사각형의 x좌표 return
        get_shape_y : num번째 사각형의 y좌표 return
    '''
    def __init__(self) -> None:
        self.point = [[0,0], [0,0], [0,0], [0,0]]
        self.rect_size = 10
    def set_shape(self, num, x, y) -> None:
        self.point[num][1] = x * self.rect_size
        self.point[num][0] = y * self.rect_size

    def get_shape_x(self, num):
        return self.point[num][1]

    def get_shape_y(self, num):
        return self.point[num][0]

t_shape = [Shape(), Shape(), Shape(), Shape()]
l_shape = [Shape(), Shape(), Shape(), Shape()]
o_shape = [Shape(), Shape(), Shape(), Shape()]
z_shape = [Shape(), Shape(), Shape(), Shape()]
i_shape = [Shape(), Shape(), Shape(), Shape()]
h_shape = [Shape(), Shape(), Shape(), Shape()]

'''
한 블럭 당 4가지의 회전한 모양이 있기 때문에 shape 클래스 객체를 이용해 list형식으로 선언함
t_shape경우 ㅗ ㅜ ㅏ ㅓ 네가지의 90도 회전한 모양 존재를 shape 클래스 객체로 표현
'''

def init_shape():
    '''
    t_shape, l_shape, o_shape, z_shape, i_shape, h_shape 블럭의 4가지 회전모양을 초기화한다.

    (y,x)

    (0,0) (0,1) (0,2) (0,3)
    (1,0) (1,1) (1,2) (1,3)
    (2,0) (2,2) (2,2) (2,3)
    (3,0) (3,1) (3,2) (3,3)

    <t_shape>
    .0.. 0... 000. .0.. 1. (0,1) (1,0) (1,1) (1,2)
    000. 00.. .0.. 00.. 2. (0,0) (1,0) (1,1) (2,0)
    .... 0... .... .0.. 3. (0,0) (0,1) (0,2) (1,1)
    .... .... .... .... 4. (0,1) (1,0) (1,1) (2,1)

    <l_shape>
    0... 0000 0... 0000 1. (0,0) (1,0) (2,0) (3,0)
    0... .... 0... .... 2. (0,0) (0,1) (0,2) (0,3)
    0... .... 0... .... 3. (0,0) (1,0) (2,0) (3,0)
    0... .... 0... .... 4. (0,0) (0,1) (0,2) (0,3)

    <o_shape>
    00.. 00.. 00.. 00.. 1. (0,0) (0,1) (1,0) (1,1)
    00.. 00.. 00.. 00.. 2. (0,0) (0,1) (1,0) (1,1)
    .... .... .... .... 3. (0,0) (0,1) (1,0) (1,1)
    .... .... .... .... 4. (0,0) (0,1) (1,0) (1,1)

    <z_shape>
    00.. .0.. 00.. .0.. 1. (0,0) (0,1) (1,1) (1,2)
    .00. 00.. .00. 00.. 2. (0,1) (1,0) (1,1) (2,0)
    .... 0... .... 0... 3. (0,0) (0,1) (1,1) (1,2)
    .... .... .... .... 4. (0,1) (1,0) (1,1) (2,0)

    <i_shape>
    0... ..0. 00.. 000. 1. (0,0) (1,0) (2,0) (2,1)
    0... 000. .0.. 0... 2. (1,0) (1,1) (1,2) (0,2) 
    00.. .... .0.. .... 3. (0,0) (0,1) (1,0) (2,0) 
    .... .... .... .... 4. (0,0) (0,1) (0,2) (1,0) 

    <h_shape>
    .00. 0... .00. 0... 1. (1,0) (1,1) (0,1) (0,2)
    00.. 00.. 00.. 00.. 2. (0,0) (1,0) (1,1) (2,1)
    .... .0.. .... .0.. 3. (1,0) (1,1) (0,1) (0,2)
    .... .... .... .... 4. (0,0) (1,0) (1,1) (2,1)

    '''
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


class Block:
    '''
    쌓여있는 사각형들을 저장하는 클래스
    
    Attributes:
        blocks      : 쌓여있는 사각형들  (list)
        dic_y       : y축 기준으로 사각형이 몇개 있는 지 key : y값, value : 사각형 갯수 (dictionary)
    Methods:
        get_blocks  : num번째 쌓여있는 사각형의 list 리턴
        set_block   : 쌓이는 블럭이 생길 시 list에 추가
        add_dic_y   : dic_y 딕셔너리에 key, value 추가
    '''
    def __init__(self) -> None:
        self.blocks = []
        self.dic_y = {}

    def get_blocks(self, num)-> list:
        return self.blocks[num]
    
    def set_block(self,list_a):
        self.blocks += list_a
    
    def add_dic_y(self, key):
        check = self.dic_y.get(key)
        if check == None:
            self.dic_y[key] = 1
        else:
            self.dic_y[key] += 1

    def erase_line(self, num):
        while 1:
            count =0
            for b in self.blocks:
                if b[0] == num:
                    count += 1
                    self.blocks.remove(b)
            if count ==0:
                break

    def push_down(self, num):
        for block in self.blocks:
            if block[0] < num:
                block[0] += 10
        self.change_key(num)
        
    def change_key(self, num):
        self.dic_y[num] =0
        for key in list(self.dic_y):
            if key < num:
                self.dic_y[key + 10]=self.dic_y.pop(key)

    def end_game(self):
        pass

class Current:
    '''
    블록의 각 모양을 x좌표, y좌표로 표현하기 위한 클래스
    사각형 4개를 합쳐 하나의 블록을 만들기 위함
    
    Attributes:
        point       : 4개의 사각형의 [y,x] 좌표 (list)
        rect_size   : point에서 1을 한칸으로 기준했기 때문에 원하는 사각형의 크기를 맞추기 위한 상수 (int)
    Methods:
        set_shape   : num을 통해 원하는 사각형의 x, y좌표를 지정할 수 있음
        get_shape_x : num번째 사각형의 x좌표 return
        get_shape_y : num번째 사각형의 y좌표 return
    '''
    def __init__(self) -> None:
        self.shpae_num = 0
        self.pos = [[0,0], [0,0], [0,0], [0,0]]
    
    def set_pos(self, num, x, y):
        self.pos[num] = [y,x]

    def get_pos(self) ->list[list]:
        return self.pos

    def get_pos_x(self, num) ->int:
        return self.pos[num][1]

    def get_pos_y(self, num) ->int:
        return self.pos[num][0]


def rand_block(num)->list:
    '''
    처음 나오는 블럭 형태를 랜덤으로 하기 위해 만든 함수
    '''
    rand_shape = []
    for i in range(4):
        rand_shape += [t_shape[i].point] + [l_shape[i].point] + [o_shape[i].point] + [z_shape[i].point] + [i_shape[i].point] + [i_shape[i].point]
    return rand_shape[num]