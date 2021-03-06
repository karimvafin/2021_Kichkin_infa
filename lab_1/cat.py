import pygame
import math
import pygame.draw as d

pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 600))
gray = (128, 128, 128)
brown = (0, 100, 0)
lightBlue = (176, 196, 222)
white = (255, 255, 255)
pink = (255, 192, 203)
gray = (128, 128, 128)
red = (220, 20, 60)
orange = (255, 0, 0)
cat = (255, 99, 71)
screen.fill(brown)

def draw_window():
    d.rect(screen, (0, 128, 0), (0, 300, 900, 300), 0)  # frame
    d.rect(screen, white, (270, 15, 225, 275), 10)  # frame
    d.rect(screen, white, (270, 15, 112.5, 105), 10)  # frame
    d.rect(screen, lightBlue, (274, 19, 108.5, 101), 0)  # outdoors
    d.rect(screen, white, (384, 15, 112.5, 105), 10)  # frame
    d.rect(screen, lightBlue, (388, 19, 108.5, 101), 0)  # outdoors
    d.rect(screen, white, (378.5, 120, 10, 175), 0)  # frame
    d.rect(screen, lightBlue, (274, 125, 106, 163))  # outdoors
    d.rect(screen, lightBlue, (388, 125, 108, 163))  # outdoors

draw_window()

def draw_cat():
    d.ellipse(screen, cat, (53, 353, 320, 140))  # body
    d.ellipse(screen, (0, 0, 0), (53, 353, 320, 140), 1)  # body
    d.ellipse(screen, cat, (43, 433, 28, 41))  # leg
    d.ellipse(screen, (0, 0, 0), (43, 433, 28, 41), 1)  # leg
    d.ellipse(screen, cat, (70, 456, 70, 40))  # leg
    d.ellipse(screen, (0, 0, 0), (70, 456, 70, 40), 1)  # leg
    d.circle(screen, cat, (75, 413), 50)  # head
    d.circle(screen, (0, 0, 0), (75, 413), 50, 1)  # head
    #circle(screen, cat, (340, 458), 42)  # hip
    #circle(screen, (0, 0, 0), (340, 458), 42, 1)  # hip
    #ellipse(screen, cat, (362, 468, 28, 65))  # leg
    #ellipse(screen, (0, 0, 0), (362, 468, 28, 65), 1)  # leg
    d.polygon(screen, pink, ((22, 364), (45, 373), (29, 391)))  # left ear
    d.polygon(screen, red, ((22, 364), (45, 373), (29, 391)), 4)  # left ear
    d.polygon(screen, pink, ((113, 357), (114, 382), (96, 368)))  # right ear
    d.polygon(screen, red, ((113, 357), (114, 382), (96, 368)), 4)  # right ear
    d.circle(screen, orange, (54, 413), 17)  # left eye
    #circle(screen, (0, 0, 0), (54, 413), 17, 1)
    d.circle(screen, orange, (96, 413), 17)  # right eye
    #circle(screen, (0, 0, 0), (96, 413), 17, 1)
    d.ellipse(screen, (0, 0, 0), (56, 400, 4, 26))  # left pupil
    d.ellipse(screen, (0, 0, 0), (98, 400, 4, 26))  # right pupil

    # блик в левом глазу
    surface = pygame.Surface((10, 10))
    surface.fill(cat)
    d.ellipse(surface, (255, 255, 255), (0, 0, 5, 10))
    a = pygame.transform.rotate(surface, 50)
    screen.blit(a, (43, 397))
    d.circle(screen, (0, 0, 0), (54, 413), 17, 1)  # left pupil

    # блик в правом глазу
    surface1 = pygame.Surface((10, 10))
    surface1.fill(cat)
    d.ellipse(surface, (255, 255, 255), (0, 0, 5, 10))
    b = pygame.transform.rotate(surface, 50)
    screen.blit(b, (84, 397))
    d.circle(screen, (0, 0, 0), (96, 413), 17, 1)

    # нос
    d.polygon(screen, pink, ((70, 433), (78, 433), (74, 438)))
    d.polygon(screen, (0,0,0), ((69, 432), (79, 432), (74, 440)), 1)

    # рот
    d.aaline(screen, (0, 0, 0), (74, 440), (74, 447))
    d.arc(screen, (0, 0, 0), (75, 444, 10, 6), math.pi, 0)
    d.arc(screen, (0, 0, 0), (65, 444, 10, 6), math.pi, 0)

    # хвост
    surface_tail = pygame.Surface((200, 100))
    surface_tail.fill((0, 128, 0))
    surface_tail.set_colorkey(cat)
    surface_tail.set_colorkey((0,128,0))
    d.ellipse(surface_tail, cat, (0, 0, 180, 60))
    d.ellipse(surface_tail, (0, 0, 0), (0, 0, 180, 60), 1)
    c = pygame.transform.rotate(surface_tail, -30)
    screen.blit(c, (280, 360))

    d.circle(screen, cat, (340, 458), 42)
    d.circle(screen, (0, 0, 0), (340, 458), 42, 1)
    d.ellipse(screen, cat, (362, 468, 28, 65))
    d.ellipse(screen, (0, 0, 0), (362, 468, 28, 65), 1)

    # усы
    d.arc(screen, (0, 0, 0), (78, 428, 120, 50), math.pi/3, 5*math.pi/6)
    d.arc(screen, (0, 0, 0), (70, 434, 130, 50), math.pi/3, 4*math.pi/5.3)
    d.arc(screen, (0, 0, 0), (62, 440, 140, 50), math.pi/3, 4*math.pi/5.55)

    d.arc(screen, (0, 0, 0), (-48, 425, 120, 50), math.pi/6, 5*math.pi/6)
    d.arc(screen, (0, 0, 0), (-56, 430, 130, 50), math.pi/5.4, 5*math.pi/6)
    d.arc(screen, (0, 0, 0), (-64, 435, 140, 50), math.pi/5.1, 5*math.pi/6)

draw_cat()

def draw_ball():
    # клубок
    d.circle(screen, gray, (300, 548), 40)
    d.arc(screen, (0, 0, 0), (290, 538, 10, 30), 2*math.pi/3, 3*math.pi/1.8)
    d.arc(screen, (0, 0, 0), (300, 535, 10, 35), 2*math.pi/3, 3*math.pi/1.8)

draw_ball()

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
