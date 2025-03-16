"""
import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False (до того как закроют окно,цикл игры продолжается)

while not done:  (основной цикл клорый обновляет события игры)
        for event in pygame.event.get():  (все события произошедшие за последний кадр)
                if event.type == pygame.QUIT:  (бфло ли закрытие окноб если да то меняется на тру)
                        done = True
        
        pygame.display.flip()  (отображает все что было нарисовано)
""" 

import pygame

pygame.init()
screen = pygame.display.set_mode((400, 400))
done = False
is_blue = True
x = 30
y = 30

clock = pygame.time.Clock()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_blue = not is_blue
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y -= 3
        if pressed[pygame.K_DOWN]: y += 3
        if pressed[pygame.K_LEFT]: x -= 3
        if pressed[pygame.K_RIGHT]: x += 3
        
        screen.fill((0, 0, 0))
        if is_blue: color = (0, 127, 255)
        else: color = (255, 100, 0)
        pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))
        
        pygame.display.flip()
        clock.tick(60)