import pygame
import sys       ##sys 모듈 임포트
import Tetris
from pygame.locals import *

pygame.init()    ##파이게임 시작

DISPLAY = pygame.display.set_mode((800,600)) ##디스플레이객체를 가로800, 세로 600 픽셀의 크기로 생성

pygame.display.set_caption("Tetris")    ##캡션을 hello world로 출력
clock = pygame.time.Clock()
Tetris.init_shape()
pos_x = [0,0,0,0] ; pos_y = [0,0,0,0]
now = 0
one_block = 10
current_x = 100; current_y = 100
for i in range(4):
    pos_x[i] = Tetris.t_shape[now].get_shape_x(i); pos_y[i] = Tetris.t_shape[now].get_shape_y(i)

while True :      ##무한루프(여기가 게임 진행시 이벤트 처리코드가 들어가는 곳
    
    current_y += 1

    for event in pygame.event.get():    ##이벤트가 발생하면 실행되는 루프
        if event.type == QUIT:          ##종료버튼이 눌리면
            pygame.quit()               ##파이게임을 종료
            sys.exit()                  ##프로그램 종료
        
        key_event = pygame.key.get_pressed()
    
        if key_event[pygame.K_LEFT]:
            current_x -= one_block
            #for i in range(4):
            #   pos_x[i] -= one_block

        elif key_event[pygame.K_RIGHT]:
            current_x += one_block
            #for i in range(4):
            #    pos_x[i] += one_block

        elif key_event[pygame.K_DOWN]:
            current_y += one_block
            #for i in range(4):
            #    pos_y[i] += one_block

        elif key_event[pygame.K_UP]:
            now = (now+1)%4
            for i in range(4):
                pos_x[i] = current_x + Tetris.t_shape[now].get_shape_x(i);  pos_y[i] = current_y + Tetris.t_shape[now].get_shape_y(i)
    
    DISPLAY.fill((0,0,0))
    #pygame.draw.circle(DISPLAY, (255,255,255), (Tetris.t_shape[0].get_shape_x(1), Tetris.t_shape[0].get_shape_y(1)), 20)
    for i in range(4):
        pos_x[i] = current_x + Tetris.t_shape[now].get_shape_x(i);  pos_y[i] = current_y + Tetris.t_shape[now].get_shape_y(i)
        pygame.draw.rect(DISPLAY,(255,255,255),(pos_x[i], pos_y[i] , 10, 10))

    pygame.draw.lines(DISPLAY,(255,255,255),True, [[100,100],[100,400],[300,400],[300,100]],5)

    pygame.display.update()         ##이벤트처리후 디스플레이 출력
    clock.tick(10)

