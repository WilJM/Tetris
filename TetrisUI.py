from asyncio.windows_events import NULL
import sys
from tkinter import SEL_FIRST
import Tetris
import pygame
import random
from pygame.locals import *

class TetrisUI():
    """
    테트리스 UI를 관리하는 클래스

    Attributes:
        screen          : 게임 디스플레이 객체
        clock           : 게임 내의 시간
        speed           : 1초당 떨어지는 속도
        now             : 0~23내의 무작위 수(24가지 블록 무작위로 나오게 하기 위한 변수)
        one_block       : 하, 좌, 우 움직이는 거리 
        currnet_x       : 처음 도형 시작하는 x좌표
        current_y       : 처음 도형 시작하는 y좌표
        current_block   : 현재 움직일 수 있는 도형(Tetris.Current 객체)
        game_map        : 현재 쌓여있는 블럭들 (Tetris.Block 객체)
        block           : now변수를 사용하여 나온 블록

    Methods:
        game_start      : 게임 시작 함수
        event_quit      : 게임 종료 함수
        key_event       : 방향키에 따른 블록 움직임을 나타내는 함수
        block_event     : 바닥에 닿은경우, 쌓여있는 사각형에 닿을 때 currnet_block -> game_map으로 변경 및 저장
        erase_line      : 한줄에 특정 갯수만큼 다 찬 경우 라인을 지워주는 함수 (list)
    """
    def __init__(self, size=[800,600], speed=1):
        pygame.init()    ##파이게임 시작
        self.screen = pygame.display.set_mode(size) ## 디스플레이객체를 가로800, 세로 600 픽셀의 크기로 생성

        pygame.display.set_caption("Tetris")    ##캡션을 Tetris로 출력
        self.clock = pygame.time.Clock()
        self.speed = speed 
        self.now = random.randint(0,23)
        self.one_block = 10 
        self.current_x = 100 
        self.current_y = 100 
        self.__bottom = 390
        self.current_block = Tetris.Current() 
        self.game_map = Tetris.Stack() 
        self.block = Tetris.rand_block(self.now) 

    def game_start(self): 
        Tetris.init_shape()       
        while True:
            self.current_y += self.speed
            
            for event in pygame.event.get():
                if event.type == QUIT:          ##종료버튼이 눌리면
                    self.event_quit()
                
                self.key_event(pygame.key.get_pressed())

            self.screen.fill((0,0,0))

            for i in range(4):
                self.current_block.set_square(i, self.current_x + self.block[i][1], self.current_y + self.block[i][0])
                pygame.draw.rect(self.screen,(255,255,255),(self.current_block.get_square_x(i), self.current_block.get_square_y(i) , 10, 10))
           
            self.block_event()
            num_erase = self.erase_line()
            
            if len(num_erase) > 0:
                for lst in num_erase:
                    self.game_map.stack_down(lst)
            
            if len(self.game_map.stacks) > 0:
                for i in range(len(self.game_map.stacks)):
                    pygame.draw.rect(self.screen,(255,255,255),(self.game_map.get_stack(i)[1], self.game_map.get_stack(i)[0], 10, 10))

            pygame.draw.lines(self.screen,(255,255,255), True, [[100,100],[100,400],[300,400],[300,100]],1)

            for i in range(4):
                pygame.draw.rect(self.screen,(255,255,255),(self.block[i][1], self.block[i][0], 10, 10))

            
            pygame.display.update()         ##이벤트처리후 디스플레이 출력
            self.clock.tick(10)

    def event_quit(self):
        pygame.quit()
        sys.exit()

    def key_event(self, event:pygame.key.get_pressed):
        if event is NULL:
            event = pygame.key.get_pressed()

        if event[pygame.K_LEFT]:
            for i in range(4):
                if self.current_x + self.block[i][1] <= 100:
                    return
                #if len(self.game_map.stacks) > 0:    
                for lst in self.game_map.stacks:
                    if self.current_y + self.block[i][0] <= lst[0] and lst[0] <= self.current_y + self.block[i][0] + 10:   
                        if self.current_x + self.block[i][1] == lst[1] + 10:
                            return
            self.current_x -= self.one_block

        elif event[pygame.K_RIGHT]:
            for i in range(4):
                if self.current_x + self.block[i][1] >= 290:
                    return

                #if len(self.game_map.stacks) > 0:    
                for lst in self.game_map.stacks:
                    if self.current_y + self.block[i][0] <= lst[0] and lst[0] <= self.current_y + self.block[i][0] + 10:   
                        if self.current_x + self.block[i][1]+10 == lst[1]:
                            return
            self.current_x += self.one_block

        elif event[pygame.K_DOWN]:
            self.current_y += self.one_block
            self.block_event()

        elif event[pygame.K_UP]:
            self.now = (self.now + 6) % 24
            self.block = Tetris.rand_block(self.now)

        elif event[pygame.K_SPACE]:
            self.block_fall_predict()

    def block_fall_predict(self):

        now_x = set(self.current_block.get_square_x(0))
        lowest_y = self.current_block.get_lowest_y()
        for i in range(1,4):
            now_x.add(self.current_block.get_square_x(i))

        for block in self.game_map.stacks: # 쌓여있는 블럭에서 현재 좌표에서의 가장 높은 높이 리턴
            block[0]

    def block_event(self):
        for i in range(4):
            if self.current_block.get_square_y(i) >= self.__bottom: # 바닥에 닿은 경우
                self.current_block.set_square_y(self.__bottom)
                self.game_map.set_stacks(self.current_block.get_square())
                for j in range(4):
                    self.game_map.add_count_y(self.current_block.get_square_y(j))
                self.current_block.__init__()
                self.current_x = 100; self.current_y = 100
                self.now = random.randint(0,23)
                self.block = Tetris.rand_block(self.now)
                return
            for block in self.game_map.stacks: # 쌓인 블럭에 닿은 경우
                if  self.current_block.get_square_y(i) + 10 >= block[0] and self.current_block.get_square_x(i) == block[1]:
                    self.current_block.set_square_y(block[0]-10)
                    self.game_map.set_stacks(self.current_block.get_square())
                    for j in range(4):
                        self.game_map.add_count_y(self.current_block.get_square_y(j))
                    self.current_block.__init__()
                    self.current_x = 100; self.current_y = 100
                    self.now = random.randint(0,23)
                    self.block = Tetris.rand_block(self.now)
                    return 

    def erase_line(self) ->list:
        key_list = []
        for key in self.game_map.count_y:
            if self.game_map.count_y[key] == 20:
                self.game_map.remove_list(key)
                key_list.append(key) 
        return key_list

    