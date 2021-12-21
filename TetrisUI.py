import sys
import Tetris
import pygame
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
        self.pos_x = [0,0,0,0]
        self.pos_y = [0,0,0,0]
        self.now = 0
        self.one_block = 10 # 좌우 움직이는 거리
        self.current_x = 100
        self.current_y = 100

    def game_start(self):
        while True:
            self.current_y += self.speed
            
            for event in pygame.event.get():
                if event.type == QUIT:          ##종료버튼이 눌리면
                    self.quit()
                
                self.key_event(pygame.key.get_pressed())
            
            self.screen.fill((0,0,0))

            for i in range(4):
                self.pos_x[i] = self.current_x + Tetris.t_shape[self.now].get_shape_x(i)
                self.pos_y[i] = self.current_y + Tetris.t_shape[self.now].get_shape_y(i)
                pygame.draw.rect(self.screen,(255,255,255),(self.pos_x[i], self.pos_y[i] , 10, 10))

            pygame.draw.lines(self.screen,(255,255,255),True, [[100,100],[100,400],[300,400],[300,100]],5)

            pygame.display.update()         ##이벤트처리후 디스플레이 출력
            self.clock.tick(10)

    def event_quit(self):
        pygame.quit()
        sys.exit()

    def key_event(self, event:pygame.key.get_pressed):
        if event is None:
            event = pygame.key.get_pressed()

        if event[pygame.K_LEFT]:
            self.current_x -= self.one_block

        elif event[pygame.K_RIGHT]:
            self.current_x += self.one_block

        elif event[pygame.K_DOWN]:
            self.current_y += self.one_block

        elif event[pygame.K_UP]:
            self.now = (self.now + 1) % 4
            for i in range(4):
                self.pos_x[i] = self.current_x + Tetris.t_shape[self.now].get_shape_x(i)
                self.pos_y[i] = self.current_y + Tetris.t_shape[self.now].get_shape_y(i)

        Tetris.init_shape()

        for i in range(4):
            self.pos_x[i] = Tetris.t_shape[self.now].get_shape_x(i)
            self.pos_y[i] = Tetris.t_shape[self.now].get_shape_y(i)

    
