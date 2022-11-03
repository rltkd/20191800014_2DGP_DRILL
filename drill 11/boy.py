from pico2d import *

#이벤트 정의

RD, LD, RU, LU, TIMER,A_ON = range(6)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT) : RD,
    (SDL_KEYDOWN, SDLK_LEFT) : LD,
    (SDL_KEYUP, SDLK_RIGHT) : RU,
    (SDL_KEYUP, SDLK_LEFT) : LU,
    (SDL_KEYDOWN,SDLK_a) : A_ON,
    #(SDL_KEYUP,SDLK_a) : A_OFF
}
class AUTO_RUN:
    def enter(self, event):
        print('enter AUTO_run')
        #self.dir 값을 결정해야 함.
        self.dir = self.face_dir
        pass

    def exit(self):
        print('exit AUTO_run')
        #auto run을 나가서 idle로 갈 때, autorun의 방향을 알려줄 필요가 있다.
        self.face_dir = self.dir

        pass

    def do(self):
        self.frame= (self.frame + 1) % 8
        if self.dir == 1:
            self.x += 1
            if self.x ==800:
                self.dir = -1
        elif self.dir == -1:
            self.x -= 1
            if self.x == 0:
                self.dir = 1
        self.x = clamp(0,self.x, 800)
        pass

    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        pass
        #크기 두배로 어케 그려요..?

class SLEEP:
    @staticmethod
    def enter(self, event):
        print('enter SLEEP')
        self.dir = 0
        pass

    @staticmethod
    def exit(self):
        print('enter SLEEP')
        pass

    @staticmethod
    def do(self):
        self.frame = (self.frame +1) % 8
        pass

    @staticmethod
    def draw(self):
        if self.face_dir == 1:#오른쪽을 바라보는 아이들
            self.image.clip_composite_draw(self.frame * 100, 300, 100, 100,
                                 3.141592/2,'',
                                 self.x+25, self.y-25,100,100)
        else:
            self.image.clip_composite_draw(self.frame * 100, 200, 100, 100,
                                           -3.141592/2,'',
                                           self.x+25, self.y-25,100,100)

        pass

#클래스를 이용해 상태를 만듦.
class IDLE:
    @staticmethod
    def enter(self, event):
        print('enter IDLE')
        self.dir = 0
        self.timer =1000
        pass

    @staticmethod
    def exit(self):
        print('enter exit')
        pass

    @staticmethod
    def do(self):
        self.frame = (self.frame +1) % 8
        self.timer -=1
        if self.timer ==0:#시간이 경과하면
            #이벤트 발생 Timer
            #self.q.insert(0,TIMER) #객체 지향 프로그래밍 위배, q를 직접 액세스 해서
            self.add_event(TIMER)
        pass


    @staticmethod
    def draw(self):
        if self.face_dir == 1:#오른쪽을 바라보는 IDLE
            self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)

        pass


class RUN:
    def enter(self, event):
        print('enter run')
        #self.dir 값을 결정해야 함.
        if event == RD: self.dir += 1
        elif event == LD:self.dir -= 1
        elif event == RU: self.dir -= 1
        elif event == LU: self.dir += 1
        pass

    def exit(self):
        print('enter.run')
        #run을 나가서 idle로 갈 때, run의 방향을 알려줄 필요가 있다.
        self.face_dir = self.dir


        pass

    def do(self):
        self.frame=(self.frame + 1) % 8
        self.x +=self.dir
        self.x = clamp(0,self.x, 800)
        pass

    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        pass


next_state = {
    SLEEP: {RD: RUN, LD: RUN, RU:RUN, LU:RUN,A_ON:SLEEP},
    IDLE: {RU: RUN, LU:RUN, RD:RUN, LD:RUN,TIMER: SLEEP, A_ON:AUTO_RUN},
    RUN: {RU: IDLE, LU:IDLE, RD:IDLE, LD:IDLE,A_ON:AUTO_RUN},
    AUTO_RUN: {RU: RUN, LU:RUN, RD:RUN, LD:RUN, A_ON:IDLE}
}




class Boy:
    def add_event(self,event):
        self.q.insert(0, event)

    def handle_event(self,event): # 소년이 스스로 이벤트를 처리할수 있게
        # event 는 키이벤트, 이것을 내부 rd 등으로 변환
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type), event.key]
            self.add_event(key_event) #변환된 내부 이벤트를 큐에 추가



    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('animation_sheet.png')

        self.q = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)


    def update(self):
        self.cur_state.do(self)

        if self.q: # q에 뭔가 있다면
            event = self.q.pop()#이벤트를 가져오고
            self.cur_state.exit(self) #현재 상태를 나가고,
            self.cur_state = next_state[self.cur_state][event] #다음 상태를 계산하기
            self.cur_state.enter(self, event)

        # self.frame = (self.frame + 1) % 8
        # self.x += self.dir * 1
        # self.x = clamp(0, self.x, 800)


    def draw(self):
        self.cur_state.draw(self)
    #     else:
    #         if self.face_dir == 1:
    #             self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
    #         else:
    #             self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)
