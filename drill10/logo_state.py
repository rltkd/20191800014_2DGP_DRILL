from pico2d import *
import game_framework
import play_state
import title_state
image = None
logo_time= 0.0
def enter():
    global image, logo_time
    image = load_image('tuk_credit.png')
    logo_time = 0.0
    pass

def exit():
    global image
    del image
    pass

def update():
    global logo_time
    # fill here
    delay(0.05)
    logo_time += 0.05
    if logo_time > 1.0:
        game_framework.change_state(title_state)
    pass

def draw():
    # fill here
    clear_canvas()
    image.draw(400,300)
    update_canvas()
    pass

def handle_events():
    events = get_events()





