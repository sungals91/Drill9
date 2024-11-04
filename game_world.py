#world = [] # 단일 계층 구조

#world[0] # 백그라운드 객체들
#world[1] # 포어그라운드 객체들

world = [ [], [], [] ]

def add_object(o, depth):
    world[depth].append(o)

def update():
    for layer in world:
        for o in layer:
            o.update()

def render():
    for layer in world:
        for o in layer:
            o.draw()

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return # 지우는 미션 달성. 다른 요소는 더 이상 체크(반복)할 필요가 없음.

    print('에러: 존재하지 않은 객체를 지운다고?')