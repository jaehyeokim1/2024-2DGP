from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

# 사각형 이동
def move_in_square():
    x = 0
    y = 90
    
    while x < 800:  # 오른쪽으로 이동
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 90)
        x += 5
        delay(0.01)
    
    while y < 600:  # 위쪽으로 이동
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(780, y)
        y += 5
        delay(0.01)
    
    while x > 0:  # 왼쪽으로 이동
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 550)
        x -= 5
        delay(0.01)
    
    while y > 90:  # 아래쪽으로 이동
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(0, y)
        y -= 5
        delay(0.01)

# 원형 이동
def move_in_circle():
    center_x = 400  # 원의 중심 x좌표
    center_y = 300  # 원의 중심 y좌표
    radius = 200    # 원의 반지름
    angle = 0       # 초기 각도 (라디안 단위)

    while angle < 2 * math.pi:  # 0부터 2π(360도)까지 회전
        clear_canvas_now()
        grass.draw_now(400, 30)
        x = center_x + radius * math.cos(angle)  # x좌표 계산
        y = center_y + radius * math.sin(angle)  # y좌표 계산
        character.draw_now(x, y)
        angle += 0.05  # 각도 증가 (속도 조절)
        delay(0.01)

# 무한 반복
while True:
    move_in_square()  # 사각형으로 이동
    move_in_circle()  # 원으로 이동

close_canvas()
