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
    """
    def __init__(self, size=[800,600], speed=1):
        pygame.init()    ##파이게임 시작
        self.screen = pygame.display.set_mode(size) ## 디스플레이객체를 가로800, 세로 600 픽셀의 크기로 생성

        pygame.display.set_caption("Tetris")    ##캡션을 hello world로 출력
        self.clock = pygame.time.Clock()
        self.speed = speed # 1초당 떨어지는 속도(난이도)
        self.now = random.randint(0,23)
        self.one_block = 10 # 좌우 움직이는 거리
        self.current_x = 100 #처음 도형 시작하는 x좌표
        self.current_y = 100 #처음 도형 시작하는 y좌표
        self.current_block = Tetris.Current() #현재 움직일 수 있는 도형
        self.game_map = Tetris.Block() #쌓여 있는 블럭들
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
                self.current_block.set_pos(i, self.current_x + self.block[i][1], self.current_y + self.block[i][0])
                pygame.draw.rect(self.screen,(255,255,255),(self.current_block.get_pos_x(i), self.current_block.get_pos_y(i) , 10, 10))
           
            self.block_event()

            if len(self.game_map.blocks) > 0:
                for i in range(len(self.game_map.blocks)):
                    pygame.draw.rect(self.screen,(255,255,255),(self.game_map.get_blocks(i)[1], self.game_map.get_blocks(i)[0], 10, 10))

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
                if len(self.game_map.blocks) > 0:    
                    for lst in self.game_map.blocks:
                        if self.current_y + self.block[i][0] <= lst[0] and lst[0] <= self.current_y + self.block[i][0] +10:   
                            if self.current_x + self.block[i][1] == lst[1] + 10:
                                return
            self.current_x -= self.one_block

        elif event[pygame.K_RIGHT]:
            for i in range(4):
                if self.current_x + self.block[i][1] >= 290:
                    return

                if len(self.game_map.blocks) > 0:    
                    for lst in self.game_map.blocks:
                        if self.current_y + self.block[i][0] <= lst[0] and lst[0] <= self.current_y + self.block[i][0] +10:   
                            if self.current_x + self.block[i][1]+10 == lst[1]:
                                return
            self.current_x += self.one_block

        elif event[pygame.K_DOWN]:
            self.current_y += self.one_block

        elif event[pygame.K_UP]:
            self.now = (self.now + 6) % 24
            self.block = Tetris.rand_block(self.now)


    def block_event(self):
        for i in range(4):
            if self.current_block.get_pos_y(i) == 390:
                self.game_map.set_block(self.current_block.get_pos())
                self.current_block.__init__()
                self.current_x = 100; self.current_y = 100
                self.now = random.randint(0,23)
                self.block = Tetris.rand_block(self.now)
                return
            for block in self.game_map.blocks:
                if self.current_block.get_pos_y(i) + 10== block[0] and self.current_block.get_pos_x(i) == block[1]:
                   self.game_map.set_block(self.current_block.get_pos())
                   self.current_block.__init__()
                   self.current_x = 100; self.current_y = 100
                   self.now = random.randint(0,23)
                   self.block = Tetris.rand_block(self.now)
                   return 
