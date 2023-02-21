N = int(input())
# area
UP, DOWN, FRONT, BACK, LEFT, RIGHT = 0, 1, 2, 3, 4, 5
area_to_variable = {
    'U': UP,
    'D': DOWN,
    'F': FRONT,
    'B': BACK,
    'L': LEFT,
    'R': RIGHT,
}
# color
white, yellow, red, orange, green, blue = 0, 1, 2, 3, 4, 5
color_to_str = {
    0: 'w',
    1: 'y',
    2: 'r',
    3: 'o',
    4: 'g',
    5: 'b'
}
# direction
CLOCKWISE, COUNTER_CLOCKWISE = '+', '-'


def _rotate_area(cube, area, direction):
    ret = [[None for _ in range(3)] for _ in range(3)]
    ret[1][1] = cube[area][1][1]
    if direction == CLOCKWISE:    
        # corner
        ret[0][0] = cube[area][2][0]
        ret[0][2] = cube[area][0][0]
        ret[2][2] = cube[area][0][2]
        ret[2][0] = cube[area][2][2]
        # edge
        ret[0][1] = cube[area][1][0]
        ret[1][2] = cube[area][0][1]
        ret[2][1] = cube[area][1][2]
        ret[1][0] = cube[area][2][1]
    else:
        #corner
        ret[0][0] = cube[area][0][2]
        ret[0][2] = cube[area][2][2]
        ret[2][2] = cube[area][2][0]
        ret[2][0] = cube[area][0][0]
        # edge
        ret[0][1] = cube[area][1][2]
        ret[1][2] = cube[area][2][1]
        ret[2][1] = cube[area][1][0]
        ret[1][0] = cube[area][0][1]

    for i in range(3):
        for j in range(3):
            cube[area][i][j] = ret[i][j]
        

    #for x in range(3):
    #    for y in range(3):
    #        dx, dy = (x - 1, y - 1)
    #        # rotated dx, rotated dy
    #        rdx, rdy = dy if direction == CLOCKWISE else -dy, dx
    #        ret[1 + rdx][1 + rdy] = area[x][y]
    #return ret


def _horizontally_rotate_side_areas(cube, area, direction):
    x = 0 if area == UP else 2
    #print(f'target row: {x}')

    from_ = {
        FRONT: [cube[FRONT][x][y] for y in range(3)],
        BACK: [cube[BACK][x][y] for y in range(3)],
        LEFT: [cube[LEFT][x][y] for y in range(3)],
        RIGHT: [cube[RIGHT][x][y] for y in range(3)],
    }

    if area == UP:
        direction = CLOCKWISE if direction == COUNTER_CLOCKWISE else COUNTER_CLOCKWISE

    to = {
        FRONT: from_[RIGHT] if direction == CLOCKWISE else from_[LEFT],
        BACK: from_[LEFT] if direction == CLOCKWISE  else from_[RIGHT],
        LEFT: from_[FRONT] if direction == CLOCKWISE  else from_[BACK],
        RIGHT: from_[BACK] if direction == CLOCKWISE  else from_[FRONT],
    }

    for area in to:
        cube[area][x] = to[area]


def _vertically_rotate_fb_side_areas(cube, area, direction):
    x = 2 if area == FRONT else 0
    left_y = 2 if area == FRONT else 0
    right_y = 0 if area == FRONT else 2
    from_ = {
            UP: [cube[UP][x][y] for y in range(3)],
            DOWN: [cube[DOWN][x][y] for y in range(3)],
            LEFT: [cube[LEFT][_x][left_y] for _x in range(3)],
            RIGHT: [cube[RIGHT][_x][right_y] for _x in range(3)],
        }

    if area == BACK:
        direction = CLOCKWISE if direction == COUNTER_CLOCKWISE else COUNTER_CLOCKWISE

    if direction == CLOCKWISE:
        from_[LEFT].reverse()
        from_[RIGHT].reverse()
    else:
        from_[UP].reverse()
        from_[DOWN].reverse()

    to = {
        UP: from_[LEFT] if direction == CLOCKWISE else from_[RIGHT],
        DOWN: from_[RIGHT] if direction == CLOCKWISE  else from_[LEFT],
        LEFT: from_[DOWN] if direction == CLOCKWISE  else from_[UP],
        RIGHT: from_[UP] if direction == CLOCKWISE  else from_[DOWN],
    }

    for area in to:
        if area == UP or area == DOWN:
            cube[area][x] = to[area]
        else:
            y = left_y if area == LEFT else right_y
            for i in range(3): cube[area][i][y] = to[area][i]


def _vertically_rotate_lr_side_areas(cube, area, direction):
    y = 2 if area == RIGHT else 0
    front_y = 2 if area == RIGHT else 0
    back_y = 0 if area == RIGHT else 2
    from_ = {
            UP: [cube[UP][x][y] for x in range(3)],
            DOWN: [cube[DOWN][x][y] for x in range(3)],
            FRONT: [cube[FRONT][x][front_y] for x in range(3)],
            BACK: [cube[BACK][x][back_y] for x in range(3)],
        }

    if area == RIGHT:
        direction = CLOCKWISE if direction == COUNTER_CLOCKWISE else COUNTER_CLOCKWISE

    if direction == CLOCKWISE:
        from_[UP].reverse()
        from_[DOWN].reverse()
    else:
        from_[FRONT].reverse()
        from_[BACK].reverse()

    to = {
        UP: from_[BACK] if direction == CLOCKWISE else from_[FRONT],
        DOWN: from_[FRONT] if direction == CLOCKWISE  else from_[BACK],
        FRONT: from_[UP] if direction == CLOCKWISE  else from_[DOWN],
        BACK: from_[DOWN] if direction == CLOCKWISE  else from_[UP],
    }

    for area in to:
        for i in range(3):
            cube[area][i][y] = to[area][i]



def rotate(cube, area, direction):
    # 어떤 면을 돌리는 건 항상 똑같음
    _rotate_area(cube, area, direction)
    # 사이드 면을 어떻게 돌릴 것인가가 중요
    if area == UP or area == DOWN:
        #print(f'Rotate horizontally {area}, {direction}')
        _horizontally_rotate_side_areas(cube, area, direction)
    elif area == FRONT or area == BACK:
        #print(f'Rotate vertically fb side {area}, {direction}')
        _vertically_rotate_fb_side_areas(cube, area, direction)
    else:
        #print(f'Rotate vertically lr side {area}, {direction}')
        _vertically_rotate_lr_side_areas(cube,area, direction)

def print_area(cube, area):
    area_up = cube[area]
    for i in range(len(area_up)):
        for j in range(len(area_up[0])):
            print(color_to_str[area_up[i][j]], end='')
        print()

while N:
    cube = [
        [[white for _ in range(3)] for _ in range(3)],
        [[yellow for _ in range(3)] for _ in range(3)],
        [[red for _ in range(3)] for _ in range(3)],
        [[orange for _ in range(3)] for _ in range(3)],
        [[green for _ in range(3)] for _ in range(3)],
        [[blue for _ in range(3)] for _ in range(3)],
    ]
    M = int(input())
    methods = list(map(lambda e: (area_to_variable[e[0]], e[1:2]), input().split()))

    for area, direction in methods:
        rotate(cube, area, direction)
        
    print_area(cube, UP)
    N -= 1
