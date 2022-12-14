import random
from pico2d import *
import game_world
import game_framework
import server
from background import FixedBackground
class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.fall_speed = random.randint(0, 1837), random.randint(0,1109), 0

    def get_bb(self):
        # fill here
        return self.x -server.background.window_left- 10, self.y -server.background.window_bottom- 10,self.x -server.background.window_left+ 10, self.y-server.background.window_bottom + 10

    def draw(self):
        self.image.draw(self.x-server.background.window_left, self.y-server.background.window_bottom)
        # fill here
        draw_rectangle(*self.get_bb())

    def update(self):
        self.y -= self.fall_speed * game_framework.frame_time

    def stop(self):
        self.fall_speed = 0

    def handle_collision(self, other, group):
        game_world.remove_object(self)

class BigBall(Ball):
    MIN_FALL_SPEED = 50  # 50 pps = 1.5 meter per sec
    MAX_FALL_SPEED = 200 # 200 pps = 6 meter per sec
    image = None

    def __init__(self):
        if BigBall.image == None:
            BigBall.image = load_image('ball41x41.png')
        self.x, self.y, self.fall_speed = random.randint(0, 1600-1), 500, random.randint(BigBall.MIN_FALL_SPEED, BigBall.MAX_FALL_SPEED)


    def get_bb(self):
        return self.x -server.background.window_left- 20, self.y -server.background.window_bottom- 20,self.x -server.background.window_left+ 20, self.y-server.background.window_bottom + 20

