import collections
import pygame
import random
# initialize game engine
pygame.init()

window_width=1100
window_height=1200

animation_increment=10
clock_tick_rate=20

# Open a window
size = (window_width, window_height)
screen = pygame.display.set_mode(size)

# Set title to the window
pygame.display.set_caption("scotlandYardv3.0")
clock = pygame.time.Clock()
background_image = pygame.image.load("resources/images/map.jpg").convert()
player1 = pygame.image.load("resources/images/flag1.gif").convert()
player2 = pygame.image.load("resources/images/flag2.gif").convert()
player3 = pygame.image.load("resources/images/flag3.gif").convert()
player4 = pygame.image.load("resources/images/flag4.gif").convert()
player5 = pygame.image.load("resources/images/flag5.gif").convert()


dead=False

def start():
    cord_node = []
    arr = []
    with open('SCOTPOS.txt','r') as f:
        for line in f:
            list = []
            for word in line.split():
                list.append(word)
            cord = tuple(list)
            cord_node.append(cord)          

    start_station = [103,112,34,155,94,117,132,53,174,198,50,91,26,29,141,13,138,197]
    num = 6
    random_start = random.sample(start_station, num)
    start1 = random_start[0]
    start2 = random_start[1]
    start3 = random_start[2]
    start4 = random_start[3]
    start5 = random_start[4]
    mr_x = random_start[5]

    cord1 = (cord_node[start1][1],cord_node[start1][2])
    x1 =int(cord1[0])
    y1 = int(cord1[1])
    arr.append((x1,y1))

    cord2 = (cord_node[start2][1],cord_node[start2][2])
    x2 =int(cord2[0])
    y2 = int(cord2[1])
    arr.append((x2,y2))


    cord3 = (cord_node[start3][1],cord_node[start3][2])
    x3 =int(cord3[0])
    y3 = int(cord3[1])
    arr.append((x3,y3))


    cord4 = (cord_node[start4][1],cord_node[start4][2])
    x4 =int(cord4[0])
    y4 = int(cord4[1])
    arr.append((x4,y4))


    cord5 = (cord_node[start5][1],cord_node[start5][2])
    x5 =int(cord5[0])
    y5 = int(cord5[1])
    arr.append((x5,y5))

    cord_mr_x = (cord_node[mr_x][1],cord_node[mr_x][2])
    xx =int(cord_mr_x[0])
    yx = int(cord_mr_x[1])
    arr.append((xx,yx))
    return arr

c = start()
while(dead==False):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dead = True

    screen.blit(background_image, [0, 0])
    x1 = int(c[0][0])
    y1 = int(c[0][1])
    screen.blit(player1,[x1,y1-50])
    x2 = int(c[1][0])
    y2 = int(c[1][1])
    screen.blit(player2,[x2,y2-50])
    x3 = int(c[2][0])
    y3 = int(c[2][1])
    screen.blit(player3,[x3,y3-50])
    x4 = int(c[3][0])
    y4 = int(c[3][1])
    screen.blit(player4,[x4,y4-50])
    x5 = int(c[4][0])
    y5 = int(c[4][1])
    screen.blit(player5,[x5,y5-50])
    pygame.display.flip()
    clock.tick(clock_tick_rate)

sgraph = {}
def map():
    global sgraph
    cord_node = []
    arr = []
    with open('SCOTMAP.txt','r') as f:
        for line in f:
            list = []
            for word in line.split():
                list.append(word)
            cord = tuple(list)
            cord_node.append(cord)
    graph = {}
    for i in range(470):
        u = cord_node[i][0]
        v = cord_node[i][1]
        w = cord_node[i][2]
        graph.setdefault(u,[]).append((v,w))
    sgraph = collections.OrderedDict(sorted(graph.items()))
    print(sgraph)
map()

def poss_moves(curr_pos):
    global sgraph
    lis = []
    #length = len(sgraph[curr_pos])
    lis = sgraph[curr_pos]
    return lis
list = poss_moves('123')
print(list)
