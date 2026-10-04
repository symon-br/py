# a = "learn"
# b = "about"
# c = "string"
# d = "variable"
# e = "in"
# f = "python"
# res = c[3] + a[0] + b[2] + d[0] + d[len(d)-1] + b[-2]
# print(res)

import pygame
pygame.init()
screen = pygame.display.set_mode((400,300))
pygame.display.set_caption("My First Game")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
