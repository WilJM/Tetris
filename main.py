import pygame
import sys       ##sys 모듈 임포트

from pygame.locals import *

pygame.init()    ##파이게임 시작

DISPLAY = pygame.display.set_mode((800,600)) ##디스플레이객체를 가로800, 세로 600 픽셀의 크기로 생성

pygame.display.set_caption("Hello world")    ##캡션을 hello world로 출력

while True :      ##무한루프(여기가 게임 진행시 이벤트 처리코드가 들어가는 곳
    for event in pygame.event.get():    ##이벤트가 발생하면 실행되는 루프
        if event.type == QUIT:          ##종료버튼이 눌리면
            pygame.quit()               ##파이게임을 종료
            sys.exit()                  ##프로그램 종료
        pygame.display.update()         ##이벤트처리후 디스플레이 출력


